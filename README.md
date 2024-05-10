# 2024-slackbot

## 環境構築

### 1. リポジトリをクローン

今回必要なものをダウンロードします。
以下のコマンドを実行してください。

```shell
git clone https://github.com/crashRT/2024-slackbot.git
```

ls コマンドでディレクトリ（Windows でのフォルダ）の中を確認できます。`2024-slackbot`が増えていることを確認しましょう。

```shell
ls
```

↓ こんな感じの表示があるはず

```
2024-slackbot
```

`2024-slackbot`ディレクトリに移動します。

```shell
cd 2024-slackbot
```

### 2. 環境構築

以下のコマンドを実行すると、今回必要なものがインストールされます。

```shell
make
```

### 3. トークンの設定

`.env` というファイルを開いて、以下のように書き込んでください。
それぞれの内容は DM で送ります。

```
BOT_TOKEN=<Bot User OAuth Token (xoxbで始まる長いやつ)>
APP_TOKEN=<App-Level Token (xappで始まる長いやつ)>
```

### 4. 起動

次のコマンドで Slack Bot を起動できます。

```shell
python3 app.py
```

停止するには、`Ctrl + C`を押してください。
変更を反映する場合は一旦停止してから再度起動してください。

この方法では画面を閉じると、Bot も停止してしまいます。
完成したら、次のコマンドで起動しましょう。
画面を閉じた後も動作し続けます。

```shell
nohup python3 app.py &
```
