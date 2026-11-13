# 物件確認サイト（GitHub Pages）

販売図面のQRコードから、物件の販売状況の確認・資料請求・内見依頼ができるサイトです。

- 公開ページ：`index.html?property=物件ID`
- 管理画面（社内用）：`admin.html`
- データ：`data/site.json`（管理画面が自動で更新します）／資料：`documents/`

## 管理画面の使い方（営業担当）

1. 管理者がリポジトリに担当者を Collaborator（書き込み権限）として招待します。
2. 担当者はGitHubで **Fine-grained personal access token** を作成します（Settings → Developer settings）。
   - Repository access：このリポジトリのみ
   - Permissions：Contents → **Read and write**
3. `https://citycreationnet-cloud.github.io/bukkenkakunin/admin.html` を開き、トークンでログインします。
4. 物件の追加・編集・資料PDFのアップロード・販売状況の変更ができます。保存は公開サイトに1〜数分で反映されます。

- 販売状況の変更は一覧のプルダウンからすぐ行えます（最終確認日時も自動更新）。
- 2人が別々の物件を同時に編集しても、互いの変更は上書きされません（保存時に最新データへ反映）。
- 変更履歴はGitHubのコミット履歴に残ります。
- トークンはその端末のブラウザにのみ保存されます。共有端末では使わず、不要になったらログアウトとトークン削除をしてください。
- `admin.html` は公開されますが、トークンがなければ何も操作できません。

## QRコード

各物件のURLは `公開URL/index.html?property=物件ID` です。印刷後は物件IDと公開URLを変えないでください。まとめて作る場合：

```bash
pip install segno
python3 tools/make_qr.py https://citycreationnet-cloud.github.io/bukkenkakunin/
```

## 含まれないもの

内見依頼・資料請求は、入力内容がメールアプリで作成される方式です（利用者が送信を完了する必要があります）。サーバー保存・自動通知・業者認証はありません。

GitHub Pagesへ置いた情報・資料は公開されます。社内資料・個人情報・パスワードを置かないでください。`noindex` は検索エンジンへの依頼であり、閲覧制限ではありません。
