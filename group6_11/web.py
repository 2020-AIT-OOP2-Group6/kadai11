import os
import pathlib
# request フォームから送信した情報を扱うためのモジュール
# redirect  ページの移動
# url_for アドレス遷移
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
# ファイル名をチェックする関数
from werkzeug.utils import secure_filename
# 画像のダウンロード
from flask import send_from_directory, render_template

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])
UPLOAD_FOLDER = './uploads'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# http://127.0.0.1:5000/


@app.route('/')
def index():
    img_url = os.listdir("./uploads")
    return render_template("index.html", img_url=img_url)


@app.route('/send', methods=['POST'])
def upload():
    img_file = request.files['img_file']
    if img_file and allowed_file(img_file.filename):
        filename = secure_filename(img_ile.filename)
        img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        img_url = os.listdir("./uploads")
        return render_template('index.html', img_url=img_url)
    else:
        return ''' <p>許可されていない拡張子です</p> '''


if __name__ == "__main__":
    # 完成したら"debug=True"を消す
    app.run(debug=True)
