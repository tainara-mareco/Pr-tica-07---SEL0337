from gpiozero import LED
from time import sleep

led = LED(13)

while True:
        led.on()
        sleep(0.8)
        led.off()
        sleep(0.8)