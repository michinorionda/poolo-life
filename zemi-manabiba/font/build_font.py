#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
POOLO Zemi Toi  —  ディスプレイ数字書体

設計規則
  1. 閉じた形（0/6/8/9）には、天の右側に小さな開口をつくる（＝問いは閉じない）
  2. 縦は太く、横は細く（明朝の骨格）
  3. 直線の終端は進行方向へ斜めにカットする
  4. 数字は等幅（表・日付・価格で桁が揃う）
"""
import math
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.t2CharStringPen import T2CharStringPen

EM   = 1000
H    = 700          # 数字の高さ
W    = 560          # 送り幅（等幅）
SW   = 112          # 縦画の太さ
HW   = 52           # 横画の太さ
CX   = W / 2        # 字面の中心
RXO  = 224          # 円環の外側 X 半径
RYO  = H / 2        # 円環の外側 Y 半径
RXI  = RXO - SW     # 内側 X 半径
RYI  = RYO - HW     # 内側 Y 半径
CY   = H / 2
GAP  = 26           # 開口の角度（度）
GAPC = 78           # 開口の中心角（度）
K    = 0.5522847498 # 円のベジェ近似係数


def ell(cx, cy, rx, ry, deg):
    r = math.radians(deg)
    return (cx + rx * math.cos(r), cy + ry * math.sin(r))


def arc(pen, cx, cy, rx, ry, a1, a2, move=False):
    """楕円弧を90度以下に割って3次ベジェで描く。a1→a2（度）。"""
    if move:
        pen.moveTo(ell(cx, cy, rx, ry, a1))
    span = a2 - a1
    n = max(1, math.ceil(abs(span) / 90.0))
    step = span / n
    a = a1
    for _ in range(n):
        b = a + step
        ra, rb = math.radians(a), math.radians(b)
        k = K * (abs(math.radians(step)) / (math.pi / 2)) * (1 if step > 0 else -1)
        p0 = (cx + rx * math.cos(ra), cy + ry * math.sin(ra))
        p3 = (cx + rx * math.cos(rb), cy + ry * math.sin(rb))
        p1 = (p0[0] - k * rx * math.sin(ra), p0[1] + k * ry * math.cos(ra))
        p2 = (p3[0] + k * rx * math.sin(rb), p3[1] - k * ry * math.cos(rb))
        pen.curveTo(p1, p2, p3)
        a = b


def ring(pen, cx, cy, a1, a2, rxo=RXO, ryo=RYO, rxi=RXI, ryi=RYI):
    """開口のある円環（環帯扇形）。a1→a2 の範囲だけ肉をつける。"""
    arc(pen, cx, cy, rxi, ryi, a1, a2, move=True)
    pen.lineTo(ell(cx, cy, rxo, ryo, a2))
    arc(pen, cx, cy, rxo, ryo, a2, a1)
    pen.closePath()


def poly(pen, pts):
    """必ず反時計回りに正規化してから描く（重なりを塗り残さないため）。"""
    a = 0.0
    for i in range(len(pts)):
        x0, y0 = pts[i]
        x1, y1 = pts[(i + 1) % len(pts)]
        a += x0 * y1 - x1 * y0
    if a < 0:
        pts = pts[::-1]
    pen.moveTo(pts[0])
    for p in pts[1:]:
        pen.lineTo(p)
    pen.closePath()


def vbar(pen, x, y0, y1, w=SW, cut=0):
    """縦画。cut は上端を右へ倒す量（斜めカット）。"""
    poly(pen, [(x - w / 2, y0), (x + w / 2, y0),
               (x + w / 2 + cut, y1), (x - w / 2 + cut, y1)])


def hbar(pen, x0, x1, y, h=HW, cut=0):
    """横画。cut は右端を上へ持ち上げる量。"""
    poly(pen, [(x0, y - h / 2), (x1, y - h / 2 + cut),
               (x1, y + h / 2 + cut), (x0, y + h / 2)])


def diag(pen, p0, p1, w):
    """任意角度の直線。太さ w、端は線に直交。"""
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    L = math.hypot(dx, dy)
    nx, ny = -dy / L * w / 2, dx / L * w / 2
    poly(pen, [(p0[0] + nx, p0[1] + ny), (p1[0] + nx, p1[1] + ny),
               (p1[0] - nx, p1[1] - ny), (p0[0] - nx, p0[1] - ny)])


# ------------------------------------------------------------------ 字形

def g_zero(pen):
    # 天の右に開口。90-GAP から一周して 90 まで。
    ring(pen, CX, CY, GAPC - GAP / 2, GAPC - GAP / 2 - 360)


def g_one(pen):
    x = CX + 24
    vbar(pen, x, 0, H)
    # 左上の払い（縦画に深く食い込ませて一体に見せる）
    diag(pen, (x + 20, H - 30), (x - 188, H - 196), 74)
    # 足は控えめに
    hbar(pen, x - 160, x + 160, HW / 2)


def g_two(pen):
    # 上の弧
    ring(pen, CX, H - 200, 184, -34, RXO, 200, RXI, 200 - HW)
    # 斜めの下り（弧の終点から足まで、両端を重ねる）
    diag(pen, (CX + 214, H - 268), (CX - 150, 40), SW * 0.88)
    # 足
    hbar(pen, CX - 214, CX + 224, HW / 2, HW, 12)


def g_three(pen):
    ring(pen, CX, H - 176, 176, -104, RXO, 176, RXI, 176 - HW)
    ring(pen, CX, 176, 104, -186, RXO, 176, RXI, 176 - HW)


def g_four(pen):
    x = CX + 84
    vbar(pen, x, 0, H)
    diag(pen, (x - 8, H - 26), (CX - 208, 196), SW * 0.8)
    hbar(pen, CX - 236, CX + 214, 196)


def g_five(pen):
    # 天の横画
    hbar(pen, CX - 158, CX + 214, H - HW / 2, HW, 14)
    # 左の縦画（弧の始まりまで下ろす）
    vbar(pen, CX - 158, 300, H)
    # 下の弧。135度は縦画の芯の上に着地する。左上を開けたまま回す。
    ring(pen, CX, 200, 135, -170, RXO, 200, RXI, 200 - HW)


def g_six(pen):
    ring(pen, CX, 196, GAPC - GAP / 2, GAPC - GAP / 2 - 360, RXO, 196, RXI, 196 - HW)
    diag(pen, (CX + 140, H - 16), (CX - 196, 300), SW * 0.84)


def g_seven(pen):
    hbar(pen, CX - 214, CX + 224, H - HW / 2, HW)
    diag(pen, (CX + 190, H), (CX - 112, 0), SW * 0.88)


def g_eight(pen):
    ring(pen, CX, H - 194, GAPC - GAP / 2, GAPC - GAP / 2 - 360, 196, 194, 196 - SW, 194 - HW)
    ring(pen, CX, 194, 90, 90 - 360, RXO, 194, RXI, 194 - HW)


def g_nine(pen):
    ring(pen, CX, H - 196, GAPC - GAP / 2, GAPC - GAP / 2 - 360, RXO, 196, RXI, 196 - HW)
    diag(pen, (CX - 140, 16), (CX + 196, H - 300), SW * 0.84)


def g_period(pen):
    poly(pen, [(CX - 46, 0), (CX + 46, 0), (CX + 46, 92), (CX - 46, 92)])


def g_comma(pen):
    poly(pen, [(CX - 46, 0), (CX + 46, 0), (CX + 46, 92), (CX - 10, 92)])
    diag(pen, (CX + 14, 40), (CX - 40, -104), 52)


def g_colon(pen):
    for y in (96, H - 188):
        poly(pen, [(CX - 46, y), (CX + 46, y), (CX + 46, y + 92), (CX - 46, y + 92)])


def g_slash(pen):
    diag(pen, (CX - 176, -40), (CX + 176, H + 40), 58)


def g_hyphen(pen):
    hbar(pen, CX - 186, CX + 186, H / 2 - 20, HW, 12)


def g_yen(pen):
    diag(pen, (CX - 200, H), (CX, H - 320), SW * 0.72)
    diag(pen, (CX + 200, H), (CX, H - 320), SW * 0.72)
    vbar(pen, CX, 0, H - 300)
    hbar(pen, CX - 176, CX + 176, 250)
    hbar(pen, CX - 176, CX + 176, 140)


def g_percent(pen):
    ring(pen, CX - 128, H - 148, 90, 90 - 360, 116, 148, 116 - 62, 148 - 44)
    ring(pen, CX + 128, 148, 90, 90 - 360, 116, 148, 116 - 62, 148 - 44)
    diag(pen, (CX - 190, -30), (CX + 190, H + 30), 54)


def g_space(pen):
    pass


GLYPHS = [
    (".notdef", "g_notdef", None, W),
    ("space",   None,       0x0020, W),
    ("zero",    g_zero,     0x0030, W),
    ("one",     g_one,      0x0031, W),
    ("two",     g_two,      0x0032, W),
    ("three",   g_three,    0x0033, W),
    ("four",    g_four,     0x0034, W),
    ("five",    g_five,     0x0035, W),
    ("six",     g_six,      0x0036, W),
    ("seven",   g_seven,    0x0037, W),
    ("eight",   g_eight,    0x0038, W),
    ("nine",    g_nine,     0x0039, W),
    ("period",  g_period,   0x002E, 300),
    ("comma",   g_comma,    0x002C, 300),
    ("colon",   g_colon,    0x003A, 300),
    ("slash",   g_slash,    0x002F, 460),
    ("hyphen",  g_hyphen,   0x002D, 460),
    ("yen",     g_yen,      0x00A5, W),
    ("percent", g_percent,  0x0025, 700),
]


def build():
    order = [g[0] for g in GLYPHS]
    fb = FontBuilder(EM, isTTF=False)
    fb.setupGlyphOrder(order)
    fb.setupCharacterMap({g[2]: g[0] for g in GLYPHS if g[2]})

    charstrings, metrics = {}, {}
    for name, fn, _, adv in GLYPHS:
        # 記号は字面幅が狭いので中心をずらす
        shift = (adv - W) / 2
        pen = T2CharStringPen(adv, None)
        if callable(fn):
            class P:
                def moveTo(s, p): pen.moveTo((p[0] + shift, p[1]))
                def lineTo(s, p): pen.lineTo((p[0] + shift, p[1]))
                def curveTo(s, a, b, c): pen.curveTo(
                    (a[0] + shift, a[1]), (b[0] + shift, b[1]), (c[0] + shift, c[1]))
                def closePath(s): pen.closePath()
            fn(P())
        charstrings[name] = pen.getCharString()
        metrics[name] = (adv, 0)

    fb.setupCFF(
        "POOLOZemiToi-Display",
        {"FullName": "POOLO Zemi Toi Display",
         "FamilyName": "POOLO Zemi Toi",
         "Weight": "Regular"},
        charstrings, {})
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=800, descent=-200, lineGap=0)
    fb.setupNameTable({
        "familyName": "POOLO Zemi Toi",
        "styleName": "Display",
        "uniqueFontIdentifier": "POOLOZemiToi-Display 1.000",
        "fullName": "POOLO Zemi Toi Display",
        "psName": "POOLOZemiToi-Display",
        "version": "Version 1.000",
        "copyright": "POOLO / TABIPPO",
        "designer": "POOLO",
        "description": "閉じた形の天に開口をもつ、POOLOゼミのためのディスプレイ数字書体。",
    })
    fb.setupOS2(sTypoAscender=800, sTypoDescender=-200, usWinAscent=800,
                usWinDescent=200, sxHeight=H, sCapHeight=H,
                achVendID="POOL", fsType=0)
    fb.setupPost(isFixedPitch=0, underlinePosition=-120, underlineThickness=60)

    out = "/Users/michinorionda/poolo-life-git/zemi-manabiba/font/"
    import os
    os.makedirs(out, exist_ok=True)
    fb.save(out + "PooloZemiToi-Display.otf")

    fb.font.flavor = "woff2"
    fb.save(out + "PooloZemiToi-Display.woff2")
    print("書き出しました:", out)


if __name__ == "__main__":
    build()
