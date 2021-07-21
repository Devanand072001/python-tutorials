from flask import Flask, render_template, request
import secrets
from forms import SignupForm
from flask_wtf.csrf import CsrfProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
CsrfProtect(app)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    # if request.method == "POST":
    #     req = request.form
    #     date = req["date_of_birth"]
    if form.validate_on_submit():
        result = request.form
        # return f'''<h1> Welcome {form.username.data} </h1>'''
        # return render_template("user.html", result=result)
    return render_template("signup.html", form=form, result=request.form)


if __name__ == "__main__":
    app.run(debug=True, port=4000)
