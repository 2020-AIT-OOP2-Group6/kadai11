import os
# request フォームから送信した情報を扱うためのモジュール
from flask import Flask, request, render_template, send_from_directory
# ファイル名をチェックする関数
from werkzeug.utils import secure_filename
import glob

app = Flask(__name__)

# 画像のアップロード先のディレクトリ
UPLOAD_FOLDER = './input-image'


OUTPUT_FACEWAKU_FOLDER = './facewaku'
OUTPUT_GRAYSCALE_FOLDER = './grayscale-image'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FACEWAKU_FOLDER'] = OUTPUT_FACEWAKU_FOLDER
app.config['OUTPUT_GRAYSCALE_FOLDER'] = OUTPUT_GRAYSCALE_FOLDER



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/upload',methods=['POST'])
def uploads_file():
    if 'file' not in request.files:
        render_template("index.html",message="ファイルを選択してください")

    # データの取り出し
    file = request.files['file']

    filename = file.filename

    if filename == '':
        render_template("index.html",message="ファイルを選択してください")
    
    # 下記のような情報がFileStorageからは取れる
    print('file_name={}'.format(filename))
    print('content_type={} content_length={}, mimetype={}, mimetype_params={}'.format(
        file.content_type,
        file.content_length,
        file.mimetype,
        file.mimetype_params))

    # ファイルの保存
    file.save(os.path.join(UPLOAD_FOLDER, filename))

    return render_template("index.html",message="アップロードが完了しました")
    
if __name__ == "__main__":
    #　完成したら"debug=True"を消す
    app.run(debug=True)