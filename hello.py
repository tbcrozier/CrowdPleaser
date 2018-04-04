from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         id1 = request.form['id']
         email1 = request.form['email']
         first_name1 = request.form['first_name']
         middle_name1 = request.form['middle_name']
         last_name1 = request.form['last_name']
         student_id1 = request.form['student_id']
         user_login_id1 = request.form['user_login_id']

         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO Person (id,email,first_name,middle_name,last_name,student_id,user_login_id) VALUES (?,?,?,?,?,?,?)",(id1,email1,first_name1,middle_name1,last_name1,student_id1,user_login_id1) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from Person")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)