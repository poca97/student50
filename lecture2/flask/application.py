from flask import Flask

app = Flask(__name__)
@app.route=("/")
def main():
    headline = "Hello, world"
    return render_template("index.html", headline=headline)

@app.route("/david")
def david():
    return "Hello, Dav"")id!"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}!</h1>"
