import network
from machine import Pin
from microdot import Microdot, Response
from time import sleep

# povezava na WiFi
wifi_ssid = "Vegova110"
wifi_geslo = "vegova24"

s = network.WLAN(network.STA_IF)
s.active(True)
s.connect(wifi_ssid, wifi_geslo)

while not s.isconnected():
    print("Se povezuje")
    sleep(0.5)

print(f"Povezano, {s.ifconfig()[0]}")


Response.default_content_type = "text/html"

app = Microdot()

@app.route("/")
async def root(rq):
    return '<h1>Hello world</h1>'

app.run(port=80)

