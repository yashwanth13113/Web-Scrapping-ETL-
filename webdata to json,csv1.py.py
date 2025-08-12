import requests
from bs4 import BeautifulSoup
import csv
import json
#Lets we give the url first...
url = "https://quotes.toscrape.com/"
response = requests.get(url)
#checking weather the url is valid or not;
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    
    quotes_data = [] #list inside it dictionary
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')

    for quote, author in zip(quotes, authors):
        quotes_data.append({
            "quote": quote.text.strip(),
            "author": author.text.strip()
        })
    # Save to CSV
    with open("quotes.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["quote", "author"])
        writer.writeheader()
        writer.writerows(quotes_data)
    print("CSV file saved as quotes.csv check your directory")
    # Save to JSON
    with open("quotes.json", mode="w", encoding="utf-8") as file:
        json.dump(quotes_data, file, indent=4, ensure_ascii=False)
    print("JSON file saved as quotes.json check your directory")

else:
    print(f"its failed check here status code {response.status_code}");
print("this is my web extractor script that fetches quotes from a website and saves them in CSV and JSON formats.");
print("Thank you for using this script! Have a great day! :)");
print(" regards yashwanth");

