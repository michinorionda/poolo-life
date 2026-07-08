# POOLO Design System（poolo-ds）

POOLO（by TABIPPO）のイベント告知ページを、**コピペではなく単一ソース**で組み立てるためのデザインシステムです。
これまで各告知ページ（`event-30s-v01-*` 等）は完成HTMLを丸ごとコピーして量産していました。ここではその共通部分を `tokens.css` ＋ `components.css` に切り出し、マークアップはこのカタログから写す運用にします。

抽出元（正規の基準ページ）: `../event-30s-v01-260720/index.html`

---

## ファイル構成

| ファイル | 役割 |
|---|---|
| `tokens.css` | `:root` のデザイントークン（色・タイポ・余白・線・角丸・影・幅・遷移）。**値の唯一の置き場所**。 |
| `components.css` | 再利用コンポーネントとレイアウト。色・サイズはすべて `var(--…)` でトークン参照。レスポンシブ（〜720px）も含む。 |
| `index.html` | コンポーネントカタログ（プレビュー）。`@dsCard` マーカーで各ブロックを分類。ここのマークアップをコピーして使う。 |
| `README.md` | 本書。 |

---

## 新しい告知ページの作り方

1. 新規ディレクトリを作り、`<head>` で Google Fonts（`Noto Sans JP` / `Shippori Mincho B1`）を読み込む。
2. その下で 2ファイルをリンクする（順序厳守：tokens が先）。
   ```html
   <link rel="stylesheet" href="../poolo-ds/tokens.css">
   <link rel="stylesheet" href="../poolo-ds/components.css">
   ```
   ※ 現行ページのように1ページ完結にしたい場合は、2ファイルの中身を `<style>` に貼り付けてもよい。
3. `index.html`（カタログ）から必要なコンポーネントのマークアップをコピーし、テキストと画像パスを差し替える。
4. **イベント固有で変えるのはコピー・日付・画像だけ**。CSS（クラス・トークン）は触らない。全ページ共通で直したいときは `poolo-ds` 側を1回直す。

---

## トークン一覧（要約）

`tokens.css` 冒頭のブランドコメントも参照。実装アクセントは `#1B99B7`（既存ページに一致）、公式ブランドカラー `#189BBC` は `--brand-primary` としてサムネ内で使用。

### 色
| トークン | 値 | 用途 |
|---|---|---|
| `--brand-primary` | `#189BBC` | 公式メインカラー（Hero Dサムネ専用） |
| `--accent` / `--cta` | `#1B99B7` | リンク・数字・CTA（本文実装値） |
| `--accent-deep` / `--cta-deep` | `#157A98` | 強調テキスト・ホバー |
| `--accent-light` | `#B8E0EB` | 淡いアクセント |
| `--main` / `--main-soft` | `#2D3E36` / `#4A5A52` | 見出し・主要テキストの深緑 |
| `--sub` / `--sub-light` | `#7A9E8A` / `#B8D0C2` | DON'T・箇条・キャプションのくすみ緑 |
| `--text` / `--text-soft` / `--text-light` | `#2A2A2A` / `#5A5A5A` / `#7A7A7A` | 本文・補助・注釈 |
| `--bg` / `--bg-soft` / `--bg-warm` | `#FFFFFF` / `#FFFCF6` / `#FBF7EE` | 背景（白／暖色白／ベージュ） |
| `--line` / `--line-light` | `#EAE5DC` / `#F2EDE3` | 区切り線 |
| `--hd-ink` / `--hd-hairline` | `#111111` / `#E8E8E8` | サムネの黒・内側仕切り |

### タイポ
| 種別 | トークン |
|---|---|
| フォント | `--font-jp`（Noto Sans JP）/ `--font-serif`（Shippori Mincho B1）/ `--font-latin`（将来 Jost 候補） |
| サイズ | `--fs-3xs 11` … `--fs-base 16` … `--fs-3xl 30` / `--fs-4xl 36` / `--fs-5xl 56` |
| 行間 | `--lh-tight 1.5` / `--lh-normal 1.9`（body）/ `--lh-loose 2.15` |
| 字間 | `--ls-base 0.04em`（body）/ `--ls-caps 0.18em` / `--ls-eyebrow 0.3em` / `--ls-vertical 0.45em` |

### 余白・レイアウト・その他
| 種別 | トークン |
|---|---|
| 余白 | `--space-2xs 8` … `--space-3xl 72` / `--space-section-y 72` / `--space-cta-y 120` |
| 幅 | `--w-article 928` / `--w-section 840` / `--w-narrow 720` / `--w-lead 640` |
| 角丸 | `--radius-xs 2` / `--radius-sm 4` / `--radius-md 8` / `--radius-pill 999` |
| 影 | `--shadow-card` / `--shadow-hd` / `--shadow-cta` / `--shadow-float` / `--shadow-fixed` |
| 遷移 | `--trans-fast .2s` / `--trans-base .25s` / `--trans-slow .35s` |

