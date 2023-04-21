import os
import psycopg2
from flask import Flask, render_template, request, redirect, url_for




app = Flask(__name__)
url = os.environ.get("DATABASE_URL")
connection = psycopg2.connect(url)


@app.route('/')
def index():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT greeting FROM messages;")
            messages = [row[0] for row in cursor.fetchall()]
    return render_template('index.html', messages=messages)



@app.route('/submit', methods=['POST'])
def submit():
    message = request.form['message']
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO messages (greeting) VALUES (%s);", (message,))
            connection.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


