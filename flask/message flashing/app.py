from flask import Flask, redirect, url_for, render_template, request, abort, flash
import secrets
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
users = {
    'SAM ': 'sam',
    'ADMIN': 'admin',
    'HOPPER': 'hopper',
    'DEVA': 'deva'
}


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        name = request.form['username'].upper()
        print(name)
        password = request.form['password']
        if name in users and password in users[name]:
            flash(f'you were logged in sucessfully as {name}')
            flash('logout before login again')
            return render_template('flash.html')
        else:
        # abort(401)
            error = 'In valid credentials, Please try again'
            return render_template('login.html', error=error)
    else:
        return redirect(url_for('index'))


# @app.route('/success/<name>')
# def success(name):
#     flash(f'you were logged in sucessfully as {name}')
#     flash('logout before login again')
#     return render_template('flash.html')
#     # return f'logged in sucessfully as {name}'


if __name__ == '__main__':
    app.run(debug=True)
