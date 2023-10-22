from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/hello_world_1")
def hello_world1():
    return "<h1>Hello, World!1</h1>"

@app.route("/hello_world!_2")
def hello_world2():
    return "<h1>Hello, World!2</h1>"
@app.route("/test")
def test():
    a = 6+5
    return "this is my function for return{}".format(a)
@app.route("/test1")
def test1():
    d = request.args.get('y')
    return "this is my test1{}".format(d)

if __name__=="__main__":
    app.run(host="0.0.0.0")
