// index.html の <body> 内の日本語テキストに、BudouXの文節区切りで <wbr> を入れる（冪等：既存の<wbr>は一度外す）
const fs = require('fs');
const { loadDefaultJapaneseParser } = require('budoux');
const parser = loadDefaultJapaneseParser();
const [,, file] = process.argv;
const FIX = [
  ["町の<wbr>人と", "町の人と"],
  ["ある<wbr>方", "ある方"],
  ["こんぴら<wbr>参り", "こんぴら参り"],
  ["渡航国数は<wbr>51", "渡航国数は51"],
  ["町の<wbr>方々", "町の方々"],
  ["<wbr></a>", "</a>"],
  ["好きな<wbr>こと", "好きなこと"],
  ["興味が<wbr>ある", "興味がある"],
  ["話してくれるようになりました", "話して<wbr>くれるように<wbr>なりました"],
  ["心ゆく<wbr>まで", "心ゆくまで"],
  ["こん<wbr>ぴらさん", "こんぴらさん"],
  ["ぴらさん<wbr>へ", "ぴらさんへ"],
  ["商店<wbr>街", "商店街"],
  ["株式会社地方<wbr>創生", "株式会社地方創生"],
  ["手が<wbr>けている", "手がけている"],
  ["高松<wbr>空港", "高松空港"],
  ["清水 直<wbr>哉", "清水 直哉"],
  ["しみな<wbr>お", "しみなお"],
  ["一人<wbr>ひとり", "一人ひとり"],
  ["移り<wbr>住", "移り住"],
  ["変わり<wbr>はじめた", "変わりはじめた"],
  ["気に<wbr>なっ", "気になっ"],
  ["過ごし方<wbr>や", "過ごし方や"],
  ["誰に<wbr>でも", "誰にでも"],
  ["と<wbr>いう", "という"],
  ["と<wbr>して", "として"],
  ["その<wbr>あとも", "そのあとも"],
  ["もう<wbr>一度", "もう一度"],
  ["よく<wbr>ある<wbr>質問", "よくある質問"],
  ["会う<wbr>人たち", "会う人たち"],
  ["申込方<wbr>法", "申込方法"],
  ["主な<wbr>対象", "主な対象"],
  ["こんな<wbr>方<wbr>へ", "こんな方へ"],
  ["時間の<wbr>ある方", "時間のある方"],
  ["ある<wbr>方POOLO", "ある方POOLO"],
  ["ひと<wbr>つ<wbr>決めた", "ひとつ<wbr>決めた"],
  ["人た<wbr>ちがいるのかを", "人たちが<wbr>いるのかを"],
  ["その<wbr>とき町で", "そのとき<wbr>町で"]
];
let html = fs.readFileSync(file, 'utf8');
const bi = html.indexOf('<body>');
let head = html.slice(0, bi), body = html.slice(bi);
body = body.replace(/<wbr>/g, '').replace(/\u2060/g, '');
let out = '', i = 0, skip = null;
while (i < body.length) {
  if (body[i] === '<') {
    const j = body.indexOf('>', i);
    const tag = body.slice(i, j + 1);
    if (/^<(script|style)\b/i.test(tag)) skip = tag.match(/^<(\w+)/)[1].toLowerCase();
    if (skip && new RegExp('^</' + skip, 'i').test(tag)) skip = null;
    if (tag.startsWith('<!--')) { const k = body.indexOf('-->', i); out += body.slice(i, k + 3); i = k + 3; continue; }
    out += tag; i = j + 1; continue;
  }
  const j = body.indexOf('<', i); const end = j < 0 ? body.length : j;
  const text = body.slice(i, end);
  if (!skip && /[぀-ヿ一-鿿]/.test(text)) {
    // 実体参照を壊さないよう、&...; を含む区間はそのまま
    const lead = text.match(/^\s*/)[0], trail = text.match(/\s*$/)[0];
    const core = text.slice(lead.length, text.length - trail.length);
    out += lead + parser.parse(core).join('<wbr>') + trail;
  } else out += text;
  i = end;
}
// 折り返さない語（.nb）の前後は、要素の境目なので改行位置がない。前後に <wbr> を足す
out = out.replace(/<span class="nb">((?:[^<]|<wbr>)*)<\/span>/g, '<wbr><span class="nb">$1</span><wbr>').replace(/(?:<wbr>)+/g, '<wbr>');
// .nb の中の <wbr> は外す（Chromeは nowrap の中でも <wbr> で折り返すため）。.nb の直後が助詞・句読点なら <wbr> を入れない
out = out.replace(/<span class="nb">((?:[^<]|<wbr>)*)<\/span>/g, (m, t) => '<span class="nb">' + t.replace(/<wbr>/g, '') + '</span>');
out = out.replace(/<\/span><wbr>([をのとがにもへでやな、。])/g, '</span>$1');
// リンクの頭の <wbr> は要らない
out = out.replace(/(<a\b[^>]*>)<wbr>/g, '$1');
// 段落の頭と終わりの <wbr> は要らない
out = out.replace(/(<(?:p|li|dd|dt|h1|h2|div)\b[^>]*>)<wbr>/g, '$1').replace(/<wbr>(<\/(?:p|li|dd|dt|h1|h2|div)>)/g, '$1');
// BudouXの区切りで読みにくいものを、ひとまとまりに戻す
for (const [a, b] of FIX) out = out.split(a).join(b);
// 「香川・琴平」は中黒で切らない
out = out.split('香川・<wbr>琴平').join('香川・琴平').split('香川・琴平').join('香川・\u2060琴平');
// 閉じかっこのすぐ後ろの助詞で行が変わらないよう、間に WORD JOINER（U+2060）を入れる
out = out.replace(/([」』）〉])(?:<wbr>)?([をのとがにもへでやな])/g, '$1\u2060$2');
// 本文の段落（行末まで詰めて組む段落）は、最後の文節を折り返さない。「す。」だけの最終行を防ぐ
out = out.replace(/(<(p|dd) class="[^"]*\b(?:body|feel-body|feel-note|person-bio|guest-bio|take-body|faq-a)\b[^"]*">(?:(?!<\/\2>)[\s\S])*?)<wbr>([^<]{1,10})(<\/\2>)/g, '$1<span class="nb">$3</span>$4');
fs.writeFileSync(file, head + out);
