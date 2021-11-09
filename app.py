from flask import Flask
import sqlite3


app = Flask(__name__)


@app.route('/item_id')
def get_animal(id):



connection = sqlite3.connect('animal.db')
cursor = connection.cursor()
sql = ('''наш sql запрос''')
cursor.execute()
connection.close()


if __name__ == '__main__':
    app.run()