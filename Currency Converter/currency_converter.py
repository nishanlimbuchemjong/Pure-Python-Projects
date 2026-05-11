import requests
API_KEY = "a0a9bf5526260d1fca1e99e4"

def main_converter():
    currency_from = input("Enter your currency (e.g. USD, NPR, EUR) : ").upper()
    currency_to = input("Enter the currency to convert (e.g. USD, NPR, EUR) : ").upper()
    amount = float(input("Enter your amount: "))

    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{currency_from}"

    try:
        response = requests.get(url)
        data = response.json()
        if data['result'] != 'success':
            print("\nMessage: API Error")

        conversion_rate = data['conversion_rates']

        if currency_to not in conversion_rate:
            print(f"\nMessage: {currency_to} not Found!")

        total_amount = amount * conversion_rate[currency_to]

        print(f"\nConversion from {currency_from} to {currency_to}:\n``````````````````````````````")
        print(f"{amount} {currency_from} = {total_amount:.4f} {currency_to}\n")
    except Exception as e:
        print("Error: ", e)

if __name__ == '__main__':
    main_converter()