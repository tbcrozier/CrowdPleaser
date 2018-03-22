
CREATE TABLE Person (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    first_name TEXT NOT NULL,
    middle_name TEXT NULL,
    last_name TEXT NOT NULL,
    student_id INTEGER NULL,
    login_id INTEGER NULL,
    FOREIGN KEY(login_id) REFERENCES UserLogin(id)
);

CREATE TABLE UserLogin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    password_hash TEXT NOT NULL
);
