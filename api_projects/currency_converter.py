import requests

def get_exchange_rate(from_currency, to_currency, api_key):
    url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}?api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    rate = data['rates'][to_currency]
    return rate

def convert_currency(amount, from_currency, to_currency, api_key):
    rate = get_exchange_rate(from_currency, to_currency, api_key)
    converted_amount = amount * rate
    return converted_amount

def main():
    api_key = 'aff049e232424a5189e68e844f657068'
    while True:
        try:
            amount = float(input('Enter the amount to convert: '))
            break
        except ValueError:
            print('Invalid input. Please enter a number.')

    while True:
        from_currency = input('Enter the currency to convert from: ').upper()
        if from_currency == 'EXIT':
            print('Exiting the program...')
            return
        if len(from_currency) != 3:
            print('Invalid currency code. Please enter a 3-letter currency code.')
            continue
        break

    while True:
        to_currency = input('Enter the currency to convert to: ').upper()
        if to_currency == 'EXIT':
            print('Exiting the program...')
            return
        if len(to_currency) != 3:
            print('Invalid currency code. Please enter a 3-letter currency code.')
            continue
        break

    converted_amount = convert_currency(amount, from_currency, to_currency, api_key)
    print(f'{amount} {from_currency} is equal to {converted_amount} {to_currency}')

if __name__ == '__main__':
    main()