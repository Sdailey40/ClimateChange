from flask import Flask, render_template, redirect,jsonify
from flask_pymongo import PyMongo
import pandas as pd
import json
from bson import json_util
from bson.json_util import dumps
import pymongo


# create instance of Flask app
app = Flask(__name__)

#create route that renders index.html.
@app.route("/")
def home():
      # return template 
    return render_template("index.html")

@app.route("/anamolies")
def scrape():

    #connect to mongo db
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    #set db variable to climate_change db
    db = client.climate_change
    #set collection variable to anamoly_data collection
    collection = db.anamoly_data
    #convert collection into a dictionary for the json dumps function
    anamoly_dict = list(collection.find())

    #return json data when the route is called
    return json.dumps(anamoly_dict, default=json_util.default)
    

if __name__ == "__main__":
    app.run(debug=True)