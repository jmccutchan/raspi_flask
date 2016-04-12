from flask import Flask, render_template 
import Adafruit_DHT as dht
import Adafruit_BMP.BMP085 as BMP085
from switch import *

app = Flask(__name__)

light = Led()

@app.route("/")
def main():
   
    switch = light.read_switch()
    title = "DHT temperature and humdidity readings"
    paragraph = ["getting ambient temperature and humidity readings from the DHT22"]

    dh,dt1 = dht.read_retry(dht.DHT22, 4)
    dt = (dt1 * 1.8) + 32
    sensor = BMP085.BMP085()
    btemp1 = sensor.read_temperature()
    btemp = (btemp1 * 1.8) + 32
    bpressure = sensor.read_pressure()
    balt = sensor.read_altitude()
    slp = sensor.read_sealevel_pressure()
 
    return  render_template('index.html', switch=switch, btemp=btemp, bpressure=bpressure, balt=balt, slp=slp, dh=dh, dt=dt)
   #return 'DHT22 readings - Temp={0:0.1f} C Humidity={1:0.1f}%'.format(t,h)
   #return 'BMP180 readings - Temp = {0:0.2f} *C'.format(sensor.read_temperature())
   #return 'Pressure = {0:0.2f} Pa'.format(sensor.read_pressure())
   #return 'Altitude = {0:0.2f} m'.format(sensor.read_altitude())
   #return 'Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure())                      

@app.route("/led/<int:led_state>", methods=['POST'])
def led(led_state):
    if led_state == 0:
        light.set_led(False)
    elif led_state == 1:
        light.set_led(True)
    else:
        return ('Unknown LED state', 400)
    return ('', 204)
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8121)


