import requests
import pandas as pd


url = "https://data.sec.gov/api/xbrl/companyfacts/CIK0001674101.json"
headers = {"User-Agent": "MyApp/1.0 (dev@example.com)"}

try:
    responses = requests.get(url, headers=headers, timeout=30)
    responses.raise_for_status()
    company = responses.json()
    name = company.get("entityName")
    if name:
        print(name)
    else:
        print("entityName not present in response")
except requests.HTTPError as e:
    print("error:", e)
except requests.RequestException as e:
    print("error:", e)
except ValueError as e:
    print("error:", e)





