import requests
import uasyncio as asyncio

async def get_departures(station, direction):
    departure_request = 'https://transport.integration.sl.se/v1/sites/' + station + '/departures?transport=METRO&direction=' + direction + '&forecast=500'
    headers = {
        "Content-Type": "application/json" 
    }

    response = requests.get(departure_request, headers=headers)
    return response