import requests

GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def get_currency_list():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()

    # Extract the currency symbols from the response data
    currency_list = list(data['rates'].keys())

    print(str(currency_list))
    return currency_list

get_currency_list()
