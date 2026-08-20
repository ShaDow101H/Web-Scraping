# 📚 Web Scraping - Books to Scrape Dataset

This project was developed as part of the **CodeAlpha** internship program. The script automatically scrapes book data from `http://books.toscrape.com/`, cleans the extracted data, and exports it into a structured CSV file.

---

### 📌 Features

* **Automated HTML Parsing:** Extracts web page data using `requests` and `BeautifulSoup4`.
* **Data Cleaning:** Removes non-numeric symbols (`£`, `Â`) from price fields and converts them into numeric `float` format.
* **Structured Data Extraction:** Collects the following attributes for each book:
  * **Title:** Full title of the book
  * **Price (£):** Book price in numerical format
  * **Availability:** Stock status
* **CSV Export:** Exports the processed dataset to `books_dataset.csv` using `Pandas` (encoded in `utf-8-sig`).

---

### 🛠️ Technologies Used

* **Python 3.x**
* **Requests** — For sending HTTP requests
* **BeautifulSoup4** — For parsing HTML structure
* **Pandas** — For structured data manipulation and CSV export

---

### 🚀 Installation & Usage

1. **Clone the repository:**
   ```bash git clone https://github.com/ShaDow101H/Web-Scraping.git
