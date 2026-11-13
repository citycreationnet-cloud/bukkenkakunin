#!/usr/bin/env python3
"""index.html の site-data から、物件ごとのQRコード(SVG/PNG)を qr/ に生成する。

使い方:
  pip install segno
  python3 tools/make_qr.py https://公開ユーザー名.github.io/bukkenkakunin/
"""
import json, re, sys, pathlib
from urllib.parse import quote
import segno

root = pathlib.Path(__file__).resolve().parent.parent
if len(sys.argv) != 2 or not sys.argv[1].startswith("https://"):
    sys.exit("公開URL(https://...)を引数に指定してください。")
base = sys.argv[1].rstrip("/") + "/index.html"
html = (root / "index.html").read_text(encoding="utf-8")
m = re.search(r'<script id="site-data" type="application/json">(.*?)</script>', html, re.S)
props = json.loads(m.group(1)).get("properties", [])
if not props:
    sys.exit("site-data に物件が登録されていません。")
out = root / "qr"; out.mkdir(exist_ok=True)
for p in props:
    url = f"{base}?property={quote(p['id'])}"
    q = segno.make(url, error="m")  # 印刷向けに誤り訂正M
    q.save(out / f"{p['id']}.svg", scale=10, border=4)
    q.save(out / f"{p['id']}.png", scale=12, border=4)
    print(p["id"], url)
