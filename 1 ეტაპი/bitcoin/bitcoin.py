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

    # Check if a command-line argument is provided
    if len(sys.argv) < 2:
        sys.exit("")

    # Get the amount from the command-line argument
    amount = sys.argv[1]

    # Convert the amount to a float
    amount = float(amount)

    finalValue = amount * multiplier_cleaned
    print(f"${finalValue:,.4f}")

except requests.RequestException:
    sys.exit("ERROR 404")

except ValueError:
    sys.exit("Not a number")