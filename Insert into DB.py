# cursor => All operations in sql done by cursor not the connection itself
# commit => Save all changes

import sqlite3

db = sqlite3.connect('app.db')

cr = db.cursor()

# cr.execute("INSERT INTO Users(id, name) VALUES(1, 'Ahmed')")
# cr.execute("INSERT INTO Users(id, name) VALUES(2, 'Mohamed')")
# cr.execute("INSERT INTO Users(id, name) VALUES(3, 'Ali')")

# If you run it again , it will throw an error due to PK Constraints
# sqlite3.IntegrityError: UNIQUE constraint failed: Users.id
cr.execute("DELETE  FROM Users WHERE id > 3")

db.commit()

db.close()