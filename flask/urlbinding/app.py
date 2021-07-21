from flask import Flask, render_template, redirect, url_for, request
from form import FormName

import secrets
from flask_wtf.csrf import CsrfProtect

app = Flask(__name__)

# app.config['SECRET KEY'] = secrets.token_hex(16)
# CsrfProtect(app)
admins = ['bob', 'admin', 'sam']
users = ['falcon', 'winter soldider', 'karli']


@app.route('/', methods=['GET', 'POST'])
def welcome():
    # form = FormName()
    # if form.validate_on_submit():
    #     result = request.form
    if request.method == 'POST':
        req = request.form
        name = req["name"]
        print(name)
        if name in admins:
            return redirect(url_for('admin',admin_name = name))
        elif name in users:
            return redirect(url_for('user', user_name=name))
        else:
            return redirect(url_for('guest', guest_name=name))
    return render_template('index.html')


@app.route('/admin')
@app.route('/admin/<admin_name>')
def admin(admin_name):
    return f'hello admin, {admin_name}'


@app.route('/quest/<guest_name>')
def guest(guest_name):
    return f"hello {guest_name}, you are guest"


@app.route('/user/<user_name>')
def user(user_name):
    return f"hellow {user_name} you are user"


@app.route('/<name>')
def vistor(name):
    
    if name in admins:
        return redirect(url_for('admin',admin_name = name))
    elif name in users:
        return redirect(url_for('user', user_name=name))
    else:
        return redirect(url_for('guest', guest_name=name))


if __name__ == '__main__':
    app.run(debug=True)
