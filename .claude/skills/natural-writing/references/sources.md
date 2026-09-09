# 出典（2026-09-02 調査）

取得できなかったページ（note / Zenn / Qiita / Wikipedia 本体など）は、検索スニペットと GitHub 上の引用から内容を確認した。

## 日本語圏

- coji「natural-japanese」（7 モデル×406 本の実測、文長変動係数、対比型の人間 1.5% vs AI 8.3%）: https://zenn.dev/coji/articles/natural-japanese-ai-smell-lint ／ https://github.com/coji/natural-japanese
- nakashimatakaya「deslop-ja」（語彙 300 項目、3 層モデル）: https://github.com/nakashimatakaya/deslop-ja
- textlint-ja「textlint-rule-preset-ai-writing」（太字コロン・絵文字・hype・述語コロン）: https://github.com/textlint-ja/textlint-rule-preset-ai-writing
- gonta223「humanizer-ja」（20 パターン）: https://github.com/gonta223/humanizer-ja ／ Ran350「humanizer-ja」（18 パターン＋告知文例）: https://github.com/Ran350/humanizer-ja
- iKora128「stop-ai-slop-jp」（書き手の不在、偏愛語、5 軸採点）: https://github.com/iKora128/stop-ai-slop-jp ／ だいち「その文章、AI に書かせただろ」: https://note.com/ikora/n/n0bbb2828b91e
- コミットメントの不在: https://zenn.dev/acntechjp/articles/c0591c4a642502
- もとやま「AI っぽい表現大全」（6 分類）: https://note.com/yusuke_motoyama/n/n2a1218636f56 ／ munyoru 15 選: https://note.com/munyoru/n/nd524ff97457f
- LP・コピー危険語と競合置き換えテスト: https://github.com/s-tsuchiya-source/LP_Creator_Team ／ UX ライティングのクリシェ辞書: https://github.com/BoxPistols/ux-writing-dead-cliche
- 技術記事チェックリスト・体験捏造禁止: https://github.com/yukikotani231/zenn-content/blob/main/docs/anti-ai-writing-checklist.md
- 教科書テスト・変動係数 0.40・敬体常体混在: https://github.com/syuya2036/skills
- 「効く」・キメ文・許可型言い回し: https://github.com/minorun365/my-claude-code-settings
- 1/5 圧縮＋具体例: https://blog.tinect.jp/?p=82102 ／ 1 文段落: https://tenbin.ai/media/generative_ai/ai-writing-remove-ai-slop
- カスタムインストラクション: https://note.com/tasty_dunlin998/n/n6b459279a5d5 ／ 固有名詞ひとつ・失敗談: https://note.com/y__u777/n/nc77fc540d7b0
- X の観察（「これ、」「正直、」「」多用・誤字なし）: https://togetter.com/li/2643830 ／ https://x.com/Mcyn301/status/1996730431035850797
- Forbes JAPAN 15 サイン: https://forbesjapan.com/articles/detail/91599
- 検出器: https://www.luft.co.jp/cgi/ai-ja-text-check.php ／ GPTZero 日本語精度 60〜70%: https://uomi-ai-lab.boy.jp/2026/07/13/gptzero-japanese-ai-checker-guide/
- 古賀史健×田中泰延: https://diamond.jp/articles/-/331527 ／ 谷崎『文章読本』: https://tinect.jp/blog/contents-learning-from-junichiro-tanizaki/ ／ 本多勝一の読点: https://www.math.nagoya-u.ac.jp/~shinichiroh/2018/02/13/japanese-punctuation.html ／ 糸井重里×東浩紀: https://www.1101.com/n/s/hiroki_azuma/2025-06-22.html

## 英語圏

