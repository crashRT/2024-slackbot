# 2024-slackbot


## 環境構築

### 1. リポジトリをクローン

今回必要なものをダウンロードします。
以下のコマンドを実行してください。
```shell
git clone https://github.com/crashRT/2024-slackbot.git
```
lsコマンドでディレクトリ（Windowsでのフォルダ）の中を確認できます。`2024-slackbot`が増えていることを確認しましょう。

```shell
ls
```
↓こんな感じの表示があるはず
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
source init.sh
```
↓こんな感じで最初に `(.venv)`とついたらOK
```
(.venv) crashrt@tachyon:~$
```

### 3. トークンの設定
`.env` というファイルを開いて、以下のように書き込んでください。
それぞれの内容はDMで送ります。

```
BOT_TOKEN=<Bot User OAuth Token (xoxbで始まる長いやつ)>
APP_TOKEN=<App-Level Token (xappで始まる長いやつ)>
```

### 4. 起動

次のコマンドでSlack Botを起動できます。
```shell
python3 app.py
```

停止するには、`Ctrl + C`を押してください。
変更を反映する場合は一旦停止してから再度起動してください。