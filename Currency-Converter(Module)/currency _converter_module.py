# Author: Aashish Sharma
# Github: https://github.com/aasis2520c

""" Currency converter in  python using currency converter module"""

from currency_converter import CurrencyConverter

currency = CurrencyConverter()

from_currency = str(input("From Currency: ")).upper()
to_currency = str(input("To Currency: ")).upper()

currency_amount = int(input("Enter the amount: "))

converted_currency = currency.convert(currency_amount, from_currency, to_currency)

print(f"{from_currency}: {currency_amount}\n{to_currency}: {converted_currency}")
