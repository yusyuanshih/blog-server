# blog-server

server for [blog-voidcloud.net](https://blog.voidcloud.net)

## Todo List

- 身份驗證:
  - OAuth 2.0: &#x2610;
  - Session: &#x2611;
- 存取控制: &#x2610;
- 資料加密: &#x2611;
  - 密碼儲存風險: &#x2611;
  - 資料傳輸風險: &#x2611;
  - 資料儲存風險: &#x2611;
  - 資料防竄改風險: &#x2611;
  - 安全漏洞風險: -
- 稽核紀錄:
  - 記錄註冊、登入與登出的資訊並記錄於資料庫裡: &#x2611;
  - 並於註冊與登入時傳送登入通知與相關資訊給使用者的電子郵件信箱: &#x2611;
  - 記錄所有的操作行為: &#x2611;
  - 判斷是否於發文或留言時輸入類似密碼的文字，並要求用戶再三確認: &#x2610;
- ORM 框架: &#x2611;
- 跨來源資源共用（CORS）: &#x2611;

## How to start

### Preparation

1. Python version: >= `3.10`
2. copy `.env.example` to `.env`
   - Set up `.env`
3. install dependencies: `pip install -r requirements.txt`

### Run

- `python run.py`

## Contribution
