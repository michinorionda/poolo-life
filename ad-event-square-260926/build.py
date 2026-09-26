# 体験会スクエア広告 30案（1080×1080）を ads.html に書き出す。
# 使い方: python3 build.py [fontsource の node_modules/@fontsource へのパス]
#   引数なし → Google Fonts を読む（ブラウザで見る用）
#   引数あり → ローカルの fontsource を読む（ネットに出られない環境で画像に書き出す用）
import sys, json

R = "../"  # リポジトリ直下からの相対
P = {
  "face":   R+"event-taikenkai-2609/images/u20_a.jpg",
  "tall":   R+"event-30s-v03-260518/images/01_563.jpg",
  "side":   R+"event-20s-v2-261021/images/feel_railing.jpg",
  "man":    R+"event-u39-evergreen/images/hero-photo-01_252.jpg",
  "seasit": R+"teshima/images/sitting-sea.jpg",
  "cycle":  R+"teshima/images/cycling-solo.jpg",
  "chair":  R+"teshima/images/sea-chair.jpg",
  "wall":   R+"event-tomonoura/images/bohatei.jpg",
  "dusk":   R+"tomonoura/images/joyato-sunset.jpg",
  "night":  R+"tanbayama/images/night-talk.jpg",
  "wide":   R+"event-taikenkai-2609/images/c20_b.jpg",
  "pair":   R+"event-20s-kansai-260614/images/hero-photo-01_111.jpg",
}
LOGO = R+"event-30s-v2-261004/images/poolo_logo.png"

# 回の情報（30代 10/14）。差し替えはここだけ。
D = dict(m="10", d="14", md="10.14", slash="10/14", wj="水", we="WED",
         t="20:00–21:30", t0="20:00", age="30代")

def ph(k, pos="center"):
    return f'<div class="ph" style="background-image:url({P[k]});background-position:{pos}"></div>'

def logo(x="left:56px;top:52px", white=False):
    f = "filter:brightness(0) invert(1);" if white else ""
    return f'<img class="logo" src="{LOGO}" style="{x};{f}" alt="POOLO">'

def meta(color="#1E1E1E"):
    return f'<span style="color:{color}">参加無料・Zoom・90分</span>'

ADS = []
def ad(no, shelf, name, note, fit, html):
    ADS.append(dict(no=no, shelf=shelf, name=name, note=note, fit=fit, html=html))

# ───────── 棚1 写真＋日付帯（勝った型に日付を足す）
ad(1, "写真と日付帯", "顔の下に、ブルーの日付帯",
   "12期で勝った「1人が写る・文字が少ない」型に、日付帯だけを足した基準の案。まずこれと比べる。",
   "型どおり",
   ph("face", "50% 30%") + logo() +
   f'''<div style="position:absolute;left:0;right:0;bottom:0;height:250px;background:var(--brand);color:#fff;display:flex;align-items:center;padding:0 64px;gap:44px">
     <div class="en" style="font-size:128px;font-weight:500;line-height:1;letter-spacing:-.01em">{D["md"]}</div>
     <div style="font-size:34px;line-height:1.55;font-weight:500">
       <div class="en" style="font-size:40px;letter-spacing:.06em">{D["we"]} {D["t"]}</div>
       <div>{D["age"]}の無料体験会・Zoom</div></div></div>''')

ad(2, "写真と日付帯", "縦の日付帯を、左に立てる",
   "縦長の人物写真を右に寄せ、左の細い帯に日付を縦で置く。顔の面積を削らずに日付を入れられる。",
   "型どおり",
   f'<div class="ph" style="left:220px;background-image:url({P["tall"]});background-position:50% 35%"></div>' +
   f'''<div style="position:absolute;left:0;top:0;bottom:0;width:220px;background:var(--brand);color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px">
     <div class="en" style="font-size:40px;letter-spacing:.1em">{D["m"]}</div>
     <div style="width:60px;height:2px;background:#fff;opacity:.6"></div>
     <div class="en" style="font-size:120px;line-height:1;font-weight:500">{D["d"]}</div>
     <div style="font-size:34px;font-weight:700">（{D["wj"]}）</div>
     <div class="en" style="font-size:36px;margin-top:20px">{D["t0"]}〜</div>
     <div style="font-size:24px;margin-top:40px;writing-mode:vertical-rl;letter-spacing:.2em">{D["age"]}の体験会・無料</div></div>''' +
   logo("right:48px;bottom:48px", white=True))

ad(3, "写真と日付帯", "視線の先に、日付の札",
   "横を向いた人物の視線の先の空きに、白い札で日付を置く。目線が自然に日付へ流れる。",
   "型どおり",
   ph("side", "30% 50%") + logo("left:56px;top:52px") +
   f'''<div style="position:absolute;right:70px;top:170px;background:#fff;padding:40px 46px;border-top:8px solid var(--brand);box-shadow:none">
     <div style="font-size:26px;letter-spacing:.14em;color:var(--brand-deep);font-weight:700">{D["age"]}の体験会</div>
     <div class="en" style="font-size:112px;line-height:1.05;font-weight:500;margin-top:8px">{D["md"]}</div>
     <div class="en" style="font-size:36px;letter-spacing:.06em">{D["we"]} {D["t"]}</div>
     <div style="font-size:24px;margin-top:14px;color:#555">参加無料・Zoom</div></div>''')

