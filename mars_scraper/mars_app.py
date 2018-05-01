from flask import Flask, render_template, jsonify, redirect
#from flask_pymongo import PyMongo
import pymongo
import mars_scraper

app = Flask(__name__)

#mongo = PyMongo(app)
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars
collection = db.news

@app.route("/")
def index():
    content = db.collection.find_one()

    return render_template("index.html", content=content)

@app.route("/scrape")
def scrape():
    content = db.collection
    content_data = mars_scraper.scrape()
    content.update(
        {},
        content_data,
        upsert=True
    )

    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)