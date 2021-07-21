from flask import Flask, render_template
app = Flask(__name__)

name = "devanand"

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


employee1 = Employee("devanand", 19, 50_000)
employee2 = Employee("bob", 17, 55_000)
@app.route('/')
@app.route("/home")
def home():
    
    return render_template("home.html", name=name)


@app.route("/about")
def about():
    # return "<center><h1>about page</h1></center>"
    return render_template("about.html", thisdict=thisdict,name=name)

@app.route("/employee")    
def employee():
    return render_template("employee.html",emp1=employee1,emp2= employee2)


if __name__ == "__main__":
    app.run(debug=True)