ad(4, "写真と日付帯", "一行のコピー＋下に日時の二段",
   "写真に一行だけ明朝で重ね、日時は白地の下段にまとめる。コピーと情報の役割を上下で分ける。",
   "型どおり",
   f'<div class="ph" style="bottom:230px;background-image:url({P["man"]});background-position:60% 40%"></div>' +
   f'''<div class="min" style="position:absolute;left:64px;top:90px;font-size:62px;line-height:1.5;color:#1E1E1E">このままの延長で、<br>いいんだっけ。</div>''' +
   f'''<div style="position:absolute;left:0;right:0;bottom:0;height:230px;background:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 64px;border-top:8px solid var(--brand)">
     <div><div class="en" style="font-size:96px;line-height:1;font-weight:500;color:var(--brand-deep)">{D["md"]}<span style="font-size:40px;margin-left:16px">{D["we"]}</span></div>
     <div class="en" style="font-size:36px;margin-top:10px">{D["t"]}<span style="font-family:var(--sans);font-size:28px;margin-left:18px">{D["age"]}・無料・Zoom</span></div></div>
     <img src="{LOGO}" style="height:52px"></div>''')

ad(5, "写真と日付帯", "風景の中の小さな人＋角の日付ブロック",
   "人を小さく、空と海を広く。右上の四角いブロックにだけ情報を集める。静けさで止める型。",
   "型から少し外れる（人が小さい）",
   ph("seasit", "50% 50%") +
   f'''<div style="position:absolute;right:0;top:0;width:360px;height:360px;background:var(--brand);color:#fff;padding:48px 44px;box-sizing:border-box">
     <div style="font-size:26px;letter-spacing:.12em;font-weight:700">{D["age"]}の体験会</div>
     <div class="en" style="font-size:118px;line-height:1.05;font-weight:500;margin-top:14px">{D["md"]}</div>
     <div class="en" style="font-size:34px">{D["we"]} {D["t0"]}–</div>
     <div style="font-size:22px;margin-top:10px">参加無料・Zoom・90分</div></div>''' +
   '<div style="position:absolute;left:0;right:0;bottom:0;height:360px;background:linear-gradient(transparent,rgba(0,0,0,.45))"></div>' +
   f'''<div class="min" style="position:absolute;left:64px;bottom:80px;font-size:54px;color:#fff;line-height:1.55;text-shadow:0 0 24px rgba(0,0,0,.3)">30代の生き方を、<br>問い直す90分。</div>''')

ad(6, "写真と日付帯", "写真2/3、下1/3に明朝の日付",
   "下の白地に、日付を明朝で「十月十四日」と組む。数字より静かで、読まれる速さが落ちる。",
   "型どおり",
   f'<div class="ph" style="bottom:340px;background-image:url({P["chair"]});background-position:60% 50%"></div>' +
   f'''<div style="position:absolute;left:64px;right:64px;bottom:60px;height:240px;display:flex;justify-content:space-between;align-items:flex-end">
     <div><div class="min" style="font-size:78px;line-height:1.2">十月十四日<span style="font-size:44px">（水）</span></div>
     <div style="font-size:30px;margin-top:22px"><span class="en" style="font-size:36px">{D["t"]}</span>　{D["age"]}の体験会・無料・Zoom</div></div>
     <img src="{LOGO}" style="height:46px;margin-bottom:8px"></div>
     <div style="position:absolute;left:64px;right:64px;bottom:320px;height:2px;background:var(--brand)"></div>''')

# ───────── 棚2 数字が主役
ad(7, "数字が主役", "大きな「14」と、小さな顔の窓",
   "日付の数字を画面の半分に。人物は窓のように小さく切り取って添える。数字で予定に入れてもらう。",
   "型から外れる（顔が小さい）",
   f'''<div style="position:absolute;inset:0;background:var(--brand-pale)"></div>
   <div class="en" style="position:absolute;left:40px;top:60px;font-size:620px;line-height:.85;font-weight:500;color:var(--brand);letter-spacing:-.04em">14</div>
   <div style="position:absolute;right:64px;top:120px;width:330px;height:420px;background:url({P["face"]}) 50% 30%/cover"></div>
   <div style="position:absolute;left:64px;bottom:70px;right:64px;display:flex;justify-content:space-between;align-items:flex-end">
     <div><div class="en" style="font-size:44px;letter-spacing:.06em">OCT {D["we"]} {D["t"]}</div>
     <div class="min" style="font-size:48px;margin-top:14px">30代の生き方を問い直す、90分。</div>
     <div style="font-size:26px;margin-top:10px;color:#444">参加無料・Zoom・先着10名</div></div>
     <img src="{LOGO}" style="height:44px"></div>''')

ad(8, "数字が主役", "数字の中に、夕暮れの写真",
   "「10.14」の字形を写真で塗る。写真と日付が一体になる。白地が多く、フィードで浮く。",
   "型から外れる（人がいない）",
   f'''<div class="en" style="position:absolute;left:0;right:0;top:170px;text-align:center;font-size:360px;font-weight:600;line-height:1;letter-spacing:-.03em;background:url({P["dusk"]}) 50% 60%/cover;-webkit-background-clip:text;background-clip:text;color:transparent">{D["md"]}</div>
   <div class="en" style="position:absolute;left:0;right:0;top:560px;text-align:center;font-size:48px;letter-spacing:.2em;color:var(--brand-deep)">{D["we"]}  {D["t"]}</div>
   <div class="min" style="position:absolute;left:0;right:0;top:680px;text-align:center;font-size:56px">平日の夜、自分のことを話す90分。</div>
   <div style="position:absolute;left:0;right:0;top:790px;text-align:center;font-size:28px;color:#555">{D["age"]}の体験会｜参加無料・Zoom</div>''' +
   logo("left:50%;transform:translateX(-50%);bottom:70px"))

