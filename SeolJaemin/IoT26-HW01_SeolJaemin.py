# IoT26-HW01_SeolJaemin.py
# 202234900 Seol Jaemin

from gpiozero import LED # or DigitalOutputDevice
from time import sleep
from signal import puase

led = LED(14) # LED is on GPIO14 = pin8

while True:
    led.toggle() # or on(), off()
    sleep(1)

    # Alternative method
    # led.blink()
    # pause()