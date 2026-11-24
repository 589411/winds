# STATUS — winds

**最後更新：** 2026-11-24
**線上：** https://winds.launchdock.app（GitHub Pages，repo 589411/winds）；lab 條目 `winds-tutorials` 已上架。

## 現況
純靜態單頁（index.html + data.js），67 筆 YouTube 教學、七種樂器（長笛、小提琴、單簧管、薩克斯風、中提琴、大提琴、法國號）。2026-11-24 加入薩克斯風與三種提琴（yt-dlp 搜尋後人工挑選，簡介依標題與時長撰寫，未做品質閘門）。2026-11-23 用 frontend-design 流程重做視覺：
五線譜樂器選擇器（音高對應音域）、節目單式列表、真實縮圖（`scripts/verify.py` 從 oEmbed 存 `thumb`）、進度圓點。
`#flute`／`#violin`／`#clarinet`／`#sax`／`#viola`／`#cello`／`#horn` 可直接分享篩選連結。進度只在瀏覽器 localStorage（key `winds-done-v1`，沿用不丟舊進度）。

## 下一個具體動作 ⭐
決定要不要做「品質閘門」：yt-dlp 抓觀看數／訂閱數／讚率設門檻，再讓 agy 為每支分級（入門／進階）並排學習順序。
沒做之前，lab 的描述維持「連結存在」的誠實版本；做了要改 lab 的 `data/projects.yaml` 該條 description。

## 怎麼驗證
`python3 scripts/verify.py` 須印 `ok 67 / dead 0`（verify 只檢 oEmbed；新增影片另用 yt-dlp 的 `playable_in_embed` 確認可嵌入）；手機 390px 無橫捲；勾選後重新整理進度仍在。

## 已知限制
- 字型走 Google Fonts（LXGW WenKai TC、Noto Sans TC），載入時會對 Google 發請求。要完全不外連就得自架字型子集。
- 縮圖來自 i.ytimg.com（已加 no-referrer）；來源 67 筆未做品質篩選；新增的 39 筆簡介是依標題寫的，沒逐支看過內容，法國號中文資源多為介紹而非教學。
