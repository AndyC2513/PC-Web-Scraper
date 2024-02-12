from bs4 import BeautifulSoup
import pandas as pd
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}

def buildData(item):
    response = requests.get(f'https://www.canadacomputers.com/search/results_details.php?keywords={item}', headers=headers).text

    soup = BeautifulSoup(response, "html.parser")

    all_title = soup.findAll("span", attrs={"class": "productTemplate_title"})
    all_price = soup.findAll("span", attrs={"class": "pq-hdr-product_price"})

    list_titles = []
    list_prices = []

    for title in all_title:
        list_titles.append(title.string)

    for price in all_price:
        list_prices.append(price.string)

    data = pd.DataFrame({'Price': list_prices, 'Product Name': list_titles})
    data = data.sort_values(by='Price')
    data = data.reset_index(drop=True, inplace=False)
    
    return data