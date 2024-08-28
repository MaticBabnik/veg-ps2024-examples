import network
from microdot import Microdot, Response
from microdot.utemplate import Template
from random import randint
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
Template.initialize('predloge')

app = Microdot()

@app.route("/")
async def root(request):
    return Template("index.html").render(a=randint(1,1000))

app.run(port=80)
