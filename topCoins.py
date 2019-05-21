import requests
import json
from coin import Coin

def main():

    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=20&page=1&sparkline=false'
    response = (requests.get(url)).json()

    
    top20 = []


    for i in response:
        top20.append(Coin(i['name'], i['current_price'], i['price_change_percentage_24h']))    

    for coin in top20:
        print(coin.__str__())


if __name__ == '__main__':
  main()