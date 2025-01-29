# connect
# execute
# close

import sqlite3 

db = sqlite3.connect("app.db")

db.execute("create table if not exists `Users`(name text not null, id integer  primary key)")
db.execute("create table if not exists `Skills`(name text not null, progress integer  primary key)")
db.execute(
    "create table if not exists `User_Skill`(progress integer , id integer)")



db.close()