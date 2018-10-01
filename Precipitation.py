# import necessary libraries
from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import scrape_info

# create instance of Flask app
app = Flask(__name__)

# create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():

    # return template and data
    return render_template("index.html")


# Route that will trigger scrape functions
@app.route("/scrape")
def scrape():

    # connect to database
    conn= "mongodb://localhost:27017/Project2_DB"
    client= pymongo.mongoclient(conn)

    db = client.Project2_DB

    cities=db.cities

    humidity=db.humidity

    # find list from dictionaries

    humidity_dict=list(humidity.find())

    return json.dumps()

if __name__ == "__main__":
    app.run(debug=True)