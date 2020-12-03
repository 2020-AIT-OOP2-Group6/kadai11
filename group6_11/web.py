import os
# request フォームから送信した情報を扱うためのモジュール
# redirect  ページの移動
# url_for アドレス遷移
from flask import Flask, request, redirect, url_for
# ファイル名をチェックする関数
from werkzeug.utils import secure_filename
# 画像のダウンロード
from flask import send_from_directory

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

# http://127.0.0.1:5000/
@app.route('/')
def index():
    return render_template("index.html")