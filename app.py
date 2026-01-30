from flask import Flask, render_template

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("home.html")

# Create page
@app.route("/create")
def create():
    return render_template("create.html")

if __name__ == "__main__":
    app.run(debug=True)
