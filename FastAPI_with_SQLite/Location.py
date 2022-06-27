import requests

# using mapquest api for getting the coordinate for particular address

# api Secret Key
secretapikey = "8BAwqVnLA6lzVeNCFtkTHaKHhxIzHZhl"

# api end point with query ?location=
locationapi = f"http://www.mapquestapi.com/geocoding/v1/address?key={secretapikey}&location="


# it's return the address information along with coordinate of and address
# It's take 3 parameter and use them as location query for api

def getlocation(address, city, state):
    mainlocationapi = f"{locationapi}{address},{city},{state}"
    req = requests.get(mainlocationapi)
    locationData = req.json()["results"][0]["locations"][0]
    return locationData
