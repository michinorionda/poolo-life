# English-language tells of LLM prose, and how to remove them

For English labels on LPs, English email, and any English copy. Sources in `sources.md`. Compiled from Wikipedia's "Signs of AI writing" (WikiProject AI Cleanup), corpus studies (Kobak 2025, Liang 2024, Reinhart/PNAS 2025, Sourati/NHB 2026, Kendro 2026, Freeburg 2026), the Economist's Aug 2026 analysis, Simon Willison's cliché highlighter (Jul 2026), and practitioner rule sets.

**The one finding everything agrees on:** vocabulary tells go stale within a model generation. "Delve" peaked Jan–Mar 2024 and fell once it was mocked. Structural and rhetorical tells persist because they come from the training objective, not from any word list. A paragraph with zero banned words can still hit every pattern below.

---

## A. Lexical

| Tell | Examples | Fix |
|---|---|---|
| 2023–24 "AI vocabulary" | delve, tapestry, testament, crucial, pivotal, intricate, landscape, realm, underscore, showcase, foster, leverage, robust, seamless, multifaceted, nuanced, vibrant, meticulous, commendable, interplay, garner, shed light on | Keep a ban list, but regenerate it from current model output every few months |
| Copula avoidance | serves as, stands as, boasts, features, represents | Write "is" and "has" |
| Latinate, nominalized diction | the implementation of; utilize; facilitate; commence | Anglo-Saxon monosyllables. Unpack nominalizations into verbs with named agents: "the compiler validates queries" |
| 2025–26 tics | genuinely, quietly, honestly, worth naming, that's not nothing, sit with that, turns out, the honest answer is | Delete. If the sentence survives, the word was filler |
| Synonym cycling | the city / the metropolis / the urban centre | Repeat the right word. Human text repeats more than LLM text does (Kendro 2026) |

## B. Syntactic and rhythmic

| Tell | Evidence | Fix |
|---|---|---|
| Uniform sentence length (low burstiness) | LLM polishing cuts complexity variance 21–50% (Sourati 2026) | Mix 3–8-word and 25+-word sentences. One one-sentence paragraph per piece |
| Em dashes where a comma or colon would do | GPT-4.1: 10.6 per 1,000 words vs human 3.2 (Freeburg 2026). By 2026 only Claude still exceeds human rates | Budget: at most 1 per 1,000 words. Restore commas, semicolons, parentheses |
| Present-participle tails | "…, highlighting the importance of X"; "…, reflecting broader trends" | Delete the tail or make it a sourced sentence |
| Bold-label bullets, title-case headings, colon into a triple | **Performance:** Performance improved… | Prose. Sentence-case headings. No bold except structural |
| Staccato fragments as a "fix" | Short. Punchy. Sentences. | This is itself a flagged pattern. Vary, don't chop |

## C. Structural

| Tell | Fix |
|---|---|
| Restating intro, "In this article we will explore", "Let's dive in" | Delete the intro. Lead with the news |
| Summarizing closer: "In conclusion", "Overall", "the future looks bright", "only time will tell" | End on the last concrete fact |
| Heading followed by a one-line restatement of the heading | Delete the restatement |
| Symmetrical sections; paragraphs reshuffleable without loss | Each paragraph must add one fact, claim, or turn, and must depend on the one before |
| Everything resolves neatly; no names, prices, dates | Inject specifics. Leave something unresolved if it is |
| "In today's fast-paced world" openers | Hard delete |

## D. Rhetorical

| Tell | Examples | Fix |
|---|---|---|
| Negative parallelism / false reframe | It's not X, it's Y. This isn't about X. It's about Y. Not only… but… No X, no Y, just Z | One per piece at most. Usually assert Y plainly. "It's not just… it's" in corporate filings went from ~50 (2023) to 208 (2025) |
| Rule of three | innovative, transformative, groundbreaking | Count the items. Write two or four when there are two or four |
| False ranges | from ancient traditions to modern innovations | Name the middle term or list the actual items |
| Stacked rhetorical questions, hypophora | The catch? … The solution? | One question, answered. The rest become statements |
| Stage-managed reveal | Here's the thing. Here's the kicker. Something shifted. Everything changed | Delete the hook, state the thing |
| Performative honesty | Let's be honest. I won't pretend. Honestly? Look, | Delete |
| Vague attribution | Experts argue, observers suggest, industry reports | Name the source or drop the claim |
| Significance inflation | stands as a testament, plays a pivotal role, indelible mark, enduring legacy | State what happened. Let the reader judge |
| Promotional register | nestled in, vibrant, breathtaking, rich cultural heritage | Concrete nouns |
| Platitudes true of every subject | Consistency is important. Building relationships takes time | Cut any sentence that is true of everything |

## E. Tonal

| Tell | Fix |
|---|---|
| Sycophantic openers: Great question! You're absolutely right. Certainly! | Delete. Anthropic's own system prompt bans flattery openers |
| Chatbot closers: I hope this helps! Let me know if… | Delete |
| Didactic hedging: It's important to note, it's worth noting, may vary, could potentially | At most one hedge per claim, only if the evidence supports it |
| Answering objections nobody raised: To be clear, I'm not saying… | Delete |
| Emoji in headers, `citeturn0search0`, `utm_source=chatgpt.com` | Delete |

## F. Process rules that practitioners report working

1. Name the clichés explicitly in the prompt, constructions included ("no 'it's not X, it's Y'", "no colon-into-three", "max one em dash").
2. Provide 2–3 samples of the target voice. The model will still compress variance, so re-edit for rhythm afterward.
3. Two passes: first remove patterns, then add voice (specifics, uneven rhythm, opinions, one unresolved thing). Never inject fake candor or manufactured stakes in pass two.
4. Fix structure before wording: outline, intros, symmetry, recaps, signposting first; word list last.
5. Read it aloud. "Don't let a sentence through unless it's the way you'd say it to a friend" (Paul Graham).
6. Flag when 3–4 signs co-occur, not on any single one.

## G. What detectors do, and how far to trust them

- GPTZero began with perplexity and burstiness, then moved to a trained classifier in 2023. Pangram and Originality.ai are fine-tuned transformers. Jabarian & Imas (NBER 2025) found Pangram near-zero error and robust to humanizers; open-source RoBERTa detectors flagged 30–69% of human text.
- Trained human readers remain the most robust detector: five heavy LLM users by majority vote misclassified 1 of 300 articles (Russell et al., ACL 2025). Their first cue was vocabulary, then formality, originality, clarity.
- Do not write to beat a detector. Write so a trained reader has nothing to point at.
