from microbit import *
import radio

radio.on()
radio.config(group=23)
    
    
while True:
    # Controlla le inclinazioni
    movimento_y = accelerometer.get_y()
    movimento_x = accelerometer.get_x()
    movimento_z = accelerometer.get_z()

    radio.send(f"{movimento_x:.3f}, {movimento_y:.3f}, {movimento_z:.3f}") # casto in stringa
    sleep(100)