ad(9, "数字が主役", "「20:00」を主役に、夜の写真",
   "平日夜の開催を、時刻そのもので伝える。仕事終わりの人に「行ける時間だ」と先に分からせる。",
   "型から外れる（3人が写る）",
   ph("night", "50% 40%") + '<div style="position:absolute;inset:0;background:rgba(0,20,30,.45)"></div>' +
   f'''<div style="position:absolute;left:64px;top:90px;color:#fff">
     <div style="font-size:34px;letter-spacing:.14em">{D["slash"]}（{D["wj"]}）</div>
     <div class="en" style="font-size:300px;line-height:1;font-weight:500;letter-spacing:-.02em;margin-top:10px">{D["t0"]}</div>
     <div class="min" style="font-size:60px;margin-top:30px;line-height:1.5">仕事のあとに、<br>自分と話す90分。</div></div>
   <div style="position:absolute;left:64px;bottom:66px;color:#fff;font-size:28px">{D["age"]}の体験会｜参加無料・Zoom・〜21:30</div>''' +
   logo("right:56px;bottom:56px", white=True))

ad(10, "数字が主役", "「90」分を大きく",
   "所要時間を主役にする。夜の90分という「軽さ」で、参加のハードルを下げる。",
   "型から外れる（人がいない）",
   f'''<div style="position:absolute;inset:0;background:var(--brand)"></div>
   <div style="position:absolute;left:64px;top:80px;color:#fff;font-size:34px;letter-spacing:.14em;font-weight:700">{D["age"]}の無料体験会</div>
   <div class="en" style="position:absolute;left:50px;top:140px;color:#fff;font-size:520px;line-height:1;font-weight:500">90<span style="font-size:110px;margin-left:10px">min</span></div>
   <div class="min" style="position:absolute;left:64px;top:700px;color:#fff;font-size:56px;line-height:1.5">違和感を、自分のことばにする。</div>
   <div style="position:absolute;left:0;right:0;bottom:0;height:170px;background:#fff;display:flex;align-items:center;padding:0 64px;justify-content:space-between">
     <div class="en" style="font-size:60px;font-weight:500;color:var(--brand-deep)">{D["md"]} <span style="font-size:36px">{D["we"]} {D["t"]}</span></div>
     <img src="{LOGO}" style="height:44px"></div>''')

ad(11, "数字が主役", "「30代 × 10.14」を並べる",
   "対象と日付を同じ大きさで並べる。誰の、いつの会かが1秒で分かる。顔は右下に大きく。",
   "型どおり",
   f'''<div class="ph" style="left:440px;top:300px;background-image:url({P["man"]});background-position:62% 40%"></div>
   <div style="position:absolute;left:64px;top:80px">
     <div style="font-size:150px;font-weight:700;line-height:1.1">30<span style="font-size:110px">代</span></div>
     <div class="en" style="font-size:60px;color:var(--brand);margin:10px 0 0 8px">×</div>
     <div class="en" style="font-size:170px;font-weight:500;line-height:1;color:var(--brand-deep)">{D["md"]}</div>
     <div class="en" style="font-size:40px;letter-spacing:.06em;margin-top:18px">{D["we"]} {D["t"]}</div>
     <div style="font-size:28px;margin-top:40px;line-height:1.7;color:#333">生き方を問い直す90分<br>参加無料・Zoom</div></div>''' +
   logo("left:64px;bottom:60px"))

ad(12, "数字が主役", "漢字一字「水」",
   "曜日を一字だけ大きく。「水曜の夜」を予定の言葉として覚えてもらう。",
   "型から外れる（人が小さい）",
   f'''<div style="position:absolute;inset:0;background:#fff"></div>
   <div class="min" style="position:absolute;left:30px;top:10px;font-size:640px;line-height:1.2;color:var(--brand)">水</div>
   <div style="position:absolute;right:64px;top:90px;width:300px;height:380px;background:url({P["cycle"]}) 50% 60%/cover"></div>
   <div style="position:absolute;right:64px;top:500px;text-align:right">
     <div class="en" style="font-size:96px;font-weight:500;line-height:1">{D["md"]}</div>
     <div class="en" style="font-size:44px">{D["t"]}</div></div>
   <div class="min" style="position:absolute;left:64px;bottom:150px;font-size:54px">水曜の夜は、自分のことを話す日。</div>
   <div style="position:absolute;left:64px;bottom:80px;font-size:28px;color:#444">{D["age"]}の体験会｜参加無料・Zoom・90分</div>''' +
   logo("right:64px;bottom:72px"))

# ───────── 棚3 予定の形
cal = ""
days = [""]*4 + [str(i) for i in range(1, 32)]  # 2026/10/1 は木曜（日曜はじまり）
for i, dd in enumerate(days):
    on = dd == D["d"]
    st = "background:var(--brand);color:#fff;font-weight:600" if on else ""
    cal += f'<div style="height:92px;display:flex;align-items:center;justify-content:center;{st}">{dd}</div>'
