import sqlite3

#1) fetchone() => Retrieve single row(Tuple) or none of rows if not available
#2) fetchall() => fetch all rows of a query result as a list of tuples and 
# may return an empty list if no row (record) to fetch
#3) fetchmany(size) => accept the number of rows that U want to retrieve
db = sqlite3.connect("company.db")

cr = db.cursor()

# query1 = cr.execute("SELECT * FROM Employees")
# print(query1.fetchone())

# print(query1.fetchall())

# print(query1.fetchmany(4))


query2  = cr.execute("SELECT name FROM Employees")
# print(query2.fetchone())

# print(query2.fetchall())

# print(query2.fetchmany(4))

query3 = cr.execute("SELECT Essn FROM Employees")

# print(query3.fetchone())

# print(query3.fetchall())

# print(query3.fetchmany(4))


query4 = cr.execute("SELECT * FROM Employees ORDER BY Essn")


# print(query4.fetchone())

# print(query4.fetchall())

# print(query4.fetchmany(4))

# Aggregate Functions (min, max, sum, avg, count)
query5 = cr.execute("SELECT sum(Essn) FROM Employees")
print(query5.fetchone())

# WILD CARDS
query6 = cr.execute("SELECT * FROM Employees WHERE name LIKE 'A%' ORDER BY Essn")


# print(query6.fetchone())

print(query6.fetchall())

# print(query6.fetchmany(4))

# BETWEEN AND, IN, IS, LIKE
query7 = cr.execute("SELECT * FROM Employees WHERE Essn BETWEEN 3 AND 6 ORDER BY Essn")
print(query7.fetchall())
