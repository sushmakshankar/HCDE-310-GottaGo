from flask import Flask, render_template, request
import	urllib.	parse, urllib.request, urllib.error, json, pprint 
from code import get_events, geocode, get_restroom

app = Flask(__name__)

#index method to initalize homepage
#the css formatting for the homepage will be defined in the base.html file
@app.route('/')
def index():
    return render_template('index.html')


#provides spaces for the user to input their search parameter data
#location query (text box)
# allow user to choose event based on query results.
@app.route('/search', methods=['GET'])
def search_events():
    if request.method == 'GET':
        query = request.form.get('event_query')
        events = get_events(query)
    else: 
        events = []
    return render_template('search_results.html', events=events)


#method to connect query search results from selected event
# OLD METHOD
# @app.route('/search',  methods=['GET', 'POST'])
# def corresponding_restrooms():
#     if request.method == 'POST':
#         addy = request.form.get('event_location')
#         ada = 'ada' in request.form
#         unisex = 'unisex' in request.form
#         b_rooms = geocode(addy, ada, unisex)
#     else:
#         b_rooms = []
#     return render_template('bathroom_results.html', restrooms=b_rooms)

# UPDATED METHOD
@app.route('/bathroom_results', methods=['GET'])
def corresponding_restrooms():
    event_id = request.args.get('event_id')
    event_name = request.args.get('event_name')
    ada = request.args.get('ada') == 'false' # set to false from default?
    unisex = request.args.get('unisex') == 'false'

    if event_id and event_name:
        b_rooms = geocode(event_id, ada, unisex)
    else:
        b_rooms = []
    return render_template('bathroom_results.html', restrooms=b_rooms, event_name=event_name)

#connects secondary html page selection (METHOD 2) to avalible nearby restrooms
#presents a list of restrooms nearby geolocational data.
# should use python api call
