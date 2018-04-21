from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hello/<string:name>/", methods=['GET', 'POST'])
def form(name):
    if request.method == 'POST':
        password = request.form
    else:
    	password = "(not provided)"

    return render_template(
        'sign.html',name=name)

app.run()
