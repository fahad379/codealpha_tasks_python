def get_amount():
  while True:
    try:
      amount = float(input('Enter the amount: '))
      if amount <= 0:
        raise ValueError()
      return amount
    except ValueError:
      print('Invalid amount')

def get_currency(label):
  currencies = ('USD', 'EUR', 'CAD', 'PKR', 'INR')
  while True:
    currency = input(f'{label} currency (USD/EUR/CAD/PKR/INR): ').upper()
    if currency not in currencies:
      print('Invalid currency')
    else:
      return currency

def convert(amount, source_currency, target_currency):
  exchange_rates = {
    'USD': { 'EUR': 0.85, 'CAD': 1.25, 'PKR': 283.50, 'INR': 83.00 },
    'EUR': { 'USD': 1.18, 'CAD': 1.47, 'PKR': 333.53, 'INR': 97.64 },
    'CAD': { 'USD': 0.80, 'EUR': 0.68, 'PKR': 226.80, 'INR': 66.43 },
    'PKR': { 'USD': 0.0035, 'EUR': 0.00299, 'CAD': 0.0044, 'INR': 0.25 },
    'INR': { 'USD': 0.012, 'EUR': 0.010, 'CAD': 0.015, 'PKR': 4.00 },
  }

  if source_currency == target_currency:
    return amount
  
  return amount * exchange_rates[source_currency][target_currency]

def main():
  amount = get_amount()
  source_currency = get_currency('Source')
  target_currency = get_currency('Target')
  converted_amount = convert(amount, source_currency, target_currency)
  print(f'{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}')

if __name__ == "__main__":
  main()
