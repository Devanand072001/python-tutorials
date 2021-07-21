from flask import Flask, render_template, redirect, request, session, url_for
import secrets
app = Flask(__name__)

app.secret_key = secrets.token_hex(16)

print(app.secret_key)


@app.route('/')
def index():

    if 'username' in session:
        username = session['username']
        return render_template('index.html', username=username)
    return render_template('not-login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('session.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
