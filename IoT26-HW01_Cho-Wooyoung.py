from gpiozero import LED
from time import sleep
from signal import pause

led = LED(14)

led.blink(on_time=1, off_time=1, n=10, background=True)

pause()


