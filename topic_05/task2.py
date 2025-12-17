import requests
import sys

def get_rate(code):
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={}&json".format(code)
    response = requests.get(url)
    data = response.json()
    rate = data[0]["rate"]
    return rate

def main():
    currency = input("Enter currency (EUR, USD, PLN): ").upper()
    amount_str = input("Enter amount: ")

    try:
        amount = float(amount_str)
    except ValueError:
        print("Wrong amount")
        return

    if currency not in ["EUR", "USD", "PLN"]:
        print("Wrong currency")
        return

    rate = get_rate(currency)
    result = amount * rate
    print("Result in UAH:", result)

if __name__ == "__main__":
    main()
