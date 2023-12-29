import requests
from bs4 import BeautifulSoup
import time

def get_card_price(card_url):
    headers = {
        'User-Agent': 'Your User Agent String',
    }

    response = requests.get(card_url, headers=headers)
    #code 200 shows that the site is online and working
    if response.status_code == 200:
    
        soup = BeautifulSoup(response.text, 'lxml')
        #this is the location for the price when inspecting element
        price_element = soup.select_one('.price-box-price')

        if price_element:
            
            price = price_element.get_text(strip=True)
            return price
        else:
            print("Price element not found on the page.")
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")

    return None

def get_card_name(card_url):
    headers = {
        'User-Agent': 'Your User Agent String',
    }

    response = requests.get(card_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        name_element = soup.select_one('.gatherer-name')

        if name_element:
            name = name_element.get_text(strip=True)
            return name
        else:
            print("Name element not found on the page.")
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")

    return None

def track_card_price(card_urls, interval_seconds=5):
    while True:
        for card_url in card_urls:
            name = get_card_name(card_url)
            price = get_card_price(card_url)
        

            if name is not None:
                print("Hello, Here is the most recent info on your card!\n")
                print(f"Card Name: {name}\n")

            if price is not None:
                print(f"Current Price: {price}\n")
                print("------------------------------------------------------------------------------------")

             #Used to show how often to refresh your search
        time.sleep(interval_seconds)

# Paste the site you want to scrape below, separate with "," for each thing you want to do.
card_url = [
    'https://www.mtggoldfish.com/price/Dominaria+United/Sheoldred+the+Apocalypse-showcase#paper',
    'https://www.mtggoldfish.com/price/PhyrexiaAll+Will+Be+One/Mondrak+Glory+Dominus#paper' 



]
track_card_price(card_url)
