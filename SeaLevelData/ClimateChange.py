from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import pandas as pd
import json
from bson import json_util
from bson.json_util import dumps
import PyMongo


#if __name__ == '__main__':
 # main()
# import scrape_info

# create instance of Flask app
app = Flask(__name__)
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/Dion_db"
mongo = PyMongo(app)

# Or set inline
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.Dion_db
# Find data
collection = db.collection.SeaLevelsHistory
print(collection)
# create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():
    SeaLevels = list(db.collection.find())
    print(SeaLevels)
#@app.route("/results")
#def search_results(search):
 #   results = []
 #   search_string = search.data['search']
# 
 #   if search.data['search'] == '':
  #      qry = db_session.query
  #      results = qry.all()

#return template and data
#return render_template("index.html", SeaLevelsHistory=SeaLevelsHistory)

SeaLevelsHistory = db.SeaLevelsHistory
results = SeaLevelsHistory.find()
for result in results:
      print(result)



#Redirect back to home page
# return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
