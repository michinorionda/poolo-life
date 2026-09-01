# POOLO Design System（poolo-ds）

POOLO（by TABIPPO）のイベント告知ページを、**コピペではなく単一ソース**で組み立てるためのデザインシステムです。共通部分を `tokens.css` ＋ `components.css` に切り出し、マークアップはこのカタログ（`index.html`）から写して作ります。

**正規の基準ページ（色・書体・部品）**: `../brand-explore-260708/direction-b2-final.html`
**正規の基準ページ（ページ構成の型・2026-09-01〜）**: `../event-tomonoura-v01-260824/index.html` … 新しい告知ページはこの並びを出発点にする（`BRAND.md` 4章）
このページの `:root` と body 構造から、再利用トークン／コンポーネントを抽出しています。旧基準（`event-30s-v01-260720`、teal＋深緑）からブランドブルーへ全面刷新しました（→末尾「旧デザインからの刷新」）。

---

## ファイル構成

| ファイル | 役割 |
|---|---|
| `tokens.css` | `:root` のデザイントークン（色・書体・レイアウト・角丸・遷移）。**値の唯一の置き場所**。フォントの `@import` もここに1本化。 |
| `components.css` | **告知ページ用**の再利用コンポーネントとレイアウト。色・書体・幅はすべて `var(--…)` 参照。レスポンシブ（860 / 640 / 560px）も各コンポーネントに同居。 |
| `slides.css` | **スライド／OG画像用**のレイヤー（2026-08-31 新設）。1280×720 のアートボード、12種のスライドの型、OG画像・編集型サムネ、印刷→PDF。告知ページとは用途が違うので別ファイルにしてある。 |
| `index.html` | 告知ページのコンポーネントカタログ（プレビュー）。`@dsCard` マーカーで各ブロックを分類。ここのマークアップをコピーして使う。 |
| `slides.html` | **スライドの型カタログ**。12種の型を1枚ずつ実装済み。ここから写して中身を差し替える。 |
| `og.html` | **OG画像・編集型サムネのカタログ**。4種。 |
| `kv.html` | **バナー／キービジュアルのカタログ**（`.kv` 折れ帯の型）。6種。 |
| `BRAND.md` | 言葉・トーン・視覚言語の思想（声のトーン／掲載ルール／ページ構成の型）。 |
| `README.md` | 本書。 |

> **読み込みの組み合わせ**
> 告知ページ → `tokens.css` ＋ `components.css`
> スライド・OG画像 → `tokens.css` ＋ `slides.css`
> （`tokens.css` が常に先。フォントの `@import` はそこに1本化されている）

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

### タイポスケール（2026-08-31 追加）

**追加の理由**：`components.css` のフォントサイズが `9.5 / 10 / 10.5 / 11 / 11.5 / 12 / 12.5 / 13 / 13.5 / 14 / 14.5 / 15px` の **12段階**に膨らんでいた。0.5px 差は視覚的に判別できないので、階層として機能しない ＝ ただのノイズ。判別できる段差だけを残して **9段階（小さい側は4段階）** に整理した。

| トークン | 値 | 用途 |
|---|---|---|
| `--fs-label` | `11px` | 英字ラベル・目次番号（`--en` ＋ `--ls-label` と組む） |
| `--fs-xs` | `12.5px` | 注記・出典・キャプション |
| `--fs-sm` | `14px` | UI・リスト項目・表の中身 |
| `--fs-base` | `16px` | 本文 |
| `--fs-md` | `20px` | リード文・小見出し |
| `--fs-lg` | `26px` | セクション見出し |
| `--fs-xl` | `clamp(30px, 4.0vw, 40px)` | 大見出し |
| `--fs-2xl` | `clamp(38px, 5.6vw, 60px)` | セクションの顔 |
| `--fs-3xl` | `clamp(44px, 6.6vw, 76px)` | Hero |

行間 `--lh-tight/head/body/loose` = `1.35 / 1.55 / 1.95 / 2.15`、字間 `--ls-label/head/body` = `0.18em / 0.04em / 0.02em`。

> **運用ルール**：新規コンポーネントは必ずこのトークンから選ぶ。生の px を書くのは、選べる段がどうしても無いと判断できたときだけ。
> **既存コンポーネントの生 px は互換のため据え置き**（公開中のページを壊さないため）。触るときに1つずつ置き換える。

