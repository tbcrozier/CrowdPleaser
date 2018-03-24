# Step 1
import sqlite3

# Step 2
conn = sqlite3.connect('database.db')
print "Opened database successfully";

# Step 3
conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print "Table created successfully";
conn.close()