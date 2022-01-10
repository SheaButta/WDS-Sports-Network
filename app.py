from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import wdsncaa_scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/wdsncaa_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    wds = mongo.db.wds.find_one()
    return render_template("index.html", wds=wds)

@app.route("/scrape")
def scrape():
    wds = mongo.db.wds
    wds_data = wdsncaa_scraping.scrape_all()
    wds.update_one({}, {"$set":wds_data}, upsert=True)
    return redirect('/', code=302)


if __name__ == "__main__":
    app.run()
