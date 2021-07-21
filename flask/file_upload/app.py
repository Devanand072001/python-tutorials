from flask import Flask, render_template, request
# from werkzeug import secure_filename
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import secrets

app = Flask(__name__)

app.secret_key = secrets.token_hex(16)

@app.route('/file-upload')
def upload():
   return render_template('upload.html')

@app.route('/file-uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        file = request.files['file']
        file.save(secure_filename(file.filename))
        print(file)
        return f'file saved successfully {secure_filename(file.filename)}'


if __name__ == '__main__':
    app.run(debug = True)