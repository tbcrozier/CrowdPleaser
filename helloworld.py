from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/home")
def home():
	return "Goodbye World!"

app.run()