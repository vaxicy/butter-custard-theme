# -*- coding: utf-8 -*-
"""Butter Custard Theme - logo candidates drawn with PIL (code-first).

Outputs (relative paths, run from project root):
  store-assets/logo-candidates/<nn>-<slug>.png          128x128  (VS Code Marketplace icon size)
  store-assets/logo-candidates/master/<nn>-<slug>.png   512x512  (master)
  store-assets/logo-candidates/preview-sheet.png        all candidates + small sizes on light/dark

Concept 01 (caramel custard pudding) is the shipped icon - see generate_icon.py.
"""
import math
import os

from PIL import Image, ImageDraw, ImageFilter, ImageFont

S = 4
BASE = 128
N = BASE * S

OUT = "store-assets/logo-candidates"
MASTER = os.path.join(OUT, "master")

CUSTARD = (253, 232, 99, 255)
CUSTARD_L = (255, 246, 176, 255)
GOLD = (233, 198, 60, 255)
ACCENT = (194, 173, 41, 255)
DEEP = (60, 50, 11, 255)
COCOA = (110, 88, 26, 255)
CREAM = (255, 252, 228, 255)
EGGSHELL = (240, 231, 205, 255)
CARAMEL = (203, 126, 52, 255)
CARAMEL_L = (226, 156, 84, 255)
WAFER = (226, 176, 104, 255)
TOAST_IN = (246, 214, 156, 255)
SHINE = (255, 250, 205, 255)


# ---------------------------------------------------------------- helpers
def canvas():
    return Image.new("RGBA", (N, N), (0, 0, 0, 0))


def mk(painter):
    m = Image.new("L", (N, N), 0)
    painter(ImageDraw.Draw(m))
    return m


def dilate(m, w):
    """Grow a binary mask by ~w px (blur + calibrated threshold)."""
    if w <= 0:
        return m
    r = max(0.8, w * 0.5)
    b = m.filter(ImageFilter.GaussianBlur(r))
    t = 255.0 * 0.5 * math.erfc(w / (r * math.sqrt(2.0)))
    t = max(2, min(200, int(round(t))))
    return b.point(lambda p: 255 if p >= t else 0)


def paint(img, m, color):
    img.alpha_composite(
        Image.composite(Image.new("RGBA", (N, N), color), Image.new("RGBA", (N, N), (0, 0, 0, 0)), m)
    )


def part(img, painter, fill, outline=None, ow=0):
    """Draw a shape: outline = grown mask under the fill."""
    m = mk(painter)
    if outline is not None and ow:
        paint(img, dilate(m, ow), outline)
    paint(img, m, fill)
    return m


def rz(img, size):
    """Downscale RGBA keeping premultiplied alpha (no dark fringes)."""
    return img.convert("RGBa").resize((size, size), Image.LANCZOS).convert("RGBA")


def rrect(d, box, r, fill=255):
    d.rounded_rectangle(box, radius=r, fill=fill)


def ell(d, box, fill=255):
    d.ellipse(box, fill=fill)


def poly(d, pts, fill=255):
    d.polygon(pts, fill=fill)


def hatch(d, y0, y1, inset):
    """Wafer cone cross line at height y0..y1 (cone spans y 300..436)."""
    left = 246 - (436 - y0) * 0.357 + inset
    right = 266 + (436 - y0) * 0.357 - inset
    d.polygon([(left, y0), (right, y0), (right, y1), (left, y1)], fill=255)


# ---------------------------------------------------------------- concepts
def c1_pudding():
    """Caramel custard pudding."""
    img = canvas()

    def body(d):
        poly(d, [(180, 202), (332, 202), (404, 390), (108, 390)])
        rrect(d, [108, 338, 404, 428], 44)

    part(img, body, CUSTARD, DEEP, 13)
    part(img, lambda d: rrect(d, [162, 270, 186, 338], 12), CUSTARD_L)

    def cara(d):
        ell(d, [176, 140, 336, 234])
        poly(d, [(176, 186), (176, 236), (204, 236)])
        ell(d, [176, 210, 216, 250])
        poly(d, [(308, 186), (308, 220), (336, 220)])
        ell(d, [300, 198, 340, 238])

    part(img, cara, CARAMEL, DEEP, 10)
    part(img, lambda d: ell(d, [204, 164, 242, 188]), CARAMEL_L)
    return img


def c2_butter():
    """Butter block with melting drips."""
    img = canvas()

    def drip_main(d):
        poly(d, [(216, 320), (268, 320), (268, 394)])
        ell(d, [214, 366, 270, 422])

    def drip_side(d):
        poly(d, [(300, 320), (322, 320), (322, 364)])
        ell(d, [298, 350, 324, 376])

    part(img, drip_main, GOLD, DEEP, 11)
    part(img, drip_side, GOLD, DEEP, 9)
    part(img, lambda d: rrect(d, [116, 232, 396, 348], 26), GOLD, DEEP, 12)

    def top(d):
        poly(d, [(146, 178), (366, 178), (396, 246), (116, 246)])
        rrect(d, [146, 158, 366, 204], 22)

    part(img, top, CUSTARD_L, DEEP, 12)
    part(img, lambda d: rrect(d, [172, 172, 302, 194], 10), SHINE)
    return img


