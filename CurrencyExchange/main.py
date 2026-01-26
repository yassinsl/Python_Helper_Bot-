from typing import Any, List,  Dict
import requests
import os

def parse_data()-> Dict[str, Any]:
    amount = int(input("Please Enter The amount: "));
    From_currency = input("Plase enter The Currency you want To convert: ");
    To_currency = input("Plase enter The Currency to convert it: ");
    if not amount or amount < 0:
        raise ValueError("Invalid amount (0 > inf)");
    elif not From_currency or not To_currency:
        raise ValueError("Invalid Currency");
    return{
            'Amount' : amount,
            'From_currency': From_currency.strip().upper(), 
            'To_currency': To_currency.strip().upper() 
            }
def get_data(data) -> float:
    url = "https://api.currencyfreaks.com/v2.0/rates/latest"
    api_key = os.getenv("CURRENCYFREAKS_API_KEY")
    if not api_key: 
        raise ValueError("Empty API KEY")
    response = requests.get(
            url,
            params={
                "base" : data['From_currency'],
                "to" : data['To_currency'],
                "apikey": api_key
                },
            timeout=15
            )
    if response.ok:
        data_r: List[Dect[str, Any]] = response.json();
    else : 
        raise ValueError(f"status: {response.status_code} reason: {response.text}");
    rates = data_r.get('rates', {});
    rate = rates.get(data['To_currency'])
    return float(rate);
def desplay_value(data: Dict, rate_value: float)->None:
    value = data['Amount'] * rate_value
    print(f"convet {data['Amount']}{data['From_currency']} to {data['To_currency']} is {value:.2f}")
def main():
    print("=== Currency Exchange CLI === ")
    print()
    try:
        data = parse_data();
        rate_value = get_data(data);
        desplay_value(data, rate_value)
    except  ValueError as e:
        print(e)
if __name__  == "__main__":
    main()
