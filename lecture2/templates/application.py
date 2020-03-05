from flask import Flask, render_template
app = Flask("__name__")
@app.route("/")
def main():
    headline = "Hello, world!"
    return render_template("index.html", headline=headline)
@app.route("/bye")
def bye():
    headline = "Bye!"
    return render_template("index.html", headline=headline)
