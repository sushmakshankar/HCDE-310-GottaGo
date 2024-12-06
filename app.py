from flask import Flask, render_template, request
import	urllib.parse, urllib.request, urllib.error, json, pprint
from urllib.parse import unquote
from code import get_events, geocode, get_restroom

app = Flask(__name__)

#index method to initialize homepage
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
        query = request.form.get('event')
        ada = request.args.get('ada', 'false').lower() == 'true'
        unisex = request.args.get('unisex', 'false').lower() == 'true'
        events = get_events(query, ada, unisex)
    else:
        events = []
    return render_template('search_results.html', events=events, query=query)


# UPDATED METHOD for rendering bathroom results list. 
@app.route('/bathroom_results', methods=['GET'])
def corresponding_restrooms():
    event_address = request.args.get('event_address')
    event_name = request.args.get('event_name')
    
    event_addy = unquote(event_address)
    if event_addy and event_name:
        b_rooms = geocode(event_address)
    else:
        b_rooms = []
    return render_template('bathroom_results.html', restrooms=b_rooms, event_name=event_name)
