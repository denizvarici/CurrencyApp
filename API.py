import requests


api_key = 'b764306742774ccce5915651'
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

def bringCurrentRates(exchangeCurrency,buyCurrency):
    result = requests.get(api_url+exchangeCurrency)
    result = result.json()
    result = result['conversion_rates'][buyCurrency]
    return result








