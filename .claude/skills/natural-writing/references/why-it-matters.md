# なぜ AI 感を消すのか（読み手の反応の実証）

前提となる論理は「読み手が AI 製だと感じる → 冷める → 申し込まない」。2023〜2026 年の研究と調査で、この鎖のどこが実証され、どこが推測かを分けた。結論から言うと、**鎖の前半は確立していて、後半は POOLO の文脈でだけ成立する**。

---

## 1. 「AI だと分かると信頼と好感が落ちる」——確立

ランダム化実験で十数本、方向が一貫している。

| 研究 | 対象 | 結果 |
|---|---|---|
| Rubin et al., Nature Human Behaviour 2025（9 実験 n=6,282） | 同一の LLM 生成の共感文に「人間」「AI」ラベルを貼り分け | 「人間」ラベルの方が共感的・支持的と評価。読み手が勝手に「AI が手伝ったのでは」と疑うだけでも低下 |
| Schilke & Reimann, OBHDP 2025（13 の事前登録実験 n>3,000） | 教育・採用・投資・クリエイティブ・社内文書 | AI 利用を開示した主体は、開示しない主体より一貫して信頼が低い |
| Altay & Gilardi, PNAS Nexus 2024（n=4,976） | 見出し | 「AI 生成」ラベルで知覚正確性と共有意向が低下。真偽と実際の作者を問わない。効果量は「虚偽」ラベルの約 1/3 |
| Nakano et al., IUI 2026（n=261、990 評価） | 6 種の文章行為 | 開示で信頼・配慮・有能・好感が低下。**対人的・社交的な文面で最も急落** |
| Zhu et al., ACL Findings 2025 | ブラインドでは区別できない文 | それでも「人間」ラベル側を 30% 超で選好。ラベルを入れ替えても同じ |

効果量は壊滅的ではない（Altay の言い方だと「虚偽ラベルの 1/3」）が、確実にマイナス。

## 2. 「それが申し込みを減らす」——POOLO の文脈では支持される

条件によって成立したり消えたりする。**成立する側の条件が、POOLO の告知ページにほぼ全部当てはまる。**

| 条件 | 罰則が大きい | 罰則が小さい／逆転する |
|---|---|---|
| 商材 | 情緒・体験・対人（寄付、共感、体験プログラム） | 実用財・低関与（EC の商品説明） |
| 関与度 | 高関与（高額・人生の選択） | 低関与 |
| 期待 | 「わざわざ書いてくれた」と読み手が期待する文脈 | 事務的な情報提供 |
| 年齢 | 高年齢層ほど抵抗（JIAA 2025：抵抗あり 37%／なし 22%） | Z 世代・AI 高リテラシー層 |
| 接触 | 長文・複数回接触ほど見抜かれる | 単発・短文 |

- Baek et al., Int. J. Advertising 2024：プロソーシャル広告の AI 開示 → 広告態度低下 → **寄付意向低下**（広告信頼性が媒介）
- Arango et al., J. Advertising 2023：チャリティ広告の AI 生成顔 → 寄付意向低下（共感と予期罪悪感が媒介）
- Mansouri et al. 2025（GoFundMe 実データ 117,000 件＋実験）：AI 的文章のキャンペーンは集金額が多い。ただし **AI 利用を知らせると人間執筆より下に落ちる**
- Fundraising.AI 2025（寄付者 n=1,031）：AI 活用団体に「もっと寄付」14%、「減らす」32%
- Equilibrium 2025：高関与商品で罰則が大きい
- arXiv 2512.03373：AI 広告はブラインドだと選好率 59.1%（人間 40.9%）。**見抜かれると選好確率が 21.2pt 落ちる**

POOLO LIFE は 8 ヶ月・高額・人生の選択・情緒的・「主催者が自分に向けて書いた」ことが価値の一部。**罰則が最大化する象限にいる。**

## 3. 「実際の CVR が落ちる」——直接の証拠はない

自己申告の意向であって行動ではない、という限界がある。

- Adobe Express 2025（米 n=1,007）：46% が「AI 執筆と分かればメール配信停止しやすい」、18% は実際に疑って解除した
- Gartner 2025（米 n=1,539）：50% が「生成 AI を顧客向けに使わないブランド」を選ぶ
- Harris Poll×4As 2025：73% が AI 製と疑う広告を信頼しにくい、63% が AI 広告のブランドから買いにくい、78% が「使いすぎは cringe」
- Hootsuite Social Trends：62% が「AI 製と知ると関与・信頼が下がる」
- Bynder（英米 n=2,000）：開示前は 56% が AI 記事を好んだ。AI と知ると 52% が「関心が下がる」

