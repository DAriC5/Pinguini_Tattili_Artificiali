from microbit import *
import radio
radio.on()
radio.config(group=23)


while True:
    display.show(Image.HEART)
    message = radio.receive()
    if message:
        print(message)
    sleep(50)
