from flask import Flask, render_template, request
import	urllib.	parse, urllib.request, urllib.error, json, pprint

app = Flask(__name__)
#METHOD 2
#index method to initalize homepage
@app.route('/')
def index():
    return render_template('base.html') #the css formatting for the homepage will be defined in the base.html file

#METHOD 2
#method to collect locational query from user
@app.route('/data-entry', methods=['GET', 'POST'])
def dataEntry():
    if request.method == 'POST':
        query = request.form.get('query')
        sort = 'sort' in request.form
        return str(query) + str(sort)
    return render_template('base.html', query=query, sort=sort)
    # return render_template('data_entry_results.html', query=query, sort=sort)

#provides spaces for the user to input their search parameter data
#location query (text box)
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

