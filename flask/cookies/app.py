from flask import Flask, redirect,request,render_template,make_response

app = Flask(__name__)
@app.route('/')
def index():
   return render_template('set-cookies.html')

@app.route('/set-cookie', methods= ['GET','POST'])
def setCookie():
   if request.method == 'POST':
       user_name = request.form['name']
       form_response = make_response(render_template('read-cookies.html'))
       form_response.set_cookie('userID',user_name)
       return form_response
@app.route('/get-cookie')
def getCookie():
   name = request.cookies.get('userID')       
   return f'<h1>welcome, {name}</h1> '

if __name__ == "__main__"      :
    app.run(debug=True)