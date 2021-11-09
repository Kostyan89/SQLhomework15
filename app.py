from flask import Flask
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect('animal.db')
cursor = connection.cursor()
query_1 = "CREATE TABLE colors(id INTEGER PRIMARY KEY AUTOINCREMENT, name(VARCHAR(30))"
query_2 = 'INSERT INTO colors(name) SELECT color_1 FROM animals'
cursor.execute(query_1)
cursor.execute(query_2)
connection.close()

if __name__ == '__main__':
    app.run(debug=True)