ad(13, "予定の形", "10月のカレンダー、14日だけ塗る",
   "ひと月の中の1マスとして見せる。「この日なら空いている」と自分の予定と照らさせる。",
   "型から外れる（人がいない）",
   f'''<div style="position:absolute;left:64px;top:70px;display:flex;align-items:baseline;gap:24px">
     <div class="en" style="font-size:120px;font-weight:500;color:var(--brand-deep);line-height:1">10</div>
     <div class="en" style="font-size:36px;letter-spacing:.2em">OCTOBER 2026</div></div>
   <div class="en" style="position:absolute;left:64px;right:64px;top:240px;display:grid;grid-template-columns:repeat(7,1fr);font-size:40px;text-align:center;border-top:2px solid #1E1E1E">
     {''.join(f'<div style="height:64px;display:flex;align-items:center;justify-content:center;font-size:24px;letter-spacing:.1em;color:#777">{w}</div>' for w in ["SUN","MON","TUE","WED","THU","FRI","SAT"])}
     {cal}</div>
   <div style="position:absolute;left:64px;right:64px;bottom:60px;display:flex;justify-content:space-between;align-items:flex-end;border-top:1px solid #ddd;padding-top:26px">
     <div><div class="min" style="font-size:46px">14日（水）{D["t"]}</div>
     <div style="font-size:28px;margin-top:8px;color:#444">30代の生き方を問い直す、90分。無料・Zoom</div></div>
     <img src="{LOGO}" style="height:44px"></div>''')

ad(14, "予定の形", "日めくりの一枚",
   "紙の日めくりを写真の上に置く。「その日」の一枚だけ見せて、予定らしさを出す。",
   "型どおり",
   ph("wide", "40% 40%") +
   f'''<div style="position:absolute;right:80px;top:120px;width:340px;background:#fff;text-align:center;padding:0 0 36px">
     <div style="background:var(--brand);color:#fff;padding:18px 0;font-size:28px;letter-spacing:.2em" class="en">2026 · OCT</div>
     <div class="en" style="font-size:220px;line-height:1.05;font-weight:500;color:#1E1E1E;margin-top:14px">{D["d"]}</div>
     <div style="font-size:40px;font-weight:700">{D["wj"]}曜日</div>
     <div style="margin:22px 40px 0;border-top:1px dashed #bbb;padding-top:20px;font-size:26px;line-height:1.7"><span class="en" style="font-size:32px">{D["t"]}</span><br>{D["age"]}の体験会<br>無料・Zoom</div></div>''' +
   logo("left:56px;bottom:56px", white=True))

ad(15, "予定の形", "手帳の週間ページに、一行",
   "手帳の水曜の欄に「20:00 自分のことを話す」と書き込まれている絵。予定に入った後の姿を見せる。",
   "型から外れる（人がいない）",
   f'''<div style="position:absolute;inset:0;background:#F9F9F9"></div>
   <div style="position:absolute;left:64px;right:64px;top:70px;bottom:230px;background:#fff;border:1px solid #E4E4E4;display:grid;grid-template-rows:repeat(4,1fr)">
     {''.join(f'<div style="border-bottom:1px solid #E4E4E4;display:flex;padding:22px 30px;gap:30px;{"background:var(--brand-pale)" if dd=="14" else ""}"><div class="en" style="width:150px;font-size:{"52" if dd=="14" else "40"}px;color:{"var(--brand-deep)" if dd=="14" else "#aaa"}">{dd} <span style="font-size:24px">{w}</span></div><div style="font-size:34px;color:#1E1E1E;line-height:1.6">{t}</div></div>' for dd,w,t in [("12","MON",""),("13","TUE",""),("14","WED",'<span class="en" style="color:var(--brand-deep)">20:00–21:30</span><br><span class="min" style="font-size:46px">自分のことを話す。</span>'),("15","THU","")])}</div>
   <div style="position:absolute;left:64px;right:64px;bottom:60px;display:flex;justify-content:space-between;align-items:flex-end">
     <div><div class="min" style="font-size:44px">30代の生き方を問い直す、90分。</div>
     <div style="font-size:28px;margin-top:8px;color:#444">10/14（水）{D["t"]}・無料・Zoom</div></div>
     <img src="{LOGO}" style="height:44px"></div>''')

ad(16, "予定の形", "写真の上に、招待状のカード",
   "「30代のあなたへ」と宛名のある一枚の紙を写真に重ねる。広告より手紙に近い距離で案内する。",
   "型どおり",
   ph("pair", "40% 40%") + '<div style="position:absolute;inset:0;background:rgba(0,0,0,.12)"></div>' +
   f'''<div style="position:absolute;left:170px;right:170px;top:190px;bottom:190px;background:#fff;padding:60px 64px;box-sizing:border-box;text-align:center">
     <div style="font-size:26px;letter-spacing:.3em;color:var(--brand-deep)" class="en">INVITATION</div>
     <div class="min" style="font-size:40px;margin-top:34px">30代のあなたへ</div>
     <div style="font-size:28px;line-height:1.9;margin-top:24px;color:#333">誰にも言えていなかった違和感を、<br>同じ30代と話す90分です。</div>
     <div style="height:1px;background:#E4E4E4;margin:34px 0"></div>
     <div class="en" style="font-size:80px;font-weight:500;line-height:1;color:var(--brand-deep)">{D["md"]} <span style="font-size:36px">{D["we"]}</span></div>
     <div class="en" style="font-size:34px;margin-top:12px">{D["t"]}<span style="font-family:var(--sans);font-size:26px;margin-left:14px">無料・Zoom</span></div></div>''' +
   logo("left:50%;transform:translateX(-50%);bottom:70px", white=True))

