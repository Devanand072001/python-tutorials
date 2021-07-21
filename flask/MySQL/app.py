
from flask import Flask, render_template, request
from flask_mysqldb import MySQL, MySQLdb
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'myflixdb'

mysql = MySQL(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        value = request.form["search"]
        print(value)
        SQL = "SELECT movie_id,title, director, year_released FROM myflixdb.movies where title like '" + '%' + \
            value+'%' + "' or director like '" + '%'+value+'%' + \
            "' or year_released like '" + '%'+value+'%' + "'"
        cur.execute(SQL)
        print(SQL+"executed successfully")
        mysql.connection.commit()
        db_data = cur.fetchall()
        return render_template('index.html', db_data=db_data)
    cur.execute(
        "SELECT movie_id,title, director, year_released FROM myflixdb.movies")
    db_data = cur.fetchall()
    return render_template('index.html', db_data=db_data)


if __name__ == '__main__':
    app.run(debug=True)