def c3_swirl():
    """Soft-serve custard swirl on a wafer cone."""
    img = canvas()
    part(img, lambda d: poly(d, [(196, 300), (316, 300), (266, 436), (246, 436)]), WAFER, DEEP, 12)
    part(img, lambda d: hatch(d, 332, 342, 8), CARAMEL)
    part(img, lambda d: hatch(d, 366, 375, 8), CARAMEL)
    part(img, lambda d: hatch(d, 398, 406, 10), CARAMEL)

    part(img, lambda d: ell(d, [146, 234, 366, 346]), CUSTARD, DEEP, 12)
    part(img, lambda d: ell(d, [164, 168, 348, 278]), CUSTARD, DEEP, 10)
    part(img, lambda d: ell(d, [190, 118, 322, 216]), CUSTARD, DEEP, 10)
    part(img, lambda d: ell(d, [226, 90, 286, 152]), CUSTARD, DEEP, 9)
    part(img, lambda d: ell(d, [214, 124, 258, 146]), CUSTARD_L)
    return img


def c4_whisk():
    """Whisk with a batter drop."""
    img = canvas()

    def dr(d):
        poly(d, [(356, 268), (392, 372), (320, 372)])
        ell(d, [318, 344, 394, 420])

    part(img, dr, CARAMEL, DEEP, 10)

    layer = canvas()
    part(layer, lambda d: rrect(d, [238, 84, 282, 238], 20), GOLD, DEEP, 11)
    part(layer, lambda d: rrect(d, [228, 228, 292, 268], 14), ACCENT, DEEP, 10)
    for box, ww in (
        ((196, 258, 320, 448), 11),
        ((226, 258, 290, 428), 10),
        ((250, 262, 266, 414), 9),
    ):
        part(layer, lambda d, b=box, w=ww: d.ellipse(b, outline=255, width=w), CUSTARD, DEEP, 6)
    img.alpha_composite(layer.rotate(-18, resample=Image.BICUBIC, center=(256, 256)))
    return img


def c5_egg():
    """Yolk sitting in a cracked shell."""
    img = canvas()
    part(img, lambda d: ell(d, [152, 146, 360, 354]), CUSTARD, DEEP, 12)
    part(img, lambda d: ell(d, [200, 188, 264, 224]), CUSTARD_L)

    def shell(d):
        d.pieslice([96, 124, 416, 444], start=0, end=180, fill=255)
        pts = []
        for i in range(9):
            x = 96 + (416 - 96) * i / 8.0
            pts.append((x, 256 if i % 2 == 0 else 292))
        poly(d, pts + [(416, 308), (96, 308)])

    part(img, shell, EGGSHELL, DEEP, 13)
    return img


def c6_ramekin():
    """Custard cup with a spoon."""
    img = canvas()

    def bowl(d):
        poly(d, [(150, 252), (362, 252), (324, 412), (188, 412)])
        rrect(d, [176, 384, 336, 430], 24)

    part(img, bowl, CREAM, DEEP, 12)
    for x in (208, 256, 304):
        part(img, lambda d, xx=x: rrect(d, [xx - 5, 302, xx + 5, 398], 5), ACCENT)
    part(img, lambda d: ell(d, [136, 204, 376, 288]), CUSTARD, DEEP, 12)

    spoon = canvas()
    part(spoon, lambda d: rrect(d, [242, 92, 268, 306], 13), GOLD, DEEP, 10)
    part(spoon, lambda d: ell(d, [206, 298, 302, 372]), GOLD, DEEP, 10)
    img.alpha_composite(spoon.rotate(-26, resample=Image.BICUBIC, center=(254, 300)))
    part(img, lambda d: ell(d, [176, 226, 258, 254]), CUSTARD_L)
    return img


def c7_toast():
    """Toast slice with butter square."""
    img = canvas()
    part(img, lambda d: rrect(d, [118, 148, 394, 432], 42), CARAMEL, DEEP, 14)
    part(img, lambda d: rrect(d, [146, 176, 366, 404], 30), TOAST_IN)

    b = canvas()
    part(b, lambda d: rrect(d, [198, 228, 318, 330], 18), CUSTARD, DEEP, 12)
    part(b, lambda d: ell(d, [216, 244, 268, 272]), CUSTARD_L)
    img.alpha_composite(b.rotate(9, resample=Image.BICUBIC, center=(258, 279)))

    def drip(d):
        poly(d, [(290, 300), (318, 300), (318, 352)])
        ell(d, [288, 336, 320, 368])

    part(img, drip, CUSTARD, DEEP, 10)
    return img


def c8_drop():
    """Abstract custard drop with a swirl."""
    img = canvas()

    def td(d):
        ell(d, [186, 236, 326, 376])
        poly(d, [(256, 112), (302, 302), (210, 302)])

    part(img, td, CUSTARD, DEEP, 13)
    for box, s, e, w in (
        ((230, 214, 324, 308), 195, 400, 14),
        ((242, 226, 312, 296), 20, 185, 13),
        ((252, 236, 302, 286), 195, 330, 12),
    ):
        part(img, lambda d, b=box, ss=s, ee=e, ww=w: d.arc(b, start=ss, end=ee, fill=255, width=ww), ACCENT)
    return img


