import requests 
import json

try:
    response = requests.get("https://cat-fact.herokuapp.com/facts/random", params={"animal_type": "cat" ,"amount": 10}, timeout=0.001)
    data = response.json()

    fakty = []
    counter = 1

    for fact in data:
        fakty.append(f"{counter}. {fact["text"]}")
        counter += 1

    with open ("kocici_fakta.json", mode="w", encoding="utf-8") as file:
        json.dump(fakty, file, ensure_ascii=False, indent=4)
   
    print("File createt succesfully.")

except (TimeoutError, ConnectionError, requests.exceptions.RequestException):
    print("Check your network availability and speed, please.")
except (FileNotFoundError, PermissionError, OSError):
    print("Error opening file.")
except (Exception) as e:
    print("Something goes wrong.")
    print(e)
