import json
import requests
import api_keys


def scrape(file_name):
    url = "https://realtor.p.rapidapi.com/properties/v2/list-sold"

    querystring = {"city": "Los Angeles", "offset": "0",
                   "state_code": "CA", "limit": "10000", "sort": "sold_date"}

    headers = {
        'x-rapidapi-key': api_keys.x_rapidapi_key,
        'x-rapidapi-host': "realtor.p.rapidapi.com"
    }

    print("Reqesting data from API")
    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    properties = response.json()["properties"]
    print("Writing file")
    f = open(file_name, "w")
    json.dump(properties, f)
    f.close()
