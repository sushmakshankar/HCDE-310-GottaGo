import urllib.	parse, urllib.request, urllib.error, json, pprint
from geopy.geocoders import Nominatim
# this program will search through three APIs - Refuge Restrooms, Google Events API, and Google Maps API - to identify
# the location of public bathrooms during events. the aim of the project is to encourage community engagement with local
# events by breaking down this barrier of not being able to find an accessible restroom, encouraging more people to discover
# and engage with local events
# psuedocode:
# functionality 1:
# 1) user will input an event
# 2) the program will search through Google Event API to determine the events geolocational data
# 3) the program will then enter that data as a query for a restroom location, and then use the Refuge Restrooms API to present
# the address of the nearest restrooms to the 
def get_events(query):
    try:
        params = {
            'engine': "google_events",
            "q": query,
            "api_key": 'a92af036d04f21a41bce9ee15ec7ff4ec06ce5196b817291a8efbc865376eb15'
        }

        base_url = "https://serpapi.com/search.json"
        url = f"{base_url}?{urllib.parse.urlencode(params)}"
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        response_str = response.read().decode('utf-8')
        data = json.loads(response_str)
        return data["events_results"]
    
    except urllib.error.HTTPError as e:
        print(e.code, e.reason)
        return []

#geocode to scrape cords 
def geocode(address, ada, unisex):
    geolocator = Nominatim(user_agent="functions")
    location = geolocator.geocode(address)
    if location == None:
        return None
    return get_restroom(location.latitude, location.longitude, ada, unisex)


#accesses restroom api 
def get_restroom(latitude, longitude, ada=False, unisex=False):
    try:
        #do somethign with cords & geo wtv
        params = {
            'lat': latitude,
            'lng': longitude,
            'ada': ada,
            'unisex': unisex
        }

        url = "https://www.refugerestrooms.org/api/v1/restrooms/by_location.json"
        url = f"{url}?{urllib.parse.urlencode(params)}"
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        response_str = response.read().decode('utf-8')
        data = json.loads(response_str)
    except urllib.error.HTTPError as e:
        print(e.code, e.reason)
        return []


# data = get_restroom(47.4956, -122.4359)
# for restroom in data:
#     print(restroom)