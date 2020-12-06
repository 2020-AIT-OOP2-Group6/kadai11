import os
# request フォームから送信した情報を扱うためのモジュール
# url_for アドレス遷移
from flask import Flask, request, render_template, send_from_directory
# ファイル名をチェックする関数
from werkzeug.utils import secure_filename
import glob

# 画像のアップロード先のディレクトリ
UPLOAD_FOLDER = './uploads'
# アップロードされる拡張子の制限
ALLOWED_EXTENSIONS = set(['png', 'jpg'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# http://127.0.0.1:5000/
@app.route('/',methods=['GET', 'POST'])
def uploads_file():
    # リクエストがポストかどうかの判別
    if request.method == 'POST':
        # ファイルがなかった場合の処理
        if 'file' not in request.files:
            flash('ファイルがありません')
            return render_template(request.url)
        # データの取り出し
        file = request.files['file']
        # ファイルのチェック
        if file and allwed_file(file.filename):
            # 危険な文字を削除（サニタイズ処理）
            filename = secure_filename(file.filename)
            # ファイルの保存
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # アップロード後のページに転送
            return render_template(url_for('uploaded_file', filename=filename))
    return render_template("index.html")

if __name__ == "__main__":
    #　完成したら"debug=True"を消す
    app.run(debug=True)