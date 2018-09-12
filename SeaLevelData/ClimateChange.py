# import necessary libraries
from flask import Flask, render_template, redirect
# from flask_pymongo import PyMongo
# import scrape_info

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/Dion_db"
# mongo = PyMongo(app)

# Or set inline
mongo = Mongo(app, uri="mongodb://localhost:27017/Dion_db")


# create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():

    # Find data
    SeaLevelsHistory = mongo.db.collection.find()

    # return template and data
    return render_template("index.html", SeaLevelsHistory=SeaLevelsHistory)


# Route that will trigger scrape functions
@app.route("/scrape")
def scrape():

    # Run scraped functions
   # weather = scrape_info.scrape_weather()
   # surf = scrape_info.scrape_surf()

    # Store results into a dictionary
   # forecast = {
     #   "time": weather["time"],
      #  "location": weather["name"],
      #  "min_temp": weather["min_temp"],
      #  "max_temp": weather["max_temp"],
      #  "surf_location": surf["location"],
      #  "height": surf["height"],
    #}

    # Insert forecast into database
   # mongo.db.collection.insert_one(forecast)

    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
