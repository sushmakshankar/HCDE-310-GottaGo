import	urllib.	parse, urllib.request, urllib.error, json, pprint


#API 1 Status: works :)
def get_restroom():
    try:
        url = "https://www.refugerestrooms.org/api/v1/restrooms"
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

data = get_restroom()
#^^Works >:)




#API 2: Status: Works :)
def get_event():
    try:
        params = {
            "engine": "google_events",
            "q": "Events in Austin",
            "hl": "en",
            "gl": "us",
            "api_key": ""
        }

        base_url = "https://serpapi.com/search.json"

        url = f"{base_url}?{urllib.parse.urlencode(params)}"
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        response_str = response.read().decode('utf-8')
        data = json.loads(response_str)
        print(data)
        return data
    except urllib.error.HTTPError as e:
        print(e.code, e.reason)
        return data


data = get_event()