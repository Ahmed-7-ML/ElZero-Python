import sqlite3

db = sqlite3.connect('APP.db')

cr = db.cursor()

cr.execute("CREATE TABLE if not exists Employees(Essn integer primary key, name text not null )")

my_List = ['Ahmed', 'Akram', 'Amer', 'Zeyad',
'Shimaa', 'Aya', 'Sayed', 'Yara']

for key, user in enumerate(my_List):
    cr.execute(f"INSERT INTO Employees(Essn, name) VALUES ({key + 1}, '{user}')")

# If U run it again =>  UNIQUE constraint failed: Employees.Essn
# key + 1 => to make start value = 1 for personal ID
db.commit()

db.close()