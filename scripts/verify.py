"""用 YouTube oEmbed 驗證每個連結仍存在，並回填真實標題與頻道。
用法：python3 scripts/verify.py   → 產生 data.js（失效的標 dead，不上架）"""
import json, sys, time, urllib.request, urllib.parse
sys.path.insert(0, __import__('os').path.dirname(__file__))
from seed import S
INST = {"flute":"長笛","clarinet":"單簧管","horn":"法國號"}
def url(kind, i):
    return (f"https://www.youtube.com/playlist?list={i}" if kind=="playlist"
            else f"https://www.youtube.com/watch?v={i}")
out, dead = [], []
for inst, lang, kind, i, note in S:
    u = url(kind, i)
    q = "https://www.youtube.com/oembed?format=json&url=" + urllib.parse.quote(u, safe="")
    try:
        d = json.load(urllib.request.urlopen(q, timeout=20))
        out.append(dict(id=i, instrument=inst, lang=lang, kind=kind, url=u,
                        title=d["title"], channel=d["author_name"], note=note))
    except Exception as e:
        dead.append((u, str(e)))
    time.sleep(0.2)
js = "window.RESOURCES = " + json.dumps(out, ensure_ascii=False, indent=1) + ";\n"
open("data.js", "w", encoding="utf-8").write(js)
print(f"ok {len(out)} / dead {len(dead)}")
for u, e in dead: print("DEAD", u, e)
sys.exit(1 if dead else 0)
