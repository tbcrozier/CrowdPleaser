from flask import Flask, flash, redirect, render_template, request, session, abort
import hashlib, uuid
import sqlite3

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


db_connection = sqlite3.connect('database.db')
db_cursor = db_connection.cursor()
db_cursor.execute("DROP TABLE IF EXISTS user;")
db_cursor.execute("CREATE TABLE user(id TEXT, salt TEXT, password TEXT);")
db_cursor.execute("INSERT INTO user VALUES('123', '{salt}', '{hash}');".format(salt='234qwlkjs', hash=hash_password('password', '234qwlkjs')))
db_cursor.execute("INSERT INTO user VALUES('234', '{salt}', '{hash}');".format(salt='lkjou234s', hash=hash_password('password', 'lkjou234s')))
db_cursor.execute("INSERT INTO user VALUES('345', '{salt}', '{hash}');".format(salt='903dlouls', hash=hash_password('password', '903dlouls')))
db_connection.commit()


@app.route("/", methods=['GET', 'POST'])
def form():    
    # If the user is loading the login page:
    if request.method == "GET":
        return render_template('sign.html', error='')
    # Otherwise, if they're submitting the login form:
    elif request.method == 'POST':
        # Get the user input:
        user_id = request.form['id']
        password = request.form['password']

        # Get the user from the database:
        user_data = get_auth_for_user(user_id)
        # If the user isn't found, return an error:
        if user_data is None:
            return render_template('sign.html', error="NO SUCH USER")
        else:
            # See if the saved password hash matches this one:
            user_id, salt, password_hash = user_data
            if password_hash == hash_password(password, salt):
                user_info = {}
                return render_template('home.html', user_info=user_info)
            # If they don't match, it's the wrong password:
            else:
                return render_template('sign.html', error="INVALID PASSWORD")

app.run()