ad(17, "予定の形", "チケットの半券",
   "切り取り線のある半券に、日時と「先着10名」を静かに書く。席があることを煽らずに伝える。",
   "型から外れる（人が小さい）",
   f'''<div style="position:absolute;inset:0;background:var(--brand-pale)"></div>
   <div style="position:absolute;left:90px;right:90px;top:250px;height:480px;background:#fff;display:flex">
     <div style="width:330px;background:url({P["man"]}) 62% 40%/cover"></div>
     <div style="flex:1;padding:50px 50px;position:relative">
       <div style="font-size:24px;letter-spacing:.2em;color:var(--brand-deep);font-weight:700">POOLO 体験会｜{D["age"]}</div>
       <div class="en" style="font-size:120px;font-weight:500;line-height:1.05;margin-top:12px">{D["md"]}</div>
       <div class="en" style="font-size:40px">{D["we"]} {D["t"]}</div>
       <div style="font-size:26px;margin-top:30px;line-height:1.8;color:#333">Zoom｜参加無料<br>先着10名</div>
       <div style="position:absolute;right:0;top:0;bottom:0;width:120px;border-left:3px dashed #C2DCE5;display:flex;align-items:center;justify-content:center"><div class="en" style="writing-mode:vertical-rl;font-size:26px;letter-spacing:.3em;color:var(--brand)">No.01–10</div></div></div></div>
   <div class="min" style="position:absolute;left:0;right:0;top:110px;text-align:center;font-size:52px">30代の生き方を問い直す、90分。</div>''' +
   logo("left:50%;transform:translateX(-50%);bottom:90px"))

ad(18, "予定の形", "カレンダーアプリの予定ブロック",
   "スマホのカレンダーに予定が入った画面の形。見慣れたUIで手を止め、日時をそのまま読ませる。",
   "型から外れる（人がいない）",
   f'''<div style="position:absolute;inset:0;background:#F9F9F9"></div>
   <div class="en" style="position:absolute;left:64px;top:70px;font-size:40px;letter-spacing:.06em;color:#777">WED, OCT 14</div>
   <div style="position:absolute;left:64px;right:64px;top:150px;bottom:250px">
     {''.join(f'<div style="height:100px;border-top:1px solid #E4E4E4;position:relative"><span class="en" style="position:absolute;left:0;top:-16px;font-size:26px;color:#999;background:#F9F9F9;padding-right:12px">{h}:00</span></div>' for h in range(17,24))}
     <div style="position:absolute;left:120px;right:0;top:300px;height:150px;background:var(--brand);color:#fff;padding:22px 30px;box-sizing:border-box;border-left:8px solid var(--brand-deep)">
       <div class="min" style="font-size:44px">自分のことを話す90分</div>
       <div class="en" style="font-size:30px;margin-top:6px">{D["t"]}  ·  Zoom</div></div></div>
   <div style="position:absolute;left:64px;right:64px;bottom:60px;display:flex;justify-content:space-between;align-items:flex-end">
     <div><div style="font-size:40px;font-weight:700">{D["age"]}の無料体験会</div>
     <div style="font-size:28px;margin-top:6px;color:#444">生き方を問い直す、90分。先着10名</div></div>
     <img src="{LOGO}" style="height:44px"></div>''')

# ───────── 棚4 問い＋日付
ad(19, "問いと日付", "明朝の問い一本、最下段に日時一行",
   "文字だけで止める。問いを大きく、日時は最下段に一行で。写真の無い回の予備にも。",
   "型から外れる（人がいない）",
   f'''<div style="position:absolute;inset:0;background:#fff"></div>
   <div class="min" style="position:absolute;left:0;right:0;top:330px;text-align:center;font-size:78px;line-height:1.7">仕事は頑張ってきた。<br>でも、このままの延長で<br>いいんだっけ。</div>
   <div style="position:absolute;left:64px;right:64px;bottom:60px;border-top:2px solid var(--brand);padding-top:30px;display:flex;justify-content:space-between;align-items:center">
     <div><span class="en" style="font-size:60px;font-weight:500;color:var(--brand-deep)">{D["md"]}</span><span class="en" style="font-size:34px;margin-left:14px">{D["we"]} {D["t"]}</span>
     <div style="font-size:26px;color:#444;margin-top:4px">{D["age"]}の体験会｜参加無料・Zoom</div></div>
     <img src="{LOGO}" style="height:44px"></div>''')

