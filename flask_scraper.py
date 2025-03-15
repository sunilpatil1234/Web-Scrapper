from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import pandas as pd

app = Flask(__name__)

EXCLUDED_DOMAINS = ["facebook.com", "twitter.com", "gmail.com", "youtube.com"]

def scrape_website(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        headlines = soup.find_all("a")
        scraped_data = []

        for headline in headlines[:10]:  
            text = headline.text.strip()
            link = headline.get("href", "")

            if any(domain in link for domain in EXCLUDED_DOMAINS):
                continue  # Skip unwanted links

            scraped_data.append({"Text": text, "URL": link})

        return scraped_data
    except:
        return []

@app.route("/", methods=["GET", "POST"])
def index():
    data = []
    if request.method == "POST":
        url = request.form["url"]
        data = scrape_website(url)
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
