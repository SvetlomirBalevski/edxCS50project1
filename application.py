import os

from flask import Flask, session, render_template,request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/", methods=["GET","POST"])
def index():
    # flights = db.execute("SELECT * FROM flights").fetchall()
    # return render_template("index.html", flights=flights)
    # return render_template("index.html")
    return render_template("index.html")

@app.route("/register", methods=["GET","POST"])
def register():
    """Please Enter your credentials."""

    # # Get form information.
    name = request.form.get("name")
    # name = request.form.get("name")
    # try:
    #     flight_id = int(request.form.get("flight_id"))
    # except ValueError:
    #     return render_template("error.html", message="Invalid flight number.")

    # # Make sure the flight exists.
    # if db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).rowcount == 0:
    #     return render_template("error.html", message="No such flight with that id.")
    # db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
    #         {"name": name, "flight_id": flight_id})
    # db.commit()
    return render_template("success.html")
@app.route("/register", methods=["GET","POST"])
def login():
    return render_template("login.html")