一方で、**無開示の実 A/B テストでは AI 文が同等以上に勝つ例が普通にある**（Columbia の実地実験で売上最大 +16.3%、GetResponse のメール、電通デジタルの LP で 108〜110%）。Jakesch et al., PNAS 2023 が示す通り、一般読者は単文では 50〜52%（偶然と同じ）でしか見抜けない。

つまり **成約が落ちるのは「読み手が気づいたとき」だけ**。ここが効くレバー。

## 4. 日本の実証でいちばん CVR に近いもの

ビデオリサーチ ひと研究所 2025-12（15〜69 歳 n=2,593、画像広告）：

- **実写の広告でも最大 7 割が「AI 広告だ」と誤認した**
- 「AI 広告だ」と認識された広告は、実際の制作手段に関係なく購入・利用喚起スコアと好感度が低下
- 29.6% が「同じような広告ばかりになりそう」

ここから 2 つ言える。ひとつ、罰を受けるのは AI を使ったかどうかではなく**そう見えたかどうか**。ふたつ、**人間が書いた文も、整いすぎていれば同じ罰を受ける**。「人間が書いたから大丈夫」は成り立たない。

## 5. 実務的な結論

1. AI を使うかどうかではなく、**AI と読まれる文体を出さないこと**が変数。
2. 情緒的・対人的な部分（コンセプト、なぜこの場所か、主催者の言葉）ほど罰則が大きい。ここは人が書くか、人の材料で書く。
3. 事実（日時・料金・持ち物・FAQ）は罰則が小さい。ここに凝る必要はない。
4. 長い LP は見抜かれやすい。全部を均等に磨くより、**読み始めの数段落**（Hero、01 コンセプト、02 なぜこの場所）を優先する。
5. 開示するなら理由と出典を添える（Toff & Simon 2025：出典リストの提示で信頼低下を相殺できた）。

## 出典

- Rubin et al. 2025: https://www.nature.com/articles/s41562-025-02247-w
- Schilke & Reimann 2025: https://www.sciencedirect.com/science/article/pii/S0749597825000172
- Altay & Gilardi 2024: https://academic.oup.com/pnasnexus/article/3/10/pgae403/7795946
- Nakano et al. 2026: https://arxiv.org/abs/2510.24011
- Zhu et al. 2025: https://aclanthology.org/2025.findings-acl.1329/
- Baek, Kim & Kim 2024: https://www.tandfonline.com/doi/full/10.1080/02650487.2024.2401319
- Arango et al. 2023: https://www.tandfonline.com/doi/full/10.1080/00913367.2023.2183285
- Mansouri et al. 2025: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5399778
- 見抜かれると −21.2pt: https://arxiv.org/abs/2512.03373
- Jakesch et al. 2023: https://www.pnas.org/doi/10.1073/pnas.2208839120
- Toff & Simon 2025: https://journals.sagepub.com/doi/abs/10.1177/19401612241308697
- ビデオリサーチ ひと研究所 2025: https://www.videor.co.jp/digestplus/article/consumer260403.html
- JIAA ユーザー意識調査 2025: https://www.jiaa.org/news/release/20250807_user_chosa/ ／ 2026: https://www.jiaa.org/news/release/20260806_user_chosa/
- Gartner 2025: https://www.gartner.com/en/newsroom/press-releases/
- Harris Poll×4As 2025: https://theharrispoll.com/articles/inside-our-cannes-research-the-algorithmic-aisle-everyone-uses-ai-nobody-trusts-it-axios-100-the-ai-culture-wars/
- Bynder: https://www.bynder.com/en/press-media/ai-vs-human-made-content-study/
- Adobe Express 2025: https://www.adobe.com/express/learn/blog/ai-marketing-emails
- Fundraising.AI 2025: https://fundraising.ai/donor-perceptions-of-ai-2025/
- Columbia 実地実験: https://arxiv.org/abs/2510.12049 ／ 電通デジタル: https://www.dentsudigital.co.jp/knowledge-charge/articles/2025-1219-mugenai-lp
