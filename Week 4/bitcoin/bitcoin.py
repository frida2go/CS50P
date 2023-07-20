import requests
import sys
import json

def main():
    if len(sys.argv)!= 2:
        sys.exit("Missing command-line argument")
    elif not isfloat(sys.argv[1]):
        sys.exit("Command-line argument is not a number")
    else:
        b_number = float(sys.argv[1])

    amount = get_bitcoin_price()* b_number
    print(f"${amount:,.4f}")

def isfloat(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

def get_bitcoin_price():
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    read_r = r.json()
    usd_rate = read_r['bpi']['USD']['rate']
    usd_rate =float(usd_rate.replace(",",""))
    return(float(usd_rate))

if __name__ == "__main__":
    main()





