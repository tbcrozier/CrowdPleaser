# Hello, World!
A "Hello, World" program is a simple program that is meant to demonstrate basic syntax of a programming language. It prints "Hello, World" to the screen, and then quits.

In this lesson, we'll run a simple web server that outputs "Hello, World" in the browser.

## Starting Flask
Flask is a web framework. Using Flask, we can run a very simple web server on our own computer. The simplest "Hello, World" program in Flask is as follows:
```
from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello World!"
 
if __name__ == "__main__":
    app.run()
```

First let's get this running, and then we'll look at some of the concepts!

Copy the code above into a text editor and save to a file called "hello.py" on your desktop [TODO: Issue #3](https://github.com/tbcrozier/Ravenwood_My1stCode/issues/3).

Now in your terminal, you can run this command:
```
python hello.py
```
![python hello.py](https://github.com/tbcrozier/Ravenwood_My1stCode/blob/master/wiki_images/hello_world_osx.gif?raw=true)

You should see output similar to this:
![http://127.0.0.1:5000/](https://github.com/tbcrozier/Ravenwood_My1stCode/blob/master/wiki_images/hello_world_output_osx.gif?raw=true)

And there you have it! Your first "Hello, World" program!
