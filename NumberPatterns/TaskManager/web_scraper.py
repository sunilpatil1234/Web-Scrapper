import requests
from bs4 import BeautifulSoup

def fetch_news():
    url = "https://news.ycombinator.com/"  # Example: Scraping Hacker News headlines
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        headlines = soup.find_all("a", class_="storylink")

        print("\n📢 Top News Headlines from Hacker News:\n")
        for idx, headline in enumerate(headlines[:10], start=1):
            print(f"{idx}. {headline.text} - {headline['href']}")
    else:
        print("Failed to fetch the website. Check the URL.")

if __name__ == "__main__":
    fetch_news()
