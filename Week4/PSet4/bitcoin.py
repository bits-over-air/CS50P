import sys
import requests
import json

api_key = "be0eea31502329d6649206e8e70181c0709a47480620414fd2c8cb847f85ba7a"

if len(sys.argv)!=2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

#query API
try:
    url =f"https://rest.coincap.io/v3/assets/bitcoin?apiKey=be0eea31502329d6649206e8e70181c0709a47480620414fd2c8cb847f85ba7a"
    r = requests.get(url)
    data = r.json()
    price = float(data["data"]["priceUsd"])
except requests.RequestException:
    sys.exit("Request Failed")


print(f"${price * n:,.4f}")