ad(20, "問いと日付", "ワークシートの問いと、書く欄",
   "当日のワークシートの問いを1問だけ見せる。「当日これをやる」が伝わり、日時も同じ紙に書く。",
   "型から外れる（人がいない）",
   f'''<div style="position:absolute;inset:0;background:var(--brand-pale)"></div>
   <div style="position:absolute;left:90px;right:90px;top:90px;bottom:230px;background:#fff;padding:70px 70px;box-sizing:border-box">
     <div style="font-size:24px;letter-spacing:.2em;color:var(--brand-deep);font-weight:700">当日のワークシートから　Q.03</div>
     <div class="min" style="font-size:52px;line-height:1.7;margin-top:30px">「これがあったから<br>続けられた」と感じた<br>場面はありますか？</div>
     {''.join('<div style="height:64px;border-bottom:1px solid #C2DCE5"></div>' for _ in range(3))}</div>
   <div style="position:absolute;left:90px;right:90px;bottom:60px;display:flex;justify-content:space-between;align-items:flex-end">
     <div><span class="en" style="font-size:64px;font-weight:500;color:var(--brand-deep)">{D["md"]}</span><span class="en" style="font-size:34px;margin-left:14px">{D["we"]} {D["t"]}</span>
     <div style="font-size:26px;color:#333;margin-top:4px">{D["age"]}の体験会｜参加無料・Zoom</div></div>
     <img src="{LOGO}" style="height:44px"></div>''')

ad(21, "問いと日付", "「わたしは、＿＿を問います。」",
   "90分の最後に書く一文を、空欄のまま見せる。空欄が「自分なら何と書くか」を考えさせる。",
   "型から外れる（人がいない）",
   f'''<div style="position:absolute;inset:0;background:#fff"></div>
   <div style="position:absolute;left:64px;top:80px;font-size:28px;letter-spacing:.14em;color:var(--brand-deep);font-weight:700">90分の最後に、この一文を書きます。</div>
   <div class="min" style="position:absolute;left:64px;right:64px;top:320px;font-size:84px;line-height:1.8">わたしは、<span style="display:inline-block;width:520px;border-bottom:4px solid var(--brand)"></span><br>を問います。</div>
   <div style="position:absolute;left:0;right:0;bottom:0;height:220px;background:var(--brand);color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 64px">
     <div><span class="en" style="font-size:88px;font-weight:500">{D["md"]}</span><span class="en" style="font-size:38px;margin-left:16px">{D["we"]} {D["t"]}</span>
     <div style="font-size:28px;margin-top:4px">{D["age"]}の体験会｜参加無料・Zoom</div></div>
     <img src="{LOGO}" style="height:46px;filter:brightness(0) invert(1)"></div>''')

ad(22, "問いと日付", "顔の横に、縦組みの問い",
   "人物を右、左に縦組みの問い。日付は下の帯。1人の表情と問いが同時に目に入る。",
   "型どおり",
   f'<div class="ph" style="left:380px;bottom:190px;background-image:url({P["face"]});background-position:45% 30%"></div>' +
   f'''<div class="min" style="position:absolute;left:70px;top:80px;height:720px;writing-mode:vertical-rl;font-size:66px;line-height:1.7;letter-spacing:.06em">このままの延長で、<br>いいんだっけ。</div>
   <div style="position:absolute;left:0;right:0;bottom:0;height:190px;background:var(--brand);color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 64px">
     <div><span class="en" style="font-size:80px;font-weight:500">{D["md"]}</span><span class="en" style="font-size:36px;margin-left:16px">{D["we"]} {D["t"]}</span></div>
     <div style="font-size:28px;text-align:right;line-height:1.6">{D["age"]}の体験会<br>無料・Zoom</div></div>''')

# ───────── 棚5 声と日付
ad(23, "声と日付", "参加者の声を、鉤括弧のまま大きく",
   "申し込んだときの気持ち（逐語）を大きく置き、属性と日付を添える。読み手が自分の声と重ねる。",
   "型から外れる（人がいない）",
   f'''<div style="position:absolute;inset:0;background:#fff"></div>
   <div class="min" style="position:absolute;left:0;top:40px;font-size:300px;color:var(--brand-pale);line-height:1">「</div>
   <div class="min" style="position:absolute;left:100px;right:90px;top:250px;font-size:58px;line-height:1.8">同期が次々と転職していき、<br>自分はこのままで<br>いいのか？と<br>もやもやしていました。</div>
   <div style="position:absolute;left:100px;top:760px;font-size:26px;color:#666">メーカー・企画職／30代・体験会参加者</div>
   <div style="position:absolute;left:64px;right:64px;bottom:60px;border-top:2px solid var(--brand);padding-top:26px;display:flex;justify-content:space-between;align-items:center">
     <div><span class="en" style="font-size:58px;font-weight:500;color:var(--brand-deep)">{D["md"]}</span><span class="en" style="font-size:32px;margin-left:12px">{D["we"]} {D["t"]}</span>
     <span style="font-size:26px;margin-left:18px">{D["age"]}の体験会・無料・Zoom</span></div>
     <img src="{LOGO}" style="height:40px"></div>''')

ad(24, "声と日付", "横顔の写真に、声を一行",
   "声を短く一行に切り出して写真に重ねる。23より文字が少なく、勝った型に近い。",
   "型どおり",
   ph("side", "90% 50%") +
   f'''<div class="min" style="position:absolute;right:48px;top:60px;width:560px;font-size:46px;white-space:nowrap;line-height:1.7;color:#1E1E1E;background:rgba(255,255,255,.88);padding:30px 36px;box-sizing:border-box">「自分はこのままで<br>いいのか？」<div style="font-family:var(--sans);font-weight:400;font-size:22px;color:#555;margin-top:10px;letter-spacing:0">30代・体験会参加者の申込時のことば</div></div>
   
   <div style="position:absolute;left:0;right:0;bottom:0;height:190px;background:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 64px;border-top:8px solid var(--brand)">
     <div><span class="en" style="font-size:80px;font-weight:500;color:var(--brand-deep)">{D["md"]}</span><span class="en" style="font-size:36px;margin-left:16px">{D["we"]} {D["t"]}</span>
     <div style="font-size:26px;color:#333">{D["age"]}の体験会｜参加無料・Zoom</div></div>
     <img src="{LOGO}" style="height:46px"></div>''')

