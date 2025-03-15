import requests
from bs4 import BeautifulSoup

# List of websites to exclude
EXCLUDED_DOMAINS = ["facebook.com", "twitter.com", "gmail.com", "youtube.com"]

def scrape_website(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract all links
        headlines = soup.find_all("a")

        if not headlines:
            print("No data found. Try a different website.")
            return

        filtered_results = []
        for headline in headlines:
            text = headline.text.strip()
            link = headline.get("href", "")

            # Skip unwanted websites
            if any(domain in link for domain in EXCLUDED_DOMAINS):
                continue  # Skip this link

            filtered_results.append(f"{text} - {link}")

        # Save to file
        with open("scraped_results.txt", "w", encoding="utf-8") as file:
            print("\n📢 Scraped Data (Filtered):\n")
            for idx, result in enumerate(filtered_results[:10], start=1):
                print(f"{idx}. {result}")
                file.write(f"{idx}. {result}\n")

        print("\n✅ Data saved to 'scraped_results.txt'!")

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    user_url = input("🔗 Enter a website URL to scrape: ")
    scrape_website(user_url)
