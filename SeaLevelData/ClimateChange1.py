from flask import Flask, render_template
from flask_pymongo import PyMongo

#import pymongo

# create instance of Flask app
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Dion_db"
mongo = PyMongo(app)

#conn = 'mongodb://localhost:27017'
#client = pymongo.MongoClient(conn)
#db = client.Dion_db

# Drops collection if available to remove duplicates
#db.Dion.drop()
# Find data
#collection = db.collection.SeaLevelsHistory
#print(collection)

@app.route("/")
def index():
#    SeaLevels = list(db.Dion.find())
#    print(SeaLevels)
    SeaLevels = mongo.db.SeaLevelsHistory
    
    #return SeaLevels.name
    return render_template('index.html', SeaLevels=SeaLevels.find())

@app.route("/test")
def test():
    return "Test"

@app.route("/SeaLevels")
def SeaLevel():
    SeaLevels = mongo.db.SeaLevelsHistory
    return render_template('index.html', SeaLevels=SeaLevels.find())
#    conn = 'mongodb://localhost:27017'
#    client = pymongo.MongoClient(conn)
#    db = client.Dion_db
#    collection = db.collection.SeaLevelsHistory
#    return render_template('SeaLevel.html',)


if __name__ == "__main__":
    app.run(debug=True)


