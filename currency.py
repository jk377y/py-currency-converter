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

    return currency_list

# Get the list of currency options
currency_options = get_currency_list()

# print the list of currency options in green
print(f"\n{GREEN}Currency options:{RESET}", currency_options)
# ask the user for the amount to convert
amount = float(input("\nEnter the amount to convert: "))
# ask the user for the currency to convert from; this will be plugged into the API URL to get the exchange rates
from_currency = input("Enter the currency to convert from: ").upper()
# ask the user for the currency to convert to
to_currency = input("Enter the currency to convert to: ").upper()


def convert_currency(amount, from_currency, to_currency):
    # make a GET request to the API using the from_currency value provided by the user; convert the response to JSON
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()

    # extract the exchange rate for the to_currency from the response data
    exchange_rate = data['rates'][to_currency]

    # perform the currency conversion
    converted_amount = amount * exchange_rate
    print(converted_amount) #not working yet
    return converted_amount



get_currency_list()


# then calculate the conversion value
