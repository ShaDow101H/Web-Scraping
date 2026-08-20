import pandas as pd
from bs4 import BeautifulSoup
import requests

# 1. Hədəf saytın URL-i
url = "http://books.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    books_data = []

    # 2. Saytdakı bütün kitab bloklarını tapırıq
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        # Kitabın adı
        title = book.h3.a["title"]

        # Qiyməti (£ simvolunu təmizləyirik)
        price_text = book.find("p", class_="price_color").text
        price = float(price_text.replace("£", "").replace("Â", "").strip())

        # Stok vəziyyəti
        availability = book.find(
            "p", class_="instock availability"
        ).text.strip()

        books_data.append(
            {"Title": title, "Price (£)": price, "Availability": availability}
        )

    # 3. Məlumatları DataFrame-ə çevirib CSV kimi saxlayırıq
    df = pd.DataFrame(books_data)
    df.to_csv("books_dataset.csv", index=False, encoding="utf-8-sig")

    print(
        f"✅ Web Scraping uğurla tamamlandı! {len(df)} kitab 'books_dataset.csv' faylına yazıldı."
    )
    print("\nİlkin məlumatlar:")
    print(df.head())
else:
    print("Sayta qoşulmaq mümkün olmadı. Xəta kodu:", response.status_code)