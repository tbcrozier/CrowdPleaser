import sqlite3

conn = sqlite3.connect('database.db')
print "Opened database successfully";

conn.execute('DROP TABLE students')
conn.execute('DROP TABLE logins')

conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print "Students table created successfully";

conn.execute('CREATE TABLE logins (uname TEXT, pword TEXT, salt TEXT, role TEXT)')
print "Login table created successfully";



conn.close()