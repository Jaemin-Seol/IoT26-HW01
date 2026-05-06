#youbin_Lim
from gpiozero import LED
from time import sleep

led = LED(14)

# blinking an LED forever
while True:
  # LED off for 1s
    led.off()
    sleep(1)

    # blink twice
    for _ in range(2):
        led.on()
        sleep(0.3)
        led.off()
        sleep(0.3)
