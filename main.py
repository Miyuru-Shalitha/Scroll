from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SECRET_KEY"] = "sdf3sdf4g5$fg%^&*(sdfjsd,kfds"

# CONNECT TO DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///scroll.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
