from flask import Flask, flash, render_template,  request, session
import sqlite3 as sql
import bcrypt
import hashlib, uuid
import os
app = Flask(__name__)


def hash_password(password, salt):
    """
    Take a password and a salt, and return a hashed password
    """
    password_string = (password + salt).encode('utf-8')
    hashed_password = hashlib.sha512(password_string).hexdigest()
    return hashed_password


def get_auth_for_user(user_id):
    """
    Take a user_id, and return what we know about that user
    """
    db_cursor.execute("SELECT * FROM user WHERE id=" + user_id)
    result = db_cursor.fetchone()
    return result

@app.route('/signup',methods = ['POST', 'GET'])
def signup():
  msg = ""
  if request.method == 'POST':
      try:
         uname = request.form['uname']
         pword = request.form['pword']
         role = request.form['role']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            
            # Create a random salt for this user
            salt = bcrypt.gensalt()
            password_hash = hash_password(pword, salt)
            cur.execute("INSERT INTO logins (uname,pword,salt,role) VALUES (?,?,?,?)",(uname,password_hash,salt,role) )
            print uname
            print pword
            print salt
            print role           
            con.commit()
            msg = "User successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()
  else:
    # Handle GET request
    return render_template("signup.html")

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   msg = ""
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         pin = request.form['pin']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            
            #cur.execute("""CREATE TABLE students(name, text, addr, text, city text, pin integer)""")
            cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
            con.commit()
            msg = "Student successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/login', methods=['POST', 'GET'])
def do_admin_login():
  if request.method == "POST":
    u_stmt="SELECT CASE WHEN '"+ request.form['username'] +"' IN (SELECT uname FROM logins) THEN 1 ELSE 0 END"  #uname in logins
    p_stmt="SELECT pword FROM logins WHERE uname = '"+request.form['username']+"'"  # retrieve pwd of uname
    s_stmt="SELECT salt FROM logins WHERE uname = '"+request.form['username']+"'"  # retrieve salt of uname
    print u_stmt
    print p_stmt
    with sql.connect("database.db") as con:
      cur = con.cursor()
      pwd = cur.execute(p_stmt)
      uname = cur.execute(u_stmt)
      salt = cur.execute(s_stmt)
      print uname
      print pwd
      print salt
      con.commit()
    con.close()

    hashed_password = hash_password(request.form['password'], salt)
    if hashed_password == pwd and uname == 1:
        session['logged_in'] = True     
        flash('right password!')
        return render_template('home.html')
    else:
        flash('wrong password!')
    return home()
  else:
    return render_template('login.html')



@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return render_template('login.html')

@app.route('/enternew')
def new_student():
   return render_template('student.html')

@app.route('/')
def login():
   return render_template('login.html')

@app.route('/home')
def home():
   return render_template('home.html')

if __name__ == '__main__':
   app.secret_key = os.urandom(12)
   app.run(debug = True)

