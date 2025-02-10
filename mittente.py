from microbit import *
import radio

radio.on()
radio.config(group=23)
    
    
while True:
    # Controlla le inclinazioni
    movimento_y = accelerometer.get_y()
    movimento_x = accelerometer.get_x()
    movimento_z = accelerometer.get_z()

    radio.send(str(movimento_x) + "," + str(movimento_y) + "," + str(movimento_z)) # casto in stringa
    sleep(100)
