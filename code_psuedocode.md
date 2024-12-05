this program will search through three APIs - Refuge Restrooms, Google Events API, and Google Maps API - to identify
the location of public bathrooms during events. the aim of the project is to encourage community engagement with local
events by breaking down this barrier of not being able to find an accessible restroom, encouraging more people to discover
and engage with local events


psuedocode:
functionality 1:
1) user will input an event
2) the program will search through Google Event API to determine the events geolocational data
3) the program will then enter that data as a query for a restroom location, and then use the Refuge Restrooms API to present
the address of the nearest restrooms to the user

functionality 2 (if time permits):
1) user can allow the program to access their current location
2) using the user's geolocational data, the program will use the Refuge Restrooms API to seaerch for public bathrooms near
their current location using the Google Maps API.
notes: this functionality involves a third API. if time permits, we will attempt to integrate this third API to have a more
refined and interactive way to display our data, as well as expand upon the given functionality of the program.

output: web or mobile app
goals: help the user identify nearby bathrooms to the event's location before and during the event

refuge restrooms documentation: https://learn.microsoft.com/en-us/connectors/refugerestroomsip/
