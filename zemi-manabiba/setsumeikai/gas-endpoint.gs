/**
 * POOLOゼミ 説明会ワークシート — 回答受け取り用エンドポイント
 * ------------------------------------------------------------
 * 参加者が書きながら何度でも送信でき、そのたびに同じ行が上書きされます。
 * （送信IDで突き合わせるので、1人1行のまま最新の内容が入ります）
 *
 * 【初回セットアップ】所要5分
 *   1. https://script.google.com/ を開き「新しいプロジェクト」
 *   2. このファイルの中身を全部貼り付けて保存
 *   3. 関数プルダウンで setup を選び「実行」→ 初回のみ承認を許可
 *      → 実行ログにスプレッドシートのURLが出るので開いておく
 *   4. 右上「デプロイ」→「新しいデプロイ」→ 種類の選択で「ウェブアプリ」
 *        次のユーザーとして実行: 自分
 *        アクセスできるユーザー: 全員                 ← ここ重要
 *   5. 発行された .../exec のURLを worksheet.html の ENDPOINT に貼る
 *
 * 【コードを更新したとき】所要30秒・URLは変わりません
 *   右上「デプロイ」→「デプロイを管理」→ 鉛筆アイコン
 *   → バージョン「新バージョン」を選択 → 「デプロイ」
 *   ※ これをやらないと古いコードが動き続けます
 */

var SHEET_NAME = '回答';
var PROP_KEY = 'SPREADSHEET_ID';

var HEADERS = [
  '最終更新',
  '開催回',
  'お名前',
  '① 旅で心が動いた瞬間（10個）',
  '記入数',
  '② 黙っていられない原石',
  '③ 仮テーマ（1行）',
  '④ 来てほしいたった一人',
  '更新回数',
  '送信ID'
];

var COL_UPDATED = 1;
var COL_COUNT   = 9;   // 更新回数
var COL_ID      = 10;  // 送信ID

/** 初回セットアップ：スプレッドシートを作り、IDを保存する */
function setup() {
  var ss = getSpreadsheet_();
  ensureHeaders_(getSheet_());
  Logger.log('スプレッドシートURL: ' + ss.getUrl());
  Logger.log('この URL をブックマークしてください。回答はここに溜まります。');
  return ss.getUrl();
}

/** 保存先スプレッドシートを取得（なければ作る） */
function getSpreadsheet_() {
  var props = PropertiesService.getScriptProperties();
  var id = props.getProperty(PROP_KEY);

  if (id) {
    try {
      return SpreadsheetApp.openById(id);
    } catch (e) {
      // 削除された等。作り直す
    }
  }

  var ss = SpreadsheetApp.create('POOLOゼミ説明会 ワークシート回答');
  props.setProperty(PROP_KEY, ss.getId());

  var sheet = ss.getSheets()[0];
  sheet.setName(SHEET_NAME);
  initSheet_(sheet);

  return ss;
}

/** 回答シートを取得（なければ作る） */
function getSheet_() {
  var ss = getSpreadsheet_();
  var sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
    initSheet_(sheet);
  }
  return sheet;
}

/** 見出し行と体裁 */
function initSheet_(sheet) {
  ensureHeaders_(sheet);

  sheet.setFrozenRows(1);
  sheet.setColumnWidth(1, 150);  // 最終更新
  sheet.setColumnWidth(2, 90);   // 開催回
  sheet.setColumnWidth(3, 110);  // お名前
  sheet.setColumnWidth(4, 420);  // ①
  sheet.setColumnWidth(5, 70);   // 記入数
  sheet.setColumnWidth(6, 300);  // ②
  sheet.setColumnWidth(7, 300);  // ③
  sheet.setColumnWidth(8, 300);  // ④
  sheet.setColumnWidth(9, 80);   // 更新回数
  sheet.setColumnWidth(10, 90);  // 送信ID

  sheet.getRange(2, 1, sheet.getMaxRows() - 1, HEADERS.length)
    .setVerticalAlignment('top')
    .setWrap(true);

  // 送信IDは普段見えなくてよい
  sheet.hideColumns(COL_ID);
}

/** 見出し行が最新でなければ書き直す（既存シートの移行にも対応） */
function ensureHeaders_(sheet) {
  var current = sheet.getRange(1, 1, 1, HEADERS.length).getValues()[0];
  var same = true;
  for (var i = 0; i < HEADERS.length; i++) {
    if (current[i] !== HEADERS[i]) { same = false; break; }
  }
  if (same) return;

  sheet.getRange(1, 1, 1, HEADERS.length)
    .setValues([HEADERS])
    .setFontWeight('bold')
    .setBackground('#DDECF1')
    .setFontColor('#127E9A');
}

/** 参加者のブラウザからの送信を受ける（同じ送信IDなら上書き） */
function doPost(e) {
  var lock = LockService.getScriptLock();
  try {
    lock.waitLock(20000);
  } catch (err) {
    return json_({ ok: false, error: 'busy' });
  }

  try {
    if (!e || !e.postData || !e.postData.contents) {
      return json_({ ok: false, error: 'no payload' });
    }

    var d = JSON.parse(e.postData.contents);
    var sheet = getSheet_();
    ensureHeaders_(sheet);

    var list = Array.isArray(d.s1) ? d.s1 : [];
    var filled = list.filter(function (v) { return v && String(v).trim(); });
    var id = String(d.id || '').trim();

    var row = [
      new Date(),
      d.session || '',
      d.name || '（無記名）',
      filled.join('\n'),
      filled.length,
      d.s2 || '',
      d.s3 || '',
      d.s4 || '',
      1,
      id
    ];

    var target = id ? findRowById_(sheet, id) : 0;

    if (target) {
      var prev = sheet.getRange(target, COL_COUNT).getValue();
      row[COL_COUNT - 1] = (Number(prev) || 0) + 1;
      sheet.getRange(target, 1, 1, HEADERS.length).setValues([row]);
      return json_({ ok: true, mode: 'update', count: row[COL_COUNT - 1] });
    }

    sheet.appendRow(row);
    return json_({ ok: true, mode: 'create', count: 1 });

  } catch (err) {
    return json_({ ok: false, error: String(err) });
  } finally {
    lock.releaseLock();
  }
}

/** 送信IDから既存行を探す。なければ 0 */
function findRowById_(sheet, id) {
  var last = sheet.getLastRow();
  if (last < 2) return 0;

  var ids = sheet.getRange(2, COL_ID, last - 1, 1).getValues();
  for (var i = 0; i < ids.length; i++) {
    if (String(ids[i][0]).trim() === id) return i + 2;
  }
  return 0;
}

/** 疎通確認用。ブラウザでURLを開くと {"ok":true} が出れば成功 */
function doGet() {
  return json_({ ok: true, msg: 'POOLO zemi worksheet endpoint is alive' });
}

function json_(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
