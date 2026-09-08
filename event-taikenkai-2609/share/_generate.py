import os
TPL = '''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>{name}</title>
<meta name="robots" content="noindex,nofollow">
<link rel="stylesheet" href="../../poolo-ds/tokens.css">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ width:{W}px; height:{H}px; overflow:hidden; background:var(--bg); }}
  .art {{
    width:{W}px; height:{H}px;
    display:grid; grid-template-rows:{ph}px 1fr {bh}px;
    font-feature-settings:"palt" 1;
  }}
  .photo {{ background:url('{img}') center {focus} / cover no-repeat; }}
  .body {{
    background:var(--bg);
    display:flex; flex-direction:column; align-items:center; justify-content:center;
    gap:{gap}px; padding:0 {pad}px; text-align:center;
  }}
  .eyebrow {{
    font-family:var(--mincho); font-weight:600;
    font-size:{fs_eb}px; letter-spacing:.28em; text-indent:.28em;
    color:var(--ink-72); line-height:1.6;
  }}
  .title {{
    font-family:var(--mincho); font-weight:900;
    font-size:{fs_t}px; line-height:1.42; letter-spacing:.05em; color:var(--ink);
  }}
  .title em {{ font-style:normal; color:var(--brand); }}
  .title .num {{ font-size:1.32em; letter-spacing:-.02em; margin-inline:.05em; line-height:1; }}
  .band {{
    background:var(--brand); color:var(--on-brand);
    display:flex; align-items:center; justify-content:center; gap:{bgap}px;
  }}
  .band .m {{ font-family:var(--head); font-weight:700; font-size:{fs_b1}px; letter-spacing:.08em; }}
  .band .s {{ font-family:var(--body); font-weight:500; font-size:{fs_b2}px; letter-spacing:.06em; }}
</style>
</head>
<body>
<div class="art">
  <div class="photo"></div>
  <div class="body">
    <p class="eyebrow">{eyebrow}</p>
    <h1 class="title">{title}</h1>
  </div>
  <div class="band">
    <span class="m">{band1}</span>
    <span class="s">{band2}</span>
  </div>
</div>
</body>
</html>
'''

THEMES = {
  '30s': dict(
    img='../../event-30s-v01-260913/images/hero_30s.jpg',
    focus='30%',
    eyebrow='あたらしい旅の学校 POOLO の体験会',
    title='<span class="num">30</span>代の生き方を<br><em>問い直す</em><span class="num">90</span>分。',
  ),
  '20s': dict(
    img='../../event-20s-v01-260916/images/hero_20s.jpg',
    focus='center',
    eyebrow='20代後半の方へ｜あたらしい旅の学校 POOLO の体験会',
    title='働く意義・生きる意味を<br><em>見つけにいく</em><span class="num">90</span>分',
  ),
}
BAND1 = 'オンライン（Zoom）・参加無料・先着10名'
BAND2 = ''

# 判型ごとの寸法と級数
FORMATS = {
  '1200x630': dict(W=1200,H=630,  ph=300, bh=76,  pad=72,  gap=16, fs_eb=17, fs_t=44, fs_b1=24, fs_b2=17, bgap=22),
  '1080x1080':dict(W=1080,H=1080, ph=520, bh=120, pad=76,  gap=22, fs_eb=20, fs_t=58, fs_b1=30, fs_b2=21, bgap=26),
  '1080x1920':dict(W=1080,H=1920, ph=1040, bh=180, pad=80,  gap=30, fs_eb=24, fs_t=68, fs_b1=32, fs_b2=24, bgap=30),
}

out='event-taikenkai-2609/share'
os.makedirs(out, exist_ok=True)
for tk, t in THEMES.items():
    for fk, f in FORMATS.items():
        p=f'{out}/{tk}-{fk}.html'
        open(p,'w',encoding='utf-8').write(TPL.format(
            name=f'{tk} {fk}', img=t['img'], focus=t['focus'],
            eyebrow=t['eyebrow'], title=t['title'], band1=BAND1, band2=BAND2, **f))
        print('生成', p)
