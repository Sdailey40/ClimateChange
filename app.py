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

#create route that renders index.html template
@app.route("/")
def home():
      # return template 
    return render_template("index.html")

@app.route("/anamolies")
def scrape():

    # #climate_scrape_func() is the function built in the other python file (climate_summary.py)
    # climate_df = pd.read_excel('C:/Users/joelb/Documents/Github/ClimateChange/climate_by_city.xlsx')
       
    # climate_df.columns = [str(i) for i in climate_df.columns.values.tolist()]

    # anamoly_data = climate_df.to_dict('list')

    # anamoly_data = climate_summary.climate_scrape_func()

    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    db = client.climate_change
    collection = db.anamoly_data   

    # # # Store results into a dictionary
    # anamoly_dict = { "City" : anamoly_data['City'],
    #             "Country" : anamoly_data['Country'],
    #             "Lat" : anamoly_data['Lat'],
    #             "Lng" : anamoly_data['Lng'],
    #             "rng_1880_1910" : anamoly_data['rng_1880_1910'],
    #             "rng_1911_1940" : anamoly_data['rng_1911_1940'],
    #             "rng_1941_1970": anamoly_data['rng_1941_1970'],
    #             'rng_1971_2000' : anamoly_data['rng_1971_2000'],
    #             'rng_2001_2017' : anamoly_data['rng_2001_2017']
    #         }
    

    # # Insert forecast into database
    # mongo.db.collection.insert_one(anamoly_dict)

    anamoly_dict = list(collection.find())
    
   
    # anamoly_dict.pop('_id')

    return json.dumps(anamoly_dict, default=json_util.default)
    

if __name__ == "__main__":
    app.run(debug=True)