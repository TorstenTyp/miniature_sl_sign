import network
import machine

led_pin = machine.Pin("LED", machine.Pin.OUT)

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print("Connecting to WiFi...")
        wlan.active(True)
        wlan.connect(ssid, password)
        led_pin.on()
        while not wlan.isconnected():
            pass
    led_pin.off()
    print("Connected on:", wlan.ifconfig()[0])