---

## コンポーネント一覧

group はカタログの `@dsCard group="…"` と対応。

| クラス | 用途 | group |
|---|---|---|
| `.header` / `.header-cta` | 固定ヘッダー＋申込ボタン | Meta |
| `.notice` | 上部お知らせ帯 | Meta |
| `.event-summary` | 日時/形式/定員/参加費の2カラム要点 | Meta |
| `.details-table` | 末尾の開催概要テーブル | Meta |
| `.footer` | 2社ロゴ＋コピーライト | Meta |
| `.section` / `.section-narrow` | 標準セクション枠（840 / 720px） | Layout |
| `.section-title[data-num]` / `.section-lead` | 連番つき見出し＋リード | Layout |
| `.section-mark` / `.page-side-mark` | セクション区切り・縦書きサイドあしらい | Layout |
| `.hd`（Hero D） | HTML/CSS編集型サムネ（16:9）。日付3か所差替え | Hero |
| `.hero` / `.hero-banner` | 画像差し替え型ヒーロー（旧／代替） | Hero |
| `.intro-text` / `.intro-break` | 導入本文＋一言ブレイク | Sections |
| `.theme-main` | 「向き合うこと」本文 | Sections |
| `.flow-list` / `.flow-item` | タイムテーブル（時間＋見出し） | Sections |
| `.worksheet-questions` / `.wq-card` | 当日の問いカード（Q.） | Sections |
| `.dialogue-rules-grid` | 対話ルール DO/DON'T 2カラム | Sections |
| `.terms-list` / `.terms-item` | ✓つき確認事項 | Sections |
| `.target-list` / `.target-item` | ダッシュ箇条「こんな方へ」 | Sections |
| `.about-text` / `.about-closing` / `.about-award` | 企画理由・運営紹介 | Sections |
| `.apply-steps` / `.apply-step` | お申込みステップ番号カード | Sections |
| `.btn` / `.btn-accent` / `.btn-link` | ボタン各種 | CTA |
| `.cta-mid` | 中間CTA | CTA |
| `.cta` | 最終CTA | CTA |
| `.float-apply` / `.sp-fixed-cta` | スクロール追従CTA（PC右上／SP下部）※要JS | CTA |
| `.photo-break` | フルブリード写真区切り | Sections |

### 追従CTA用のJS（`.float-apply`）
スクロール60%で `.is-visible` を付与する小さなスクリプトが基準ページ末尾にあります。新規ページにもそのままコピーしてください。

---

## 命名規則

- **ブロック単位のクラス名**（BEMのゆるい適用）。`block` → `block-element`（例：`event-summary` → `event-summary-row` → `dt/dd`）。
- **状態**は `.is-visible` のように `is-` プレフィックス。
- **セクション見出しの連番**は `data-num="01"` 属性で持たせ、CSSの `::before` が描画（HTMLに数字を書かない）。
- **フォント**はクラス側で毎回 `font-family: var(--font-jp|--font-serif)` を明示（継承に頼らない現行方針を踏襲）。
- 色・サイズの**生値は書かない**。必ず `var(--…)`。トークンに無い一度きりの値だけ例外的に直書き（例：サムネの `#D6E9EF`）。

---

## 更新フロー

1. 全ページ共通の変更（色・余白・コンポーネント修正）は **`poolo-ds` 側だけ**を編集する。
2. 値の変更は `tokens.css`、見た目の構造は `components.css`。
3. 変更後は `index.html`（カタログ）で表示を確認。カタログが壊れていなければ各ページにも安全に反映される。
4. 新コンポーネントを足すときは、`components.css` に `/* ===== 名前 ===== */` 区切りで追記し、カタログにも `<!-- @dsCard group="…" -->` 付きのプレビューを1つ足す。

---

## 既知の命名の揺れ（今後の整理メモ）

- **`--accent` と `--cta` が同値（#1B99B7）**。意味づけ（リンク色 / 申込導線色）で分けているが実質重複。将来ブランド青を1トークンに寄せるなら `--accent` を正とし、`--cta` はエイリアスに。
- 同様に **`--accent-deep` と `--cta-deep`** も同値の重複。
- **サムネの `#189BBC`（公式）と本文の `#1B99B7`（実装）が微妙に異なる**。今は意図的に共存（`--brand-primary` vs `--accent`）。ブランド厳密化するなら本文も `#189BBC` に寄せる判断があり得る。
- **Hero D のタイトル行に2系統**：標準型 `.hd-title-row1/-row2` と 30代型 `.hd-title-row2-sm/-lg/-90`。どちらも残置。定型化するなら「small/large/suffix」の命名に統一するのが素直。
- サイズに**トークン化されていない中間値**（14.5px, 15.5px, 17px, 11.5px 等）が本文に残る。可読性のための微調整なので当面は直書きのまま許容。
