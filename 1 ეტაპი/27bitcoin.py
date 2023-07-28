import requests
import sys
import json


try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    jsonList = r.text
    aList = json.loads(jsonList)
    multiplier = aList['bpi']['USD']['rate']
    multiplier_cleaned = multiplier.replace(',', '')
    multiplier_cleaned = float(multiplier_cleaned)
    amount = input("")

    if amount == "":
        sys.exit("Missing command-line argument")

    finalValue = float(amount)*multiplier_cleaned

    print(f"${finalValue:,.4f}")

except requests.RequestException:
    sys.exit("ERROR 404")

except ValueError:
    sys.exit("Not a number")