### 余白スケール（2026-08-31 追加）

数字ではなく **「関係」** で名前を付けている。`--sp-1..8` のような等比の梯子だと「なんとなく中くらい」で選べてしまい、余白が距離を語らなくなるため。この命名なら、使うたびに「これは近いのか遠いのか」を決めることになる。

| トークン | 値 | 意味 |
|---|---|---|
| `--sp-tie` | `6px` | 不可分：ラベルとその値、見出しと添字 |
| `--sp-near` | `12px` | 同じかたまりの中 |
| `--sp-item` | `22px` | 項目と項目 |
| `--sp-group` | `40px` | 小見出しと、その外側 |
| `--sp-block` | `72px` | ブロックとブロック |
| `--sp-sec` | `clamp(88px, 12vh, 132px)` | セクションとセクション |

---

## スライドの作り方（`slides.css`）

1. 新規 HTML を作り、`<head>` で 2ファイルをリンクする（順序厳守）。
   ```html
   <link rel="stylesheet" href="../poolo-ds/tokens.css">
   <link rel="stylesheet" href="../poolo-ds/slides.css">
   ```
   ※ 従来のスライドはトークンを `<style>` にコピペしていたが、**これはやめる**。値の置き場所は `tokens.css` 1箇所。
2. `<body class="deck"><div class="stage">` の中に `<section class="sl sl--◯◯">` を並べる。
3. `slides.html`（型カタログ）から必要な型のマークアップを写して、テキストを差し替える。
4. 末尾の JS（`slides.html` にあるもの）をコピーする。ナビ・キーボード操作・アートボードの拡大縮小が入る。
5. PDF にするときは Chrome の「印刷 → PDFに保存」。**余白：なし／背景グラフィック：オン**。1280×720 の各ページで出る。

### スライドの型（12種）

型を選ぶ ＝ **そのスライドの主役を決める**、という手順にする。迷ったら `.sl--statement`。言いたいことが1つに絞れていないという合図。

| クラス | 型 | 主役 | 使いどころ |
|---|---|---|---|
| `.sl--cover` | 表紙 | タイトル | 1枚目 |
| `.sl--section` | 中扉 | 章番号 | 章の切り替えだけ。多用すると章の重みが消える |
| `.sl--statement` | 主張 | 一文 | 一番強い型。絞るほど効く |
| `.sl--define` | 定義 | 定義文 | 言葉をひとつ確定させる回 |
| `.sl--split` | 対比 | 片方の列 | `.is-lead` / `.is-sub` で主役を必ず決める |
| `.sl--triad` | 3項目 | 3つの並び | 4つ以上並べたくなったら2枚に割る |
| `.sl--figure` | 図解 | 図 | 見出しは短く、言いたいことはキャプションで受ける |
| `.sl--quote` | 引用 | 声 | 参加者の声。加工しない |
| `.sl--data` | 数字 | 数値 | 1枚に3つまで。数字は図として置く |
| `.sl--question` | 問い | 問い | **ブルーのベタ面はここにだけ**使う |
| `.sl--photo` | 写真 | 写真 | 文字は白場に退避。写真の上に直接載せない |
| `.sl--close` | 締め | 最後の一文 | 連絡先や告知は入れない |

共通パーツは天の柱（`.sl-top`：番号／柱／メタ）、本体（`.sl-body`）、地の脚（`.sl-foot`：出典／ページ番号）。**全スライドで天地を必ず揃える**。これだけで「揃っている」印象が出る。

スライド専用のサイズは 6段だけ（`--sfs-label / note / body / lead / head / hero`、＋数字用の `--sfs-data`）。アートボードが固定なので clamp は使わない。

---

## OG画像・編集型サムネ（`slides.css` / `og.html`）

用語（社内）：
- **OG画像** … SNSシェア用に書き出す PNG（**1200×630 固定**）
- **編集型サムネ** … 告知ページ上部に置く HTML/CSS 製のサムネ（可変幅・`.is-fluid`）

| クラス | 型 | 使いどころ |
|---|---|---|
| `.og-wrap` | 標準（白地） | 既定。回のタイトルを主役に |
| `.og-wrap.og--brand` | ブルーのベタ面 | 問い・強いメッセージ。タイムラインで一番効く |
| `.og-wrap.og--photo` | 写真を敷く | 現地開催の回。文字は白パネルに退避 |
| `.og-wrap.is-fluid` | 可変（編集型サムネ） | 告知ページに直接埋め込む。書き出し不要 |

