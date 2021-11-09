import sqlite3

con = sqlite3.connect('animal.db')
cursor = con.cursor()
query_1 = "CREATE TABLE colors(id INTEGER PRIMARY KEY AUTOINCREMENT, name(VARCHAR(30))"
query_2 = 'INSERT INTO colors(name) SELECT color_1 FROM animal'
cursor.execute(query_1)
cursor.execute(query_2)
con.close()

