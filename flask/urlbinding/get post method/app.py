from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


users = {'admin': 'admin', 'user': 'user'}


@app.route('/welcome/<name>/<password>')
@app.route('/welcome')
def welcome(name,password):
    if any([True for k, v in users.items() if (k == name and v == password)]):
        return f"welcome, {name}"
    else:
        return "invalid credentials"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        name = request.form['name']
        password = request.form['password']
        # if any([True for k,v in users.items() if v == value]):
        return redirect(url_for('welcome', name=name,password=password))
        # if i in users.items():
        #     if  any([True for k, v in users.items() if (k == )]):
        # else:
        #     name = request.args.get("name")
        #     return redirect(url_for('welcome', name=name))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
