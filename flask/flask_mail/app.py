from flask import Flask, redirect, request, render_template
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ssig432@gmail.com'
app.config['MAIL_PASSWORD'] = 'Ssig@1234'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/')
def index():
    # msg = Message('Hello world', sender='ssig432@gmail.com', recipients= ['dev.velu2001@gmail.com', 'devanand.cs19@bitsathy.ac.in'])
    # msg.body = 'Hello dev, this is flask sample message'
    # mail.send(msg)
    # sender='ssig432@gmail.com'

    # return f'message sent successfully to {sender}'

    return render_template('index.html')


@app.route('/send-mail', methods=['GET', 'POST'])
def sendMail():
    if request.method == 'POST':
        name = request.form['name']
        recipiant = request.form['email']
        sub = request.form['sub']
        body = f'Hi {name.capitalize()},\n '+request.form['body']
        file_type = request.form['type']
        print('file type: ', file_type)
        f = {'txt': 'text/plain', 'html': "text/html", 'pdf': "application/pdf", 'jpg': 'image/jpg', 'png': 'image/png', 'exe': 'application/x-msdownload', 'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
             'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation'}
        if file_type in f:
            sub_type = f[file_type]
            print(sub_type)
        files = request.files['file']
        files.save(secure_filename(files.filename))
        print(secure_filename(files.filename))
        print(files)
        # print(FileStorage)
        # print(name)
        # print(recipiant)
        # print(sub)
        # print(body)
        mail_message = Message(sub, sender=(
            'SSIG', 'ssig432@gmail.com'), recipients=[recipiant])
        mail_message.body = body

        with app.open_resource(secure_filename(files.filename)) as fp:
            mail_message.attach(secure_filename(
                files.filename), sub_type, fp.read())
        mail.send(mail_message)
        return f'mail sent sucessfully to {recipiant}'
    else:
        return 'mail unseccessful'


if __name__ == '__main__':
    app.run(debug=True)
