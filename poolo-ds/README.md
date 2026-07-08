# POOLO Design System（poolo-ds）

POOLO（by TABIPPO）のイベント告知ページを、**コピペではなく単一ソース**で組み立てるためのデザインシステムです。共通部分を `tokens.css` ＋ `components.css` に切り出し、マークアップはこのカタログ（`index.html`）から写して作ります。

**正規の基準ページ（新デザインの実体）**: `../brand-explore-260708/direction-b2-final.html`
このページの `:root` と body 構造から、再利用トークン／コンポーネントを抽出しています。旧基準（`event-30s-v01-260720`、teal＋深緑）からブランドブルーへ全面刷新しました（→末尾「旧デザインからの刷新」）。

---

## ファイル構成

| ファイル | 役割 |
|---|---|
| `tokens.css` | `:root` のデザイントークン（色・書体・レイアウト・角丸・遷移）。**値の唯一の置き場所**。フォントの `@import` もここに1本化。 |
| `components.css` | 再利用コンポーネントとレイアウト。色・書体・幅はすべて `var(--…)` 参照。レスポンシブ（860 / 640 / 560px）も各コンポーネントに同居。 |
| `index.html` | コンポーネントカタログ（プレビュー）。`@dsCard` マーカーで各ブロックを分類。ここのマークアップをコピーして使う。 |
| `BRAND.md` | 言葉・トーン・視覚言語の思想（声のトーン／掲載ルール／ページ構成の型）。 |
| `README.md` | 本書。 |

---

## 新しい告知ページの作り方

1. 新規ディレクトリを作る。**フォントは tokens.css の `@import` が読むので、個別の Google Fonts 読み込みは不要。**
2. `<head>` で 2ファイルをリンクする（順序厳守：tokens が先）。
   ```html
   <link rel="stylesheet" href="../poolo-ds/tokens.css">
   <link rel="stylesheet" href="../poolo-ds/components.css">
   ```
   ※ 1ページ完結にしたい場合は、2ファイルの中身を `<style>` に貼り付けてもよい（基準ページはこの形）。
3. `index.html`（カタログ）から必要なコンポーネントのマークアップをコピーし、テキストと画像パスを差し替える。
4. **イベント固有で変えるのはコピー・日付・画像だけ**。CSS（クラス・トークン）は触らない。全ページ共通で直したいときは `poolo-ds` 側を1回直す。
5. 追従CTA（`.float-apply`）を使うなら、末尾のJS（下記）をHTMLに貼る。

---

## トークン一覧（要約）

主役は公式ブランドカラー **`#189BBC`（`--brand`）**。文字は黒、背景は白、罫はヘアライン。脱AI原則としてグラデ・blur影・角丸の乱発はしない（角丸は 2px 基調、影トークンは置かない）。

### 色
| トークン | 値 | 用途 |
|---|---|---|
| `--brand` | `#189BBC` | 公式メイン。ベタ面・CTA・数字・罫の基準 |
| `--brand-deep` | `#127E9A` | ホバー／強調テキスト（引用など） |
| `--brand-mid` | `#8FC6D6` | 中間トーン（補助） |
| `--brand-pale` | `#DDECF1` | 最淡の面（問い・photo-break の帯） |
| `--ink` / `--ink-soft` | `#000000` / `#1E1E1E` | 見出し純黒 / body 既定 |
| `--ink-72 … --ink-40` | `rgba(0,0,0,.72)`〜`.40` | 補助テキストの黒アルファ段階 |
| `--bg` / `--bg-off` | `#FFFFFF` / `#F9F9F9` | 背景 / 段差のオフホワイト |
| `--line` / `--line-pale` | `#E4E4E4` / `#C2DCE5` | ヘアライン / ブルー面上の淡い罫 |
| `--on-brand` ほか | `#FFFFFF` / `rgba(255,255,255,.92〜.40)` | ブルー面に載る白 |

### タイポ（4書体）
| トークン | 書体 | 役割 |
|---|---|---|
| `--mincho` | Zen Old Mincho | **見出しの"顔"**（Hero・sec-title・引用・問い） |
| `--head` | Zen Kaku Gothic New | データ／UI見出し（要点の値・flow-title・FAQ・ボタン） |
| `--body` | Noto Sans JP | 本文（body 15px / line-height 2.05 / letter-spacing 0.05em） |
| `--en` | Jost | 英字ラベル・数字（日付帯・sec-num・Q番号・コピーライト） |

