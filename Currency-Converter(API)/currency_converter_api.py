"""Program to convert currency using API"""

import requests

api_key = "your api key"


user_input = str(input(
    "\n1. List of currencies and their symbols\n2. Change currencies\n3. Exit\n\nYour input: "))

if user_input == '1':
    currencies = requests.get(
        f"https://free.currconv.com/api/v7/currencies?apiKey={api_key}")

    dict_currency = currencies.json()['results']

    for value in dict_currency:
        try:
            print("Currency Name: " + dict_currency[value]['currencyName'])
            print("Currency Symbol: " + dict_currency[value]['currencySymbol'])
            print("Currency ID: " + dict_currency[value]['id'] + "\n")
        except:
            print("Currency ID: " + dict_currency[value]['id'] + "\n")


if user_input == '2':
    from_currency = str(input("From Currency: ")).upper()
    to_currency = str(input("To Currency: ")).upper()
    currency_rate = f"{from_currency}_{to_currency}"
    currency_amount = int(input("Enter the amount: "))

    currencies_rate = requests.get(
        f"https://free.currconv.com/api/v7/convert?q={currency_rate}&compact=ultra&apiKey={api_key}")

    dict_converted = float(currencies_rate.json()[currency_rate])
    print(
        f"\nThe currency rate from {from_currency} to {to_currency} is {dict_converted} equivalent to 1")
    print(f"Converted Amount: {dict_converted*currency_amount}\n")

else:
    print("Exiting...\n")
