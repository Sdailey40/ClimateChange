from flask import Flask, render_template
#from flask_pymongo import pymongo

import pymongo

# create instance of Flask app
app = Flask(__name__)


conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.Dion_db

# Drops collection if available to remove duplicates
db.Dion.drop()
# Find data
collection = db.collection.SeaLevelsHistory
print(collection)

@app.route("/")
def index():
    SeaLevels = list(db.Dion.find())
    print(SeaLevels)
    return render_template('index.html', SeaLevels=SeaLevels)

if __name__ == "__main__":
    app.run(debug=True)


