import urllib.	parse, urllib.request, urllib.error, json
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
def get_events(query, ada=False, unisex=False):
    try:
        params = {
            'engine': "google_events",
            "q": query,
            "api_key": # add API key here
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
def geocode(address, ada=False, unisex=False):

    geolocator = Nominatim(user_agent="functions")
    location = geolocator.geocode(address)
    if location is None:
        return None
    return get_restroom(location.latitude, location.longitude, ada, unisex)


#accesses restroom api 
def get_restroom(latitude, longitude, ada=False, unisex=False):
    try:
        #do something with cords & geo wtv
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
        return data
    except urllib.error.HTTPError as e:
        print(e.code, e.reason)
        return []


# data = get_restroom(47.4956, -122.4359)
# for restroom in data:
#     print(restroom)