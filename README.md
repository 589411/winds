# winds — 管樂入門 YouTube 教學精選

長笛、單簧管、法國號的入門教學導覽站。純靜態（index.html + data.js），無框架、無後端；進度只存在瀏覽器 localStorage。

- 資料來源：`scripts/seed.py`（來自交接文件）
- 驗證與產生 `data.js`：`python3 scripts/verify.py`（用 YouTube oEmbed 檢查每個連結，任何一筆失效就 exit 1）
- 新增資源：在 seed.py 加一行 → 跑 verify.py → commit data.js
