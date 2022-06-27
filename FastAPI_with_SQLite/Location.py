import requests

# using mapquest api for getting the coordinate for particular address

# api Secret Key
secretapikey = "8BAwqVnLA6lzVeNCFtkTHaKHhxIzHZhl"

# api end point with query ?location=
locationapi = f"http://www.mapquestapi.com/geocoding/v1/address?key={secretapikey}&location="


def getlocation(address, city, state):
    mainlocationapi = f"{locationapi}{address},{city},{state}"
    req = requests.get(mainlocationapi)
    # taking corordinates from location
    locationData = req.json()["results"][0]["locations"][0]
    # sending coordinates
    return locationData
