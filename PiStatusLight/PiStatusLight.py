import time
import rpi_ws281x
import json
from rpi_ws281x import Color

#get json file

ledStatusFile = open('ledStatusFile.json')

ledStatus = json.load(ledStatusFile)

LightsOnTime = 1 #in Seconds
TimeBetweenFlash = 4 #in seconds, set to 0 to have lights always be on

ProgramRunTime = 30 #in days, if negative will be infinite

# LED strip configuration:
LED_COUNT = 10        # Number of LED pixels.
LED_PIN = 21          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0   

strip = rpi_ws281x.PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

def SetAll(color): #color = [0,0,0]
    for i in range(LED_COUNT):
        print('DeBug: 1')
        print(color)
        strip.setPixelColor(i, Color(color[0], color[1], color[2]))
    strip.show()

def SetJSONToStrip(ledStatus): #takes the data from the json file as argument and sets strip to the RGB values
    for i in range(len(ledStatus[0])):
        print('Set Loop: ', i)
        try:
            print('DeBug: 2')
            print(ledStatus[0][i])
            strip.setPixelColor(i, Color(ledStatus[0][i][0], ledStatus[0][i][1], ledStatus[0][i][2]))
        except Exception as e:
            print(e)
    strip.show()

runSeconds = (ProgramRunTime * 24 * 60 * 60)

endTime = round(time.time()) + runSeconds#end time in unix time
ledStatus[1][0] = endTime
json_object = json.dumps(ledStatus, indent = 4)
with open('ledStatusFile.json', 'w') as f:
    f.write(json_object)
    f.close()

if ProgramRunTime > 0:
    while True:
        ledStatusFile = open('ledStatusFile.json')
        ledStatus = json.load(ledStatusFile)
        if time.time() < ledStatus[1][0]:
            SetJSONToStrip(ledStatus)
            time.sleep(LightsOnTime)
            SetAll((0,0,0))#turn Strip Off
            time.sleep(TimeBetweenFlash)
        else:
            break
else:
    while True:
        SetJSONToStrip(ledStatus)
        time.sleep(LightsOnTime)
        SetAll((0,0,0))#turn Strip Off
        time.sleep(TimeBetweenFlash)
