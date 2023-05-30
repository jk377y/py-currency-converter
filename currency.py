# import the requests module to make HTTP requests
import requests
# import the datetime module to format the unix time stamp returned by the API
from datetime import datetime

# ANSI escape codes for colors
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# define a function to get the list of currencies from the API
def get_currency_list():
    # makes a GET request to the API to get the list of currencies
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    # extracts the currency symbols from the response data
    currency_list = list(data['rates'].keys())
    return currency_list

# define a function to convert the currency using the API by querying the exchange rates for the from_currency
def convert_currency(amount, from_currency, to_currency):
    # make a GET request to the API using the from_currency value provided by the user; convert the response to JSON
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    # extract the exchange rate for the to_currency from the response data
    exchange_rate = data['rates'][to_currency]
    # multiply the amount we want to exchange by the exchange rate found in the response data
    converted_amount = amount * exchange_rate
    # return the converted amount to the caller
    return converted_amount, int(data['time_last_updated'])

# get the list of currency options from the get_currency_list function above
currency_options = get_currency_list()
# print the list of currency options in green
print(f"\n{GREEN}Currency options:{RESET}", currency_options)
# ask the user for the amount to convert
amount = float(input("\nEnter the amount to convert: "))
# ask the user for the currency to convert from; this will be plugged into the API URL to get the exchange rates
from_currency = input("Enter the currency to convert from: ").upper()
# ask the user for the currency to convert to
to_currency = input("Enter the currency to convert to: ").upper()



# need to validate the user input to make sure it's a valid currency
while from_currency not in currency_options or to_currency not in currency_options:
    # prints the list of currency options
    print("\nInvalid currency. Please choose from the available options.")
    print(f"\n{GREEN}Currency options:{RESET}", currency_options)
    # ask the user for the currency to convert from; this will be plugged into the API URL to get the exchange rates
    from_currency = input("Enter the currency to convert from: ").upper()
    to_currency = input("Enter the currency to convert to: ").upper()
    # this loop will continue until the user enters both as valid currencies

# call the convert_currency function, store the result in a variable, and print the result
converted_amount, last_updated = convert_currency(amount, from_currency, to_currency)
# convert the UNIX timestamp to a local time representation
last_updated_local = datetime.fromtimestamp(last_updated).strftime('%m-%d-%Y %H:%M:%S')
print(f"{amount} {GREEN}{from_currency}{RESET} {YELLOW}is equal to{RESET} {converted_amount} {GREEN}{to_currency}{RESET}")
print(f"\n{BLUE}This is accurate as of:{RESET} {last_updated_local}")