### レイアウト・その他
| トークン | 値 | 用途 |
|---|---|---|
| `--header-h` | `64px`（≤640px `54px`） | 固定ヘッダー高。body に padding-top で反映 |
| `--shell-max` / `--shell-pad` | `1160px` / `clamp(22px,5.4vw,72px)` | 版面幅 / 左右余白 |
| `--radius` | `2px` | 角丸の基調（タグ・ボタン） |
| `--bw-frame` | `8px`（≤860px 6px） | Hero 写真のブルー額装罫 |
| `--trans-fast/base/slow` | `.2s / .25s / .28s ease` | ホバー / ボタン面 / 追従CTA |
| `--z-header` / `--z-float` | `200` / `180` | 固定ヘッダー / 追従CTA |

---

## コンポーネント一覧

group はカタログの `@dsCard group="…"` と対応。

| クラス | 用途 | group |
|---|---|---|
| `.brand-row` / `.header-link` / `.header-cta` | 固定ヘッダー＋申込ボタン（下辺ヘアライン） | Header |
| `.mon` | 家紋モノグラム（ブルー線画SVG） | Header |
| `.hero` / `.hero-grid` / `.hero-copy` / `.hero-photo` / `.hero-chip` | 写真ドリブンHero（左コピー＋右裁ち落とし写真） | Hero |
| `.hero-eyebrow` / `.hero-title`(.t-sm/.t-lg .em) / `.hero-lead` / `.hero-foot` | Hero内のコピー要素（見出しは明朝、強調語だけブルー） | Hero |
| `.hero-band` / `.hero-band-num`(.dow) / `.hero-band-time` / `.hero-band-meta` | ブルーの全幅日付帯 | Hero |
| `.sec` / `.sec-inner` / `.sec-spine` / `.sec-num`(.ja/.small) / `.sec-en` / `.sec-title` / `.sec-lead` | セクション枠＋非対称スパイン（連番／和文ラベル＋明朝見出し） | Sections |
| `.intro-body` / `.intro-break` / `.quoted` | 導入本文＋一言ブレイク＋引用色 | Sections |
| `.flow-list` / `.flow-item` / `.flow-time` / `.flow-title` / `.flow-desc` | 当日の流れ（4フェーズ・時刻＋タイトル＋説明） | Sections |
| `.sec-questions` / `.q-list` / `.q-item` / `.q-no`(.kanji) / `.q-text` / `.q-helper` | 当日の問い（ブルー淡面・漢数字番号・明朝） | Sections |
| `.notice-bar` / `.notice-tag` / `.notice-text` / `.notice-link` | お知らせバンド（一行アナウンス） | Content |
| `.summary` / `.summary-grid` / `.summary-cell` / `.summary-label`(.en/.ja) / `.summary-value` | イベント要点（4カラム：日時／形式／定員／参加費） | Content |
| `.photo-break`(--left/--right) / `.pb-frame` / `.pb-caption`(-en/-rule/-text) | 写真ブレイク（裁ち落とし＋足元ブルー淡面＋編集キャプション） | Content |
| `.voice-list` / `.voice-item` / `.voice-quote`(.vq-mark) / `.voice-attr` / `.voice-note` | 参加者の声（引用＝明朝・属性＝Noto・掲載注記） | Content |
| `.about` / `.about-inner` / `.about-title` / `.about-text` / `.about-figs` / `.about-fig` | About POOLO（企画者・信頼の小コーナー） | Content |
| `.faq-list` / `.faq-item` / `.faq-q`(.m) / `.faq-a`(.m) | FAQ（Q/A ヘアライン区切り） | Content |
| `.cta` / `.cta-inner` / `.cta-en` / `.cta-title` / `.cta-btn` / `.cta-note` | 中間・最終CTA（ブルーのベタ面＋白ボタン） | CTA |
| `.float-apply` / `.fa-inner` / `.fa-texts`(.fa-main/.fa-sub) / `.fa-btn` | 追従CTA（`.is-visible` で出現・要JS） | CTA |
| `.footer` / `.footer-top` / `.footer-marks` / `.footer-bottom` / `.footer-copy` | フッター（家紋＋2社ロゴ＋コピーライト） | Meta |

---

## 追従CTAのJS（`.float-apply`）

`components.css` にはスクロール表示のJSは含めません。追従CTAを使うページは、以下を `</body>` 直前に貼ってください。
**DOM順の約束**：`.float-apply` を `.brand-row` より**前**に置くこと。CSSの後続兄弟セレクタ `.float-apply.is-visible ~ .brand-row .header-cta { visibility: hidden; }` で、追従CTA表示中はヘッダー右上の申込ボタンを隠す（重複回避）ためです。

