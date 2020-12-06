# import necessary libraries
from flask import Flask, render_template
import pymongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# create mongo connection
client = pymongo.MongoClient()
db = client.mars_db
collection = db.mars_data_entries

# Route to render index.html template for initial scraping
@app.route("/")
def home():

    # Return template
    return render_template("index.html")

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function and save the results to a variable
    scraped_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mars_data.update({}, scraped_data, upsert=True)

    # Redirect to the scraped data page
    return redirect("/data")

# Route to render data.html template using data from Mongo
@app.route("/data")
def data():

    # Find one record of data from the mongo database
    mars_info = db.mars_data_entries.find_one()

    # Return template and data
    return render_template("data.html", info=mars_info)


if __name__ == "__main__":
    app.run(debug=True)