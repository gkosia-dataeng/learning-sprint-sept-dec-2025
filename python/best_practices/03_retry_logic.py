'''Use tenacity to implement rtetry logic

'''

from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import requests


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    retry=retry_if_exception_type((requests.exceptions.Timeout, requests.exceptions.ConnectionError)),
    reraise=True
)
def fetch_data():
    print("Trying to get data..")
    response = requests.get("https://api.example.com/data", timeout=3)
    response.raise_for_status()
    return response.json()


try:
    data = fetch_data()
except Exception as e:
    print(f"Request failed: {e}")