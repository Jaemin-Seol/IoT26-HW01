# gpiozero: controls raspberrypi pins
from gpiozero import LED
from time import sleep
from signal import pause

# led assign gpio pin 14
led = LED(14)

# blink 10 times: 1s on, 1s off. running in background
led.blink(on_time=1, off_time=1, n=10, background=True)

# keeps the process alive while the led blinks in the background
pause()

