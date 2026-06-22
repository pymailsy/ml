import requests

BASE_URL = "https://raw.githubusercontent.com/pymailsy/ml/main"

def run(n):
    url = f"{BASE_URL}/{n}.txt"

    response = requests.get(url)
    response.raise_for_status()

    print(response.text)
