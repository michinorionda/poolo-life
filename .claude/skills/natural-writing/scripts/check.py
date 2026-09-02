#!/usr/bin/env python3
"""AI っぽさの機械チェック（日本語テキスト向け）。

使い方:
    python3 check.py <file.html|file.md|file.txt> [...]
    cat text.txt | python3 check.py -

HTML は本文テキストだけを抜き出して判定する。判定は目安であって合否ではない。
数値は「密度」と「併発」で見る。ひとつ引っかかっただけで直すのは早い。
"""
import html
import re
import statistics
import sys

# ---- 兆候リスト（references/catalog-ja.md と対応） ---------------------------
PATTERNS = {
    "接続詞・つなぎ（AI が文を接着する語）": [
        "これにより", "一方で", "さらに、", "加えて、", "また、", "だからこそ", "つまり",
        "そのため、", "したがって", "〜を通じて", "を通じて", "において", "といった",
    ],
    "文末ヘッジ（断定を避けて濁す）": [
        "と言えるでしょう", "といえるでしょう", "ではないでしょうか", "と考えられます",
        "と言われています", "とされています", "かもしれません", "と言っても過言では",
    ],
    "定型の導入・締め": [
        "近年", "昨今", "本記事では", "いかがでしたか", "ぜひ", "してみてください",
        "注目を集め", "注目が集ま", "まとめると", "結論から言うと", "ご存知でしょうか",
        "想像してみてください",
    ],
    "評価語・意義づけ（事実の後ろに勝手に付く）": [
        "重要", "不可欠", "鍵とな", "画期的", "革新的", "多面的", "包括的", "本質的",
        "貴重な", "大きな意味", "示唆", "浮き彫り", "物語って",
    ],
    "コピーの常套句（誰の告知にも貼れる語）": [
        "唯一無二", "かけがえのない", "心に響く", "寄り添", "伴走", "実現し", "提供し",
        "活用", "最適", "シームレス", "新しい自分", "一歩踏み出", "仲間と共に", "仲間とともに",
        "特別な体験", "体験をお届け", "応援します", "解像度", "本質", "熱量", "営み",
        "紡", "彩", "切り拓", "化学反応", "絶景", "満喫", "人生が変わる", "市場価値",
    ],
    "対比の型（Aではなく B）": [
        "ではなく", "ではありません。", "だけではありません", "それだけでなく", "ではない。",
    ],
    "煽り・記号": [
        "！", "!!", "今すぐ", "残りわずか", "限定", "——", "―", "**", "✨", "🔥", "👉", "✅",
    ],
}

JP_SENT_END = re.compile(r"(?<=[。！？!?])\s*")
VERB_ENDINGS = (
    "です", "ます", "でした", "ました", "ません", "ない", "た", "る", "い", "う", "く",
    "ね", "よ", "か", "だ", "ん", "から", "けど", "が", "し", "て", "で",
)


def strip_html(src: str) -> str:
    src = re.sub(r"(?is)<(script|style|noscript)\b.*?</\1>", " ", src)
    src = re.sub(r"(?i)<br\s*/?>", "\n", src)
    src = re.sub(r"(?i)</(p|div|li|h[1-6]|section|article|blockquote|dd|dt|tr)>", "\n", src)
    src = re.sub(r"<[^>]+>", "", src)
    src = html.unescape(src)
    src = re.sub(r"[ \t　]+", " ", src)
    return src


def sentences(text: str):
    out = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        for s in JP_SENT_END.split(line):
            s = s.strip()
            # 日本語を含む文だけ数える（CSS 残骸や英字ラベルを除く）
            if len(s) >= 2 and re.search(r"[ぁ-んァ-ン一-龥]", s):
                out.append(s)
    return out


def is_taigen(s: str) -> bool:
    core = s.rstrip("。！？!?」』）)").rstrip()
    if not core:
        return False
    return not core.endswith(VERB_ENDINGS)


def analyse(name: str, text: str) -> None:
    sents = sentences(text)
    body = "".join(sents)
    n_chars = max(len(body), 1)
    per1k = lambda c: c * 1000 / n_chars  # noqa: E731

    print(f"\n=== {name} ===")
    print(f"文字数 {n_chars}  文数 {len(sents)}")
    if len(sents) >= 3:
        lens = [len(s) for s in sents]
        mean = statistics.mean(lens)
        cv = statistics.pstdev(lens) / mean if mean else 0
        short = sum(1 for l in lens if l <= 6)
        longs = sum(1 for l in lens if l >= 60)
        print(f"一文の長さ 平均 {mean:.1f} 字  変動係数 {cv:.2f}  6字以下 {short}  60字以上 {longs}")
        print("  → 変動係数 0.40 未満は「均一すぎ」の目安。短文だけで刻むのも、長文だけで押すのも AI 的。")
    taigen = sum(1 for s in sents if is_taigen(s))
    print(f"体言止め {taigen}/{len(sents)} ({taigen*100//max(len(sents),1)}%)  → 0% も 50% 超も不自然")
    digits = len(re.findall(r"\d+", body))
    quoted = len(re.findall(r"「[^」]{1,12}」", body))
    print(f"数字 {digits} 個（/1000字 {per1k(digits):.1f}）  「」で立てた語 {quoted} 個（/1000字 {per1k(quoted):.1f}）")
    print("  → 数字・固有名詞・場面が薄いと抽象語だけの文になる。")

    total_hits = 0
    for group, words in PATTERNS.items():
        hits = []
        for w in words:
            c = body.count(w)
            if c:
                hits.append((w, c))
        cnt = sum(c for _, c in hits)
        total_hits += cnt
        if hits:
            hits.sort(key=lambda x: -x[1])
            shown = "、".join(f"{w}×{c}" for w, c in hits[:8])
            print(f"[{group}] {cnt} 件 (/1000字 {per1k(cnt):.1f}): {shown}")
    dewa = body.count("ではなく") + body.count("ではありません。")
    print(f"「Aではなく B」型 {dewa} 件 / {len(sents)} 文 = {dewa*100/max(len(sents),1):.1f}%  → 人間の中央値 1.5%、AI は 8%台")
    print(f"兆候の合計密度 /1000字 {per1k(total_hits):.1f}")

    print("--- 引っかかった文（最大 12 件）---")
    shown = 0
    for s in sents:
        matched = [w for ws in PATTERNS.values() for w in ws if w in s]
        if matched and shown < 12:
            print(f"  ・{s[:70]}{'…' if len(s) > 70 else ''}   ← {', '.join(matched[:4])}")
            shown += 1


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    for path in argv[1:]:
        if path == "-":
            raw = sys.stdin.read()
            name = "stdin"
        else:
            with open(path, encoding="utf-8") as f:
                raw = f.read()
            name = path
        text = strip_html(raw) if re.search(r"<\w+[^>]*>", raw) else raw
        analyse(name, text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