**PNG の書き出し**：Chrome DevTools で `.og-wrap` のノードを選び、右クリック →「Capture node screenshot」。等倍で 1200×630 の PNG になる。

---

## バナー／キービジュアル（`.kv` / `kv.html`）

参照：[HOUYHNHNM のフィーチャーバナー](https://www.houyhnhnm.jp/feature/1140966/)。
ブランドカラーのベタ面を「地」にし、写真をその上に**窓として抜く**型。一文が上の横帯から右の縦帯へ **L字に折れる**のがこの型の核心で、和文が縦に流れることで欧文の横組みと直交し、面が締まる。

### 参照元から、何を取って何を変えたか

| | 内容 |
|---|---|
| **取った** | 地＝ベタ面／写真は窓として抜く／横組み欧文と縦組み和文の直交／折れ帯／色は3色 |
| **変えた（1）** | 地の色を `#189BBC` に。欧文は Jost |
| **変えた（2）** | **縦組みの和文を、参照元の太いゴシックではなく Zen Old Mincho（明朝）にした。** ここが一番の分かれ目で、明朝にすると「ヒップ」が「静けさ」に転調し、POOLO のトーンに寄る |
| **変えた（3）** | 参照元は欧文が写真に少し重なるが、あちらは写真の左上が暗いから成立している。POOLO の写真は空が入って明るいことが多く白ヌキが飛ぶので、**欧文は左カラムの内側で必ず折り返す**（4つの問い④に立ち返った）。そのぶんカラムを広く取った |
| **原則の例外** | DS は「角丸は 2px 基調・乱発しない」だが、窓の対角の大きな R は装飾ではなく**窓の形＝構造**なので例外として認める。角を立てたい回は `.kv--square` |

### クラス

| クラス | 型 | 使いどころ |
|---|---|---|
| `.kv` | 標準（折れ帯・青地） | 既定。回のタイトルを横→縦に折って読ませる |
| `.kv--band` | 簡素版（縦帯だけ） | タイトルが短く、折る必要がないとき |
| `.kv--light` | 静かな版 | 地を白に、帯をブルーに反転。写真を主役にしたい回 |
| `.kv--square` | 直角の窓 | 角を立てたい回。角丸原則に完全に戻した版 |
| `.is-og` / `.is-fluid` | 1200×630 ／ 可変幅 | 内部寸法は全部 `cqw` なので、同じ1組のルールで比率だけ変わる |

構成要素は `.kv-window`（写真の窓）/ `.kv-en`（左上の欧文）/ `.kv-spine`（縦のヘアライン）/ `.kv-vsub`（縦組みの小見出し）/ `.kv-vol`（左下の巻数・期）/ `.kv-fold-h` ＋ `.kv-fold-v`（折れ帯）。

### 書くときの制約（守らないと崩れる）

- **折れ帯は一文を2つに割って入れる。** 横帯に前半、縦帯に後半。縦帯は**目安13文字**。
- **縦組みの小見出しは目安12文字**（「開催地＋短い括弧書き」まで。参照元の「凜太郎（モデル）」と同じ分量）。
- 溢れたぶんは**2列目を作らず切れる**ようにしてある。崩れたまま気づかないより、切れて見えたほうがよいため。切れたら文言を短くする。
- **縦組みの中の半角数字は `<span class="tcy">` で囲む**（縦中横）。囲まないと「3日間」の 3 が寝る。ラテン語（Compath など）は回転したままが正しいので囲まない。
- `.kv-*` は `<p>` で書くので、**slides.css 側で margin: 0 と box-sizing: border-box を持たせてある**（ページ側の reset に依存しない。margin を消し忘れると横帯だけ 1em 下がって、L字ではなく十字になる）。
- **横帯と縦帯の中央寄せは `line-height: var(--kv-bar)`（行送り＝帯の太さ）で取る。`flex` + `justify-content` は使わない。** 縦組みでは flex の主軸が縦に入れ替わるので `justify-content` が横方向に効かず、縦帯の文字だけ帯の右端に寄って、折れ角で文字の流れがガタつく。字間も横帯・縦帯で揃える（同じ一文を折っているため）。

---

## デザイン判断の基準（4つの問い）

新しく何かを組むとき、参照を保存するときに必ず通す。詳細と参照リストは Obsidian の [デザイン参照ライブラリ]（`POOLO-Vault/15_References/`）。

1. **文字の階層は何段階あるか** — 大きさだけで差をつけていないか。3〜4段階で止まっているか
2. **余白は「距離」を語っているか** — 関係が近い情報は近く、別の話は遠く
3. **色は3つに収まっているか** — 地 `#F9F9F9` / 墨 `#000000` / 差し色 `#189BBC`。4色目が入った瞬間に素人っぽくなる
4. **主役がどちらか決まっているか** — 写真が主役なら文字は退く。両方主役にすると両方死ぬ

`slides.css` はこの4つをレイアウト側で担保するように書いてある（① 段は6つで打ち止め ② 余白は関係で命名 ③ `--brand` 以外の色相を入れない ④ 型を選ぶ＝主役を決める）。

---

## 日本語の改行則

見出し・本文が「消費ではな／く」「独り言のま／ま。」のように**語の途中で泣き別れる**のを防ぐため、`components.css` の冒頭で以下を当てています。

| プロパティ | 効果 |
|---|---|
| `word-break: auto-phrase` | 文節単位で改行する。**`<html lang="ja">` が必須**（無いと効かない）。非対応ブラウザは従来どおりの改行に戻るだけ。 |
| `text-wrap: pretty` | 最終行に1〜2文字だけ取り残されるのを減らす。 |

- `text-wrap: balance` は**使いません**。和文見出しだと1行目が極端に短くなり、意味の切れ目より行長を優先してしまうため。
- それでも位置が気に入らないときは、従来どおり `<br>` と `.nb`（`white-space:nowrap`）で明示的に固定します。
- ただし**幅が内容に追従する要素**（`display:flex` / `inline-block` など）に `.nb` を入れると、その幅に合わせて全体が折り返され行が崩れます。これらは `auto-phrase` に任せてください。
- 新しいテキスト系コンポーネントを足したら、冒頭の改行則セレクタにもクラスを追加すること。

---

## コンポーネント一覧

group はカタログの `@dsCard group="…"` と対応。

| クラス | 用途 | group |
|---|---|---|
| `.brand-row` / `.header-link` / `.header-cta` | 固定ヘッダー＋申込ボタン（下辺ヘアライン） | Header |
| `.mon` | 家紋モノグラム（ブルー線画SVG） | Header |
| `.hero` / `.hero-grid` / `.hero-copy` / `.hero-photo` / `.hero-chip` | 写真ドリブンHero（左コピー＋右裁ち落とし写真） | Hero |
| `.hero--long-title` | 長い和文タイトル用のHero変種（`.hero` に付ける）。コピー欄を46%→51%に広げ、右パディングと `t-lg` を調整して、大見出しが写真に重なるのを防ぐ。**和文6文字以上を `t-lg` の1行に置くときは既定だと溢れる**ので、この変種を使う。中身は `@media (min-width: 861px)` で囲ってある（囲まないと860px以下の1カラム化を後勝ちで打ち消す） | Hero |
| `.hero-eyebrow` / `.hero-title`(.t-sm/.t-lg .em) / `.hero-lead` / `.hero-foot` | Hero内のコピー要素（見出しは明朝、強調語だけブルー） | Hero |
| `.hero-band` / `.hero-band-num`(.dow) / `.hero-band-time` / `.hero-band-meta` | ブルーの全幅日付帯 | Hero |
| `.step-band` / `.step-band-head` / `.step-cell` / `.step-no` / `.step-title` / `.step-desc` | プログラム要約帯（日付帯の直下。3ステップを横並びで先に見せる） | Hero |
| `.sec` / `.sec-inner` / `.sec-spine` / `.sec-num`(.ja/.small) / `.sec-en` / `.sec-title` / `.sec-lead` | セクション枠＋非対称スパイン（連番／和文ラベル＋明朝見出し） | Sections |
| `.intro-body` / `.quoted` | 導入本文＋引用色。**導入の途中で一文だけを強調する装置は置かない**（`.intro-break` は 2026-09-01 に廃止。転換は組版ではなく文章で示す） | Sections |
| `.flow-list` / `.flow-item` / `.flow-time` / `.flow-title` / `.flow-desc` | 当日の流れ（4フェーズ・時刻＋タイトル＋説明） | Sections |
| `.sec-questions` / `.q-list` / `.q-item` / `.q-no`(.kanji) / `.q-text` / `.q-helper` | 当日の問い（ブルー淡面・漢数字番号・明朝） | Sections |
| `.notice-bar` / `.notice-tag` / `.notice-text` / `.notice-link` | お知らせバンド（一行アナウンス） | Content |
| `.summary` / `.summary-grid` / `.summary-cell` / `.summary-label`(.en/.ja) / `.summary-value` | イベント要点（4カラム：日時／形式／定員／参加費） | Content |
| `.photo-break`(--left/--right) / `.pb-frame` / `.pb-caption`(-en/-rule/-text) | 写真ブレイク（裁ち落とし＋足元ブルー淡面＋編集キャプション） | Content |
| `.voice-list` / `.voice-item` / `.voice-quote`(.vq-mark) / `.voice-attr` / `.voice-note` | 参加者の声（引用＝明朝・属性＝Noto・掲載注記） | Content |
| `.about` / `.about-inner` / `.about-title` / `.about-text` / `.about-figs` / `.about-fig` | About POOLO（企画者・信頼の小コーナー） | Content |
| `.faq-list` / `.faq-item` / `.faq-q`(.m) / `.faq-a`(.m) | FAQ（Q/A ヘアライン区切り） | Content |
| `.gallery` / `.gallery-head`(-en/-rule/-text) / `.g-grid` / `.g-item`(.is-wide/.is-tall/.is-big) / `.g-strip` / `.gallery-note` | 写真ギャラリー（点数の多い旅ページ用。モザイク or 全幅の横スクロール帯。目地は1pxヘアラインのみ） | Content |
| `.program-steps` / `.program-step`(.is-main) / `.ps-num` / `.ps-tag`(.is-quiet) / `.ps-title` / `.ps-desc` / `.ps-meta` | プログラムの3ステップ（事前→現地→事後のような、前後を含む一連の流れ。主役の回は `.is-main`） | Sections |
| `.point-list` / `.point-item` / `.point-num`(.no) / `.point-title` / `.point-desc` | 体験の要点（「この体験で得られる4つのこと」を2列で） | Sections |
| `.ba-flow` / `.ba-col`(--after) / `.ba-label`(.en) / `.ba-items` / `.ba-arrow` | 旅の前と後（Before → After。成果を約束せず変化の幅を示す） | Sections |
| `.day-block` / `.day-head` / `.day-num` / `.day-date` / `.day-note` | 日別の見出し（複数日のスケジュールで `.flow-list` の直前に置く） | Sections |
| `.people-list` / `.person` / `.person-photo`(.is-empty) / `.person-role` / `.person-name`(.ruby) / `.person-bio` / `.person-links` | 出会う人・登壇者（写真＋肩書＋名前＋略歴＋外部リンク。未入稿は `.is-empty`） | Content |
| `.fee-grid` / `.fee-card`(--sub) / `.fee-label` / `.fee-price` / `.fee-note` / `.fee-add` / `.fee-foot` | 参加費（プログラム参加費と現地実費を分けて示す。合算を主役にしない） | Application |
| `.date-list` / `.date-item`(.is-special) / `.date-no` / `.date-when`(.dow/.time) / `.date-what` / `.date-note` | 開催日程一覧（複数回の講座・ゼミ。別日程の回は `.is-special`） | Application |
| `.fit-grid` / `.fit-col`(--yes/--no) / `.fit-head`(.en) / `.fit-items` | 向き・不向き（こんな方へ／今回は向かないかも の2カラム） | Application |
| `.apply-steps` / `.apply-step` / `.apply-step-num` / `.apply-step-title` / `.apply-step-desc` | 申込ステップ（申込→受講開始までの4手順） | Application |
| `.terms-list` / `.terms-row` / `.terms-k` / `.terms-v` | 募集要項（締切・支払い・キャンセルポリシー） | Application |
| `.cta` / `.cta-inner` / `.cta-en` / `.cta-title` / `.cta-lead` / `.cta-btn` / `.cta-note` | 中間・最終CTA（ブルーのベタ面＋白ボタン。`.cta-lead` は最終CTAのクロージング文） | CTA |
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