# ───────── 棚6 中身と日付
ad(25, "中身と日付", "90分の流れを、時間の線で",
   "20:00から21:30までを一本の線にし、書く・話す・問いにするを並べる。何をする会かを先に見せる。",
   "型から外れる（文字が多い）",
   f'''<div style="position:absolute;inset:0;background:#fff"></div>
   <div style="position:absolute;left:64px;top:70px"><div class="min" style="font-size:56px">書いて、話して、問いにする。</div>
   <div style="font-size:28px;color:#444;margin-top:10px">{D["age"]}の体験会｜{D["slash"]}（{D["wj"]}）・無料・Zoom</div></div>
   <div style="position:absolute;left:130px;top:280px;bottom:230px;width:4px;background:var(--brand-mid)"></div>
   {''.join(f'<div style="position:absolute;left:112px;top:{y}px;display:flex;align-items:center;gap:40px"><div style="width:40px;height:40px;background:{c};"></div><div style="font-size:{fs}px;{w}">{t}</div></div>' for y,c,t,fs,w in [(270,"var(--brand-deep)",'<span class="en" style="font-size:52px">20:00</span>',40,""),(380,"var(--brand)","はじめに",40,"font-weight:700"),(470,"var(--brand)","書く",40,"font-weight:700"),(560,"var(--brand)","話す（3〜4人で）",40,"font-weight:700"),(650,"var(--brand)","問いにする",40,"font-weight:700"),(740,"var(--brand-deep)",'<span class="en" style="font-size:52px">21:30</span>　一文を書いて終わる',34,"")])}
   <div style="position:absolute;right:64px;top:300px;width:330px;height:460px;background:url({P["seasit"]}) 78% 50%/cover"></div>''' +
   logo("left:64px;bottom:66px") +
   f'<div class="en" style="position:absolute;right:64px;bottom:60px;font-size:70px;font-weight:500;color:var(--brand-deep)">{D["md"]}</div>')

ad(26, "中身と日付", "迷う理由を、3つの箱で先に消す",
   "無料・Zoom・悩みがなくてもいい。申し込む前の迷いに先に答える（くもんの先生の型）。",
   "型から外れる（文字が多い）",
   ph("man", "60% 30%") +
   f'''<div style="position:absolute;left:0;right:0;bottom:0;height:470px;background:#fff">
     <div style="display:flex;gap:18px;padding:40px 64px 0">
     {''.join(f'<div style="flex:1;border:2px solid var(--brand);padding:22px 10px;text-align:center"><div style="font-size:34px;font-weight:700;color:var(--brand-deep)">{a}</div><div style="font-size:22px;color:#444;margin-top:6px">{b}</div></div>' for a,b in [("参加無料","体験会のみでもOK"),("Zoomで90分","自宅から参加"),("悩みがなくても","そのまま来てください")])}</div>
     <div style="padding:30px 64px 0;display:flex;justify-content:space-between;align-items:flex-end">
     <div><div class="en" style="font-size:88px;font-weight:500;line-height:1;color:var(--brand-deep)">{D["md"]}<span style="font-size:38px;margin-left:14px">{D["we"]} {D["t"]}</span></div>
     <div style="font-size:30px;margin-top:14px">30代の生き方を問い直す体験会</div></div>
     <img src="{LOGO}" style="height:44px"></div></div>''')

ad(27, "中身と日付", "持ちもの「PCと、書けるもの。」",
   "持ちものを見出しにする。準備が軽いことと、書く会であることが同時に伝わる。",
   "型から外れる（人がいない）",
   f'<div class="ph" style="bottom:380px;background-image:url({R}event-higashikawa-winter-v2-261204/images/g_desk.jpg);background-position:50% 55%"></div>' +
   f'''<div style="position:absolute;left:64px;right:64px;bottom:60px;height:300px">
     <div style="font-size:26px;letter-spacing:.2em;color:var(--brand-deep);font-weight:700">持ちもの</div>
     <div class="min" style="font-size:72px;margin-top:6px">PCと、書けるもの。</div>
     <div style="display:flex;justify-content:space-between;align-items:flex-end;margin-top:30px">
     <div><span class="en" style="font-size:64px;font-weight:500;color:var(--brand-deep)">{D["md"]}</span><span class="en" style="font-size:34px;margin-left:14px">{D["we"]} {D["t"]}</span>
     <div style="font-size:26px;color:#333">{D["age"]}の体験会｜参加無料・Zoom</div></div>
     <img src="{LOGO}" style="height:44px"></div></div>''')

