"""

import CurrencyRates

cr = CurrencyRates()

amount = int(input("Please enter the amount you want to convert: "))

from_currency = input("Please enter the currency code that has to be converted: ").upper()

to_currency = input("Please enter the currency code to convert: ").upper()

print("You are converting", amount, from_currency, "to", to_currency,".")

output = cr.convert(from_currency, to_currency, amount)

print("The converted rate is:", output)

"""

from easy_exchange_rates import API
api = API()
time_series = api.get_exchange_rates(
  base_currency="EUR", 
  start_date="2021-01-01", 
  end_date="2021-08-13", 
  targets=["USD","CAD"]
)
data_frame = api.to_dataframe(time_series)
print(data_frame.head(5))
