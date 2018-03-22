
CREATE TABLE Person (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    first_name TEXT NOT NULL,
    middle_name TEXT NULL,
    last_name TEXT NOT NULL,
    student_id INTEGER NULL,
    user_login_id INTEGER NULL,
    FOREIGN KEY(user_login_id) REFERENCES UserLogin(id)
);

CREATE TABLE UserLogin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    password_hash TEXT NOT NULL
);
