from flask import flask
app = Flask(__name)

@app.route('/')
def index():
  return '<h1>Hello World!</h1>'
