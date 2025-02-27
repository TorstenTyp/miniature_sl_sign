from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd
from swedish_letters import swedify_string
import uasyncio as asyncio

display_width = 40
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, display_width)
speed = 0.2
white_space = '     '
current_task = None

async def display_departures(departures):    
    count_down = 0
    minutes_until_refresh = get_minutes_until_next_departure(departures)
    
    while count_down < minutes_until_refresh:
        if 'Nu' in departures['departures'][0]['display']:
            first_string = f"{departures['departures'][0]['line']['id']} {departures['departures'][0]['destination']}{white_space}Nu"
        else:
            first_string = f"{departures['departures'][0]['line']['id']} {departures['departures'][0]['destination']} {minutes_until_refresh - count_down} min"
        
        second_string = ''
        
        for departure in departures['departures']:
            if departure != departures['departures'][0]:
                if ':' in departure['display']:
                    second_string += f"{departure['line']['id']} {departure['destination']} {departure['display']}{white_space}"
                if 'Nu' in departure['display']:
                   second_string += f"{departure['line']['id']} {departure['destination']} Nu{white_space}"
                if 'min' in departure['display']:
                    minutes = int(departure['display'][:-4])
                    second_string += f"{departure['line']['id']} {departure['destination']} {minutes - count_down} min{white_space}"
        
        if '-' in second_string:
            return
        second_string = second_string[:-4]
        show_first_string(first_string)
        lcd.move_to(0, 1)
        second_string = swedify_string(second_string)
        
        global current_task
        if current_task and not current_task.done():
            current_task.cancel()
         
        current_task = asyncio.create_task(show_second_string(second_string))
             
        count_down = count_down + 1
        await asyncio.sleep(60)
        
def show_first_string(first_string):
    lcd.clear()
    lcd.move_to(0, 0)
    first_string = first_string[:-6] + (' ' * (display_width - len(first_string[:-6]) - 6)) + first_string[-6:]
    first_string = swedify_string(first_string)
    lcd.putstr(first_string)
 
async def show_second_string(original_string):
    while True:
        for i in range(len(original_string) + 1):
            shifted_string = original_string[i:] + ' ' * i
            lcd.move_to(0, 1)
            lcd.putstr(shifted_string[:display_width])
            await asyncio.sleep(speed)

        empty_space = ' ' * display_width
        for i in range(len(original_string) + 1):
            concatenated_string = empty_space + original_string
            concatenated_string = concatenated_string[i:]
            lcd.move_to(0, 1)
            lcd.putstr(concatenated_string[:display_width])
            await asyncio.sleep(speed)

def get_minutes_until_next_departure(departures):
    if ':' in departures['departures'][0]['display']:
        minutes_until_refresh = 10
    if 'Nu' in departures['departures'][0]['display']:
        minutes_until_refresh = 1
    if 'min' in departures['departures'][0]['display']:
        minutes_until_refresh = int(departures['departures'][0]['display'][:-4])
    return minutes_until_refresh