from flask import Flask, render_template
from scrapers.amazon_scraper import scrap_amazon_data
from scrapers.flipkart_scraper import scrape_flipkart_data
from scrapers.goodreads import scrape_quote_data
from scrapers.mutual_funds_scraper import scrape_funds_data
from scrapers.top_colleges_scraper import scrape_colleges_data
from scrapers.spotify_scraper import scrape_spotify_data
from scrapers.books_scraper import scrape_books_data
from scrapers.imdb_scraper import scrape_movies_data
from scrapers.json_scraper import scrape_json_data
from scrapers.dummy_json_scraper import scrape_dummy_json_data
from scrapers.fakestore_api_scraper import scrape_fakestore_api_data
from scrapers.courses_api_scraper import scrape_courses_data
from scrapers.feedbacks_api_scraper import scrape_feedbacks_data
from scrapers.myntra_scraper import scrape_myntra_data
from scrapers.github_scraper import scrape_github_data

app = Flask(__name__) # main

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/learnmore")
def learnmore():
    return render_template("learnmore.html")

@app.route("/webscraping")
def webscraping():
    return render_template("webscraping.html")    

@app.route("/static_scraping")
def static_scraping():
    return render_template("static_scraping.html")


@app.route("/dynamic_scraping")
def dynamic():
    return render_template("dynamic_scraping.html")


@app.route("/api_scraping")
def api():
    return render_template("api_scraping.html")

@app.route("/amazon_scraper")
def amazon_scraper():
    products=scrap_amazon_data()
    return render_template("amazon_scraper.html", products = products)

@app.route("/flipkart_scraper")
def flipkart_scraper():
    shoes = scrape_flipkart_data()
    return render_template("flipkart_scraper.html", shoes=shoes)


@app.route("/goodreads")
def goodreads_scraper():
    quotes = scrape_quote_data()
    return render_template("goodreads.html", quotes=quotes)


@app.route("/mutual_funds_scraper")
def mutual_funds_scraper():
    funds = scrape_funds_data()
    return render_template("mutual_funds_scraper.html", funds=funds)


@app.route("/top_colleges_scraper")
def top_colleges_scrapers():
    colleges = scrape_colleges_data()
    return render_template("top_colleges_scraper.html", colleges=colleges)

@app.route("/spotify_scraper")
def spotify_scraper():
    songs = scrape_spotify_data()
    return render_template("spotify_scraper.html", songs=songs)

@app.route("/books_scraper")
def books_scraper():
    books = scrape_books_data()
    return render_template("books_scraper.html", books=books)

@app.route("/imdb_scraper")
def imdb_scraper():
    movies = scrape_movies_data()
    return render_template("imdb_scraper.html", movies=movies)

@app.route("/json_scraper")
def json_scraper():
    data = scrape_json_data()
    return render_template("json_scraper.html", data=data)

@app.route("/dummy_json_scraper")
def dummy_json_scraper():
    data = scrape_dummy_json_data()
    return render_template("dummy_json_scraper.html", data=data)

@app.route("/fakestore_api_scraper")
def fakestore_api_scraper():
    data = scrape_fakestore_api_data()
    return render_template("fake_store_api.html", data=data)

@app.route("/courses_api_scraper")
def courses_api_scraper():
    data = scrape_courses_data()
    return render_template("courses_api_scraper.html", data=data)



@app.route("/feedbacks_api_scraper")
def feedbacks_api_scraper():
    data = scrape_feedbacks_data()
    return render_template("feedbacks_api_scraper.html", data=data)

@app.route("/myntra_scraper")
def myntra_scraper():
    products = scrape_myntra_data()
    return render_template("myntra_scraper.html", products=products)

@app.route("/github_scraper")
def github_scraper():
    repositories = scrape_github_data()
    return render_template("github_scraper.html", repositories=repositories)


if __name__ == "__main__":
     app.run(debug=True, port=5002)