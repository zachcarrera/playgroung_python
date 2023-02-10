from flask import Flask, render_template

app = Flask(__name__)


# all these routes use the same function index() to display the html
@app.route("/play")
@app.route("/play/<int:x>")
@app.route("/play/<int:x>/<string:color>")

# index has default values for parameters x and color so it can work
# if the values are given or not
def index(x=3, color="lightblue"):
    return render_template("index.html", boxes=x, color=color)



if __name__ == "__main__":
    app.run(debug=True)