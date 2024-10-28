from wifi_connector import connect_to_wifi
from departures import get_departures
from display import display_departures, get_minutes_until_next_departure
import config
import uasyncio as asyncio

wifi_name = config.WIFI_NAME
wifi_password = config.WIFI_PASSWORD
station = str(config.station_dictionary.get(config.STATION))
direction = config.DIRECTION

connect_to_wifi(wifi_name, wifi_password)

async def main():
    while True:
        print('Fetching departures..')
        current_departures = await get_departures(station, direction)
        current_departures = current_departures.json()
        asyncio.run(display_departures(current_departures))
    
asyncio.run(main())