```html
<script>
(function () {
  var bar = document.getElementById('floatApply');
  if (!bar) return;
  var hero = document.querySelector('.hero');
  // 最終CTA・フッターが視界に入ったら追従バーを退避（重複回避）
  var sentinels = [document.querySelector('.cta'), document.querySelector('.footer')]
    .filter(function (el) { return el; });
  var threshold = 0;
  var ticking = false;

  function computeThreshold() {
    // ヒーロー（写真＋日付帯）の下端が画面上部 40vh を切った頃に出現。
    if (hero) {
      return hero.offsetTop + hero.offsetHeight - window.innerHeight * 0.4;
    }
    return window.innerHeight * 0.6; // .hero が無い場合のフォールバック
  }

  function update() {
    var nearEnd = sentinels.some(function (el) {
      var r = el.getBoundingClientRect();
      return r.top < window.innerHeight && r.bottom > 0;
    });
    bar.classList.toggle('is-visible', window.scrollY > threshold && !nearEnd);
    ticking = false;
  }

  window.addEventListener('scroll', function () {
    if (!ticking) { window.requestAnimationFrame(update); ticking = true; }
  }, { passive: true });
  window.addEventListener('resize', function () { threshold = computeThreshold(); update(); });
  window.addEventListener('load', function () { threshold = computeThreshold(); update(); });

  threshold = computeThreshold();
  update();
})();
</script>
```

対応する最小マークアップ（`.brand-row` の直前）:

```html
<div class="float-apply" id="floatApply">
  <div class="shell fa-inner">
    <div class="fa-texts">
      <span class="fa-main">30代の生き方を問い直す 90分</span>
      <span class="fa-sub">7/20(月) 20:00〜 ・ オンライン ・ 無料</span>
    </div>
    <a class="fa-btn" href="#">申し込む</a>
  </div>
</div>
```

---

## 命名規則

- **ブロック単位のクラス名**（BEMのゆるい適用）。`block` → `block-element`（例：`hero` → `hero-band` → `hero-band-num`）。
- **状態**は `.is-visible` のように `is-` プレフィックス。
- **バリアント**は `--` サフィックス（例：`.photo-break--left` / `.photo-break--right`）。
- **書体**はクラス側で毎回 `font-family: var(--mincho|--head|--body|--en)` を明示（継承に頼らない）。
  - 大見出しの顔＝`--mincho`、データ／UI見出し＝`--head`、本文＝`--body`、英字数字＝`--en`。
- **セクション番号**は数字なら `.sec-num`（Jost）、和文ラベルなら `.sec-num.ja`（明朝・「問」「声」等）、小さめ和文は `.sec-num.ja.small`（「よくある質問」等）。
- 色・サイズの**生値は書かない**。必ず `var(--…)`。黒の階調は `--ink-72 … --ink-40`、白は `--on-brand-*` を使う。

---

## 更新フロー

1. 全ページ共通の変更（色・余白・コンポーネント修正）は **`poolo-ds` 側だけ**を編集する。
2. 値の変更は `tokens.css`、見た目の構造は `components.css`。
3. 変更後は `index.html`（カタログ）で表示を確認。カタログが壊れていなければ各ページにも安全に反映される。
4. 新コンポーネントを足すときは、`components.css` に `/* ===== 名前 ===== */` 区切りで追記し、カタログにも `<!-- @dsCard group="…" -->` 付きのプレビューを1つ足す。groupは `Foundations / Header / Hero / Sections / Content / CTA / Meta` のいずれか。

---

## 旧デザインからの刷新（teal → ブランドブルー）

`2026-07-08` に、正規リファレンス `direction-b2-final.html` に合わせて全面刷新しました。

- **撤去**：くすみ深緑 `#2D3E36`（`--main`）系、実装アクセント水色 `#1B99B7`（`--accent`/`--cta`）系、くすみ緑 `#7A9E8A`（`--sub`）、暖色オフホワイト（`--bg-soft`/`--bg-warm`）、**blur影**（`--shadow-*` 一式）、**英字イタリックのあしらい**、明朝の Shippori Mincho B1。
- **追加／刷新**：主役を公式 `#189BBC`（`--brand`）1色に統一、明朝を Zen Old Mincho（見出しの顔）に、英字を Jost（`--en`）に、写真ドリブンHero＋ブルー日付帯、非対称スパインのセクション、フラット面＋ヘアライン基調（角丸2px）。
- 旧カタログの group（Meta/Layout/Hero/Sections/CTA）は、新構成（Foundations/Header/Hero/Sections/Content/CTA/Meta）に再編。
