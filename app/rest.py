from app import app
from db import mysql

conn = mysql.connect()
cursor = conn.cursor()


@app.route("/")
def main():
    return "Welcome!"


@app.route('/hello')
def hello():
    return 'I am good, how about you?'


@app.route('/database')
def read():
    cursor.execute("SELECT * FROM employees")
    row = cursor.fetchone()
    result = []
    while row is not None:
        result.append(row[0])
        row = cursor.fetchone()

    return ",".join(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
