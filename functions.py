import sqlite3

connection = sqlite3.connect('animal.db')
cursor = connection.cursor()
# query_1 = '''CREATE TABLE colors(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(30) )'''
# query_2 = '''INSERT INTO colors (name) SELECT color1 FROM animals'''
# query_3 = '''CREATE TABLE animal_colors(animal_id INT, color_id INT )'''
# query_4 = '''INSERT INTO animal_colors SELECT animals."index", colors.id FROM animals JOIN colors ON color1 = colors.name'''
query_5 = '''INSERT INTO animal_colors SELECT animals."index", colors.id FROM animals JOIN colors ON color2 = colors.name'''
# cursor.execute(query_1)
# cursor.execute(query_2)
# cursor.execute(query_3)
# cursor.execute(query_4)
cursor.execute(query_5)
# result = cursor.fetchall()
connection.close()