# ───────── 棚7 複数日程
ad(28, "日程を選ばせる", "10月の3回を並べる",
   "30代の10月の回を3つ並べ、都合のいい日を選ばせる。1回ずつの広告より、予定が合う人の母数が広がる。",
   "型から外れる（文字が多い）",
   f'<div class="ph" style="right:540px;background-image:url({P["tall"]});background-position:50% 30%"></div>' +
   f'''<div style="position:absolute;left:540px;right:0;top:0;bottom:0;background:#fff;padding:70px 56px;box-sizing:border-box">
     <div style="font-size:30px;font-weight:700;letter-spacing:.08em">{D["age"]}の体験会、10月は3回。</div>
     <div style="font-size:24px;color:#555;margin-top:6px">参加無料・Zoom・90分</div>
     {''.join(f'<div style="border-top:2px solid {"var(--brand)" if i==0 else "#E4E4E4"};padding:26px 0 22px;margin-top:{34 if i==0 else 0}px"><div class="en" style="font-size:84px;font-weight:500;line-height:1;color:var(--brand-deep)">{a}<span style="font-family:var(--sans);font-size:32px;font-weight:700;margin-left:10px;color:#1E1E1E">（{b}）</span></div><div class="en" style="font-size:34px;margin-top:8px">{c}</div></div>' for i,(a,b,c) in enumerate([("10.14","水","20:00–21:30"),("10.18","日","17:00–18:30"),("10.28","水","20:00–21:30")]))}
     <img src="{LOGO}" style="position:absolute;right:56px;bottom:56px;height:40px"></div>''')

ad(29, "日程を選ばせる", "年代で分けた2つの回",
   "20代後半（10/21）と30代（10/14）を左右に並べる。自分の年代の側を選ぶ動作で、自分ごとにさせる。",
   "型から外れる（2人・文字が多い）",
   f'''<div style="position:absolute;inset:0;display:grid;grid-template-columns:1fr 1fr">
   {''.join(f'<div style="position:relative;background:url({img}) {pos}/cover"><div style="position:absolute;left:0;right:0;bottom:0;height:340px;background:{bg};color:#fff;padding:40px 44px;box-sizing:border-box"><div style="font-size:40px;font-weight:700">{age}</div><div class="en" style="font-size:110px;font-weight:500;line-height:1.05;margin-top:6px">{md}</div><div class="en" style="font-size:32px">{t}</div></div></div>' for img,pos,bg,age,md,t in [(P["tall"],"50% 25%","var(--brand-deep)","30代","10.14","WED 20:00–21:30"),(P["man"],"62% 40%","var(--brand)","20代後半","10.21","WED 20:00–21:30")])}</div>
   <div style="position:absolute;left:0;right:0;top:0;height:150px;background:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 56px">
     <div class="min" style="font-size:46px">あなたの年代の回へ。</div>
     <div style="font-size:24px;text-align:right;color:#444">参加無料・Zoom・90分<br><img src="{LOGO}" style="height:34px;margin-top:6px"></div></div>''')

ad(30, "日程を選ばせる", "最小限：写真と、日時の一行だけ",
   "情報を一行に削り切った対照群。勝った型をいちばん素直に守ると、どこまで減らせるかの基準。",
   "型どおり（いちばん文字が少ない）",
   ph("face", "50% 30%") +
   f'''<div style="position:absolute;left:56px;bottom:56px;background:#fff;padding:18px 28px;display:flex;align-items:baseline;gap:18px">
     <span class="en" style="font-size:52px;font-weight:500;color:var(--brand-deep)">{D["md"]}</span>
     <span class="en" style="font-size:30px">{D["we"]} {D["t0"]}</span>
     <span style="font-size:28px;font-weight:700">{D["age"]}・無料・Zoom</span></div>''' +
   logo("right:56px;top:52px"))


def css(fontsrc):
    if fontsrc:
        links = "".join(f'<link rel="stylesheet" href="{fontsrc}/{p}">' for p in
            ["zen-old-mincho/700.css", "noto-sans-jp/400.css", "noto-sans-jp/500.css", "noto-sans-jp/700.css",
             "jost/400.css", "jost/500.css", "jost/600.css"])
        mincho, sans = "'Zen Old Mincho'", "'Noto Sans JP'"
    else:
        links = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Zen+Old+Mincho:wght@700&family=Noto+Sans+JP:wght@400;500;700&family=Jost:wght@400;500;600&display=swap">'
        mincho, sans = "'Zen Old Mincho'", "'Noto Sans JP'"
    return links + f'''<style>
:root{{--brand:#189BBC;--brand-deep:#127E9A;--brand-mid:#8FC6D6;--brand-pale:#DDECF1;--mincho:{mincho},serif;--sans:{sans},sans-serif}}
body{{margin:0;background:#ddd;display:flex;flex-wrap:wrap;gap:40px;padding:40px}}
.ad{{width:1080px;height:1080px;position:relative;overflow:hidden;background:#fff;color:#1E1E1E;font-family:var(--sans);font-feature-settings:"palt";line-height:1.4}}
.ph{{position:absolute;inset:0;background-size:cover;background-repeat:no-repeat}}
.logo{{position:absolute;height:46px}}
.min{{font-family:var(--mincho);font-weight:700;letter-spacing:.02em}}
.en{{font-family:'Jost',var(--sans);font-variant-numeric:tabular-nums}}
</style>'''


if __name__ == "__main__":
    fontsrc = sys.argv[1] if len(sys.argv) > 1 else None
    body = "".join(f'<div class="ad" id="a{a["no"]:02d}">{a["html"]}</div>' for a in ADS)
    open("ads.html", "w").write(f'<!doctype html><meta charset="utf-8"><title>体験会スクエア広告30案（書き出し用）</title>{css(fontsrc)}{body}')
    json.dump([{k: a[k] for k in ("no", "shelf", "name", "note", "fit")} for a in ADS],
              open("ads.json", "w"), ensure_ascii=False, indent=1)
    print(len(ADS), "ads")
