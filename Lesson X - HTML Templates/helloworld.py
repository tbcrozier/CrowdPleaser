from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/hello/<string:name>/")
def form(name):
    return render_template(
        'sign.html',name=name)

app.run()
