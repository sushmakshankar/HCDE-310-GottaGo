# Test file for the apis.
import	urllib.	parse, urllib.request, urllib.error, json, pprint

#API 1 Status: works :)
def get_restroom():
    try:
        url = "https://www.refugerestrooms.org/api/v1/restrooms" #
        url = f"{url}"
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        response_str = response.read().decode('utf-8')
        data = json.loads(response_str)
        print(data)
        return data
    except urllib.error.HTTPError as e:
        print(e.code, e.reason)
        return


#API 2: Status: Works :)
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
        a = data["events_results"]
        return a
    except urllib.error.HTTPError as e:
        print(e.code, e.reason)
        return []


data = get_events('events in Seattle')
print(data)