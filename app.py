from flask import Flask
import	urllib.	parse, urllib.request, urllib.error, json, pprint

#flask development here

app = Flask(__name__)
#METHOD 2
#index method to initalize homepage
@app.route('/')
def index():
    return render_template('base.html') #the css formatting for the homepage will be defined in the base.html file

#METHOD 2
#method to collect locational query from user
@app.route('/')
def dataEntry():
    query = request.form.get('query')
    sort = 'sort' in request.form
#provides spaces for the user to input their search parameter data
#location queery (text box)
# optional language (drop down menu? )


#possible method?
# allow user to choose event based on query results.
@app.route('/search', methods=['POST'])
def search_events():
    query = request.form.get('event_query')
    language = request.form.get('language', 'en')
    api_key = request.form.get('api_key', '')  #supplied by user
    events = get_events(query, language, api_key)
    return render_template('search_results.html', events=events)

#METHOD 3
#method to connect query search results from selected event
#@app


#connects secondary html page selection (METHOD 2) to avalible nearby restrooms
#presents a list of restrooms nearby geolocational data.
# should use python api call
#

# def get_restrooms(latitude, longitude):
#     try:
#         url = f"https://www.refugerestrooms.org/api/v1/restrooms/by_location?lat={latitude}&lng={longitude}"
#         req = urllib.request.Request(url)
#         response = urllib.request.urlopen(req)
#         response_str = response.read().decode('utf-8')
#         data = json.loads(response_str)
#         return data
#     except urllib.error.HTTPError as e:
#         print(f"HTTPError: {e.code} - {e.reason}")
#         return []

