import requests
import time

API_NYCKEL_PLATSUPPSLAG = '376ebd97e0244900bb8d52b251818b22'
API_NYCKEL_REALTIDSINFORMATION4 = 'bdb4a66d3f564776b30551afddcd2a58'
HAMMARBYHÖJDEN = '9144'
real_time_departures = 'https://api.sl.se/api2/realtimedeparturesV4.json?key=' + \
    API_NYCKEL_REALTIDSINFORMATION4 + '&siteid=' + HAMMARBYHÖJDEN + '&timewindow=500'
NORTH = 1
sleep_time = 30

def get_departures():
    while True:        
        response = requests.get(real_time_departures)

        if response.json()['StatusCode'] > 0:
            print('Error..')
        else:
            departures = response.json()['ResponseData']['Metros']
            departure_info = []

            for departure in departures:
                if departure['JourneyDirection'] == NORTH & departure['JourneyDirection'] not in departure_info:
                    displayString = departure['LineNumber'] + ' ' + \
                        departure['Destination'] + ' ' + departure['DisplayTime']
                    departure_info.append(displayString)
            print(departure_info[0])
            sleep_time = departures[0]
            departure_string = ''
            for departure in departure_info[:4]:
                if departure != departure_info[0]:
                    departure_string += departure + '   '
            print(departure_string)
        time.sleep(30)
        
get_departures()
