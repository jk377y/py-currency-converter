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

# so far so good, prints a list of currency symbols, but I want to print the currency symbols in green;
# need to accept a value from the user, and let them select the current currency
# then need to let the user select what currency they want to convert to
# then calculate the conversion value