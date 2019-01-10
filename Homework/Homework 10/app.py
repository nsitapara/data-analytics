from flask import Flask, render_template, redirect
import pymongo
import mission_to_mars

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
client.drop_database('nasa_data')
db = client.nasa_data
collection = db.items


app = Flask(__name__)

@app.route("/")
def index():
    try:
        featured_image_url = client.nasa_data.featured_image_url.find_one({})
        mars_weather = client.nasa_data.mars_weather.find_one({})
        mars_facts = client.nasa_data.mars_facts.find_one({})
        article = client.nasa_data.items.find_one({})
        mars_facts = mars_facts["mars_facts"]
    except:
        print("first run, no prior data")
    
    return render_template("index.html", article=article, mars_facts=mars_facts,mars_weather=mars_weather,featured_image_url=featured_image_url)
    
        
        


@app.route("/scrape")
def scraper():
    listings_data = mission_to_mars.scrape()
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
