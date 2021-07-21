from flask import Flask, redirect, url_for, render_template, request, abort
app = Flask(__name__)

users = {
    'sam': 'sam',
    'admin': 'admin',
    'hopper': 'hopper'
}


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        if  name in users and password in users[name]:
            return redirect(url_for('success',name=name))
        else:
            # abort(401)//
            abort (401,"invalid credentials")   #display costum message
    else:
        return redirect(url_for('index'))


@app.route('/success/<name>')
def success(name):
    return f'logged in sucessfully as {name}'


if __name__ == '__main__':
    app.run(debug=True)