CANDIDATES = [
    ("01-pudding", "Custard Pudding", "焦糖布丁", c1_pudding),
    ("02-butter", "Butter Block", "黄油方块", c2_butter),
    ("03-swirl", "Soft-Serve Swirl", "奶油旋风", c3_swirl),
    ("04-whisk", "Whisk & Batter", "打蛋器", c4_whisk),
    ("05-egg", "Egg & Shell", "蛋壳蛋黄", c5_egg),
    ("06-ramekin", "Custard Cup", "布丁陶杯", c6_ramekin),
    ("07-toast", "Toast & Butter", "吐司黄油", c7_toast),
    ("08-drop", "Swirl Drop", "抽象奶油滴", c8_drop),
]


# ---------------------------------------------------------------- preview sheet
def font(size, bold=False):
    cands = [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for c in cands:
        if os.path.exists(c):
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()


def font_zh(size):
    for c in ("C:/Windows/Fonts/msyh.ttc", "C:/Windows/Fonts/msyhbd.ttc", "C:/Windows/Fonts/simhei.ttf"):
        if os.path.exists(c):
            return ImageFont.truetype(c, size)
    return font(size)


def build_sheet(entries):
    W, H = 1400, 700
    LEFT, RIGHT = 40, W - 40
    sheet = Image.new("RGBA", (W, H), (255, 251, 235, 255))
    d = ImageDraw.Draw(sheet)

    d.text((LEFT, 24), "Butter Custard Theme  -  Logo Candidates", font=font(33, True), fill=DEEP)
    d.text((LEFT, 74), "VS Code theme icon proposals   |   黄油蛋奶主题 logo 方案", font=font_zh(18), fill=(150, 130, 70, 255))

    f_cap = font(17, True)
    f_lab = font(19, True)
    f_zh = font_zh(17)

    n = len(entries)
    gap = (RIGHT - LEFT - n * BASE) // (n - 1)
    assert gap >= 20, "icons too wide for sheet"
    xs = [LEFT + i * (BASE + gap) for i in range(n)]
    assert xs[-1] + BASE <= RIGHT, "right safety line violated"

    d.text((LEFT, 112), "128 px  (Marketplace icon size)", font=f_cap, fill=(120, 104, 52, 255))
    AY = 140
    for x, (slug, en, zh, im) in zip(xs, entries):
        sheet.alpha_composite(im, (x, AY))
        d.text((x, AY + BASE + 14), en, font=f_lab, fill=DEEP)
        d.text((x, AY + BASE + 40), zh, font=f_zh, fill=(150, 130, 70, 255))
    assert AY + BASE + 62 < 336

    d.text((LEFT, 336), "48 / 32 / 16 px  on light background", font=f_cap, fill=(120, 104, 52, 255))
    BY = 360
    for x, (slug, en, zh, im) in zip(xs, entries):
        d.rounded_rectangle([x, BY, x + BASE, BY + 84], radius=14, fill=(255, 255, 255, 255),
                            outline=(228, 216, 172, 255), width=2)
        sheet.alpha_composite(rz(im, 48), (x + 6, BY + 18))
        sheet.alpha_composite(rz(im, 32), (x + 64, BY + 26))
        sheet.alpha_composite(rz(im, 16), (x + 104, BY + 34))
    assert BY + 84 < 462

    d.text((LEFT, 462), "64 / 32 / 16 px  on dark background", font=f_cap, fill=(120, 104, 52, 255))
    CY = 486
    d.rounded_rectangle([LEFT, CY, RIGHT, CY + 150], radius=18, fill=DEEP)
    for x, (slug, en, zh, im) in zip(xs, entries):
        sheet.alpha_composite(rz(im, 64), (x + 8, CY + 20))
        sheet.alpha_composite(rz(im, 32), (x + 82, CY + 36))
        sheet.alpha_composite(rz(im, 16), (x + 122, CY + 44))
    assert CY + 150 < 652

    d.text((LEFT, 654), "Frameless glyphs (no outer plate). Pick a number, or ask for tweaks / a plate variant.",
           font=font(16), fill=(150, 130, 70, 255))
    assert CY + 150 + 20 < H
    return sheet


# ---------------------------------------------------------------- main
def main():
    os.makedirs(MASTER, exist_ok=True)
    entries = []
    for slug, en, zh, fn in CANDIDATES:
        master = fn()
        assert master.mode == "RGBA" and master.size == (N, N)
        master.save(os.path.join(MASTER, slug + ".png"))
        small = rz(master, BASE)
        small.save(os.path.join(OUT, slug + ".png"))
        entries.append((slug, en, zh, small))
        print("ok", slug, small.size, master.size)

    build_sheet(entries).save(os.path.join(OUT, "preview-sheet.png"))
    print("done ->", OUT)


if __name__ == "__main__":
    main()
