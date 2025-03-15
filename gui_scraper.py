import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import pandas as pd

# List of excluded websites
EXCLUDED_DOMAINS = ["facebook.com", "twitter.com", "gmail.com", "youtube.com"]

def scrape_website():
    url = url_entry.get()
    if not url.startswith("http"):
        messagebox.showerror("Invalid URL", "Please enter a valid URL (starting with http or https).")
        return
    
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        headlines = soup.find_all("a")
        if not headlines:
            messagebox.showinfo("No Data", "No headlines found. Try a different website.")
            return

        scraped_data.clear()  # Clear previous results
        results_text.delete("1.0", tk.END)

        for idx, headline in enumerate(headlines[:10], start=1):
            text = headline.text.strip()
            link = headline.get("href", "")

            if any(domain in link for domain in EXCLUDED_DOMAINS):
                continue  # Skip unwanted links

            scraped_data.append({"Text": text, "URL": link})
            results_text.insert(tk.END, f"{idx}. {text} - {link}\n")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"⚠️ Error: {e}")

def save_to_csv():
    if not scraped_data:
        messagebox.showwarning("No Data", "No scraped data available to save.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                             filetypes=[("CSV files", "*.csv")])
    if file_path:
        df = pd.DataFrame(scraped_data)
        df.to_csv(file_path, index=False)
        messagebox.showinfo("Saved", f"Data successfully saved to {file_path}.")

# GUI Setup
root = tk.Tk()
root.title("Web Scraper")
root.geometry("600x450")

scraped_data = []

tk.Label(root, text="Enter Website URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

scrape_button = tk.Button(root, text="Scrape Website", command=scrape_website)
scrape_button.pack(pady=5)

save_button = tk.Button(root, text="Save to CSV", command=save_to_csv)
save_button.pack(pady=5)

results_text = scrolledtext.ScrolledText(root, width=70, height=15)
results_text.pack(pady=10)

root.mainloop()
def scrape_multiple_pages(base_url, num_pages):
    scraped_data.clear()
    results_text.delete("1.0", tk.END)

    for page in range(1, num_pages + 1):
        url = f"{base_url}?page={page}"  # Modify based on the website's pagination pattern
        try:
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            headlines = soup.find_all("a")
            if not headlines:
                continue

            for headline in headlines[:10]:  # Modify limit as needed
                text = headline.text.strip()
                link = headline.get("href", "")

                if any(domain in link for domain in EXCLUDED_DOMAINS):
                    continue  # Skip unwanted links

                scraped_data.append({"Text": text, "URL": link})
                results_text.insert(tk.END, f"{text} - {link}\n")

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"⚠️ Error fetching {url}: {e}")

# Example usage:
# scrape_multiple_pages("https://news.ycombinator.com", 3)  # Scrape first 3 pages