- Wikipedia「Signs of AI writing」（WikiProject AI Cleanup）: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing ／ 読んだミラー: https://raw.githubusercontent.com/softaworks/agent-toolkit/main/skills/writing-clearly-and-concisely/signs-of-ai-writing.md
- Kobak et al. 2025, Science Advances（PubMed 抄録、delve 25 倍、2024 年の 13.5% 以上が LLM 処理）: https://www.science.org/doi/10.1126/sciadv.adt3813 ／ https://arxiv.org/abs/2406.07016 ／ データ: https://github.com/berenslab/llm-excess-vocab
- Liang et al. 2024（ICLR 査読、commendable 9.8 倍、meticulous 34.7 倍）: https://arxiv.org/abs/2403.07183
- Reinhart et al. 2025, PNAS（名詞化 1.5〜2 倍、分詞節 2〜5 倍、tapestry 150 倍）: https://www.pnas.org/doi/10.1073/pnas.2422455122
- Russell, Karpinska, Iyyer 2025, ACL（人間の熟練読者は 300 本中 1 本しか誤判定しない）: https://aclanthology.org/2025.acl-long.267/
- Sourati et al. 2026, Nature Human Behaviour（LLM 推敲で分散 21〜50% 減）: https://www.nature.com/articles/s41562-026-02550-0
- Kendro 2026, IJAL（反復の分散 人間 16.4 vs ChatGPT 4.8〜5.8）: https://onlinelibrary.wiley.com/doi/10.1111/ijal.70115
- Freeburg 2026「The Last Fingerprint」（em dash 10.6 vs 3.2 /1000 語、markdown の漏出）: https://arxiv.org/abs/2603.27006
- The Economist, Aug 2026（55,940 文の比較、ラテン語系・名詞化・文長の均一）: https://theeconomistoffthecharts.substack.com/p/how-to-spot-ai-writing
- Simon Willison, LLM cliché highlighter（38 パターン、2026-07）: https://simonwillison.net/2026/Jul/17/llm-cliche-highlighter/
- Barron's / TechCrunch（「It's not just… it's」が決算資料で 50→208 件）: https://techcrunch.com/2026/04/20/ai-writing-its-not-just-this-its-that-barrons/
- OpenAI の em dash 修正（2025-11）: https://techcrunch.com/2025/11/14/openai-says-its-fixed-chatgpts-em-dash-problem/
- StationX 2026（語彙ゼロでもパターンで AI と分かる）: https://app.stationx.net/articles/ai-writing-patterns
- Colin Gorrie（修辞の飽和＝slop）: https://www.deadlanguagesociety.com/p/rhetorical-analysis-ai ／ Charlie Guo「Field Guide to AI Slop」: https://www.ignorance.ai/p/the-field-guide-to-ai-slop ／ Louis Bouchard（構造から直す）: https://www.louisbouchard.ai/ai-editing/
- Paul Graham「Write Like You Talk」: https://paulgraham.com/talk.html ／「Writes and Write-Nots」: https://paulgraham.com/writes.html
- ルールセット: https://github.com/blader/humanizer ／ https://github.com/conorbronsdon/avoid-ai-writing ／ https://raw.githubusercontent.com/cursor/plugins/main/pstack/skills/unslop/SKILL.md ／ https://github.com/gabelul/slopbuster
- 検出器の信頼性: Jabarian & Imas 2025, NBER w34223: https://www.nber.org/papers/w34223 ／ Pangram: https://arxiv.org/abs/2402.14873 ／ Weber-Wulff et al. 2023: https://edintegrity.biomedcentral.com/articles/10.1007/s40979-023-00146-z ／ GPTZero の perplexity/burstiness: https://gptzero.me/news/perplexity-and-burstiness-what-is-it/
- 追従性（sycophancy）: Claude 4 system prompt の分析: https://www.prompthub.us/blog/an-analysis-of-the-claude-4-system-prompt ／ OpenAI GPT-4o rollback: https://openai.com/index/sycophancy-in-gpt-4o/
- 「delve」の起源仮説（Juzek & Ward, COLING 2025）: https://aclanthology.org/2025.coling-main.426/ ／ 人間の話し言葉への漏出（Yakura et al.）: https://arxiv.org/abs/2409.01754
