from flask import Flask, render_template, redirect,jsonify
from flask_pymongo import PyMongo
import pandas as pd
import json
from bson import json_util
from bson.json_util import dumps
import pymongo


# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/climate_anamolies"
mongo = PyMongo(app)

#create route that renders index.html.
@app.route("/")
def home():
      # return template 
    return render_template("index.html")

@app.route("/anamolies")
def scrape():

    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    db = client.climate_change
    collection = db.anamoly_data   

    anamoly_dict = list(collection.find())


    return json.dumps(anamoly_dict, default=json_util.default)
    

if __name__ == "__main__":
    app.run(debug=True)