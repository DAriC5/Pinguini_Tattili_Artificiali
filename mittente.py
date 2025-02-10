from microbit import *
import radio

radio.on()
radio.config(group=23)
    
    
while True:
    # Controlla le inclinazioni
    movimento_y = accelerometer.get_y()
    movimento_x = accelerometer.get_x()
    movimento_z = accelerometer.get_z()

    radio.send(str(movimento_y)) # casto in stringa
    display.scroll(movimento_y)  # Mostra il comando sul display
    sleep(100)
    
    radio.send(str(movimento_x)) # casto in stringa
    display.scroll(movimento_x)  # Mostra il comando sul display
    sleep(100)
    
    radio.send(str(movimento_z)) # casto in stringa
    display.scroll(movimento_z)  # Mostra il comando sul display
    sleep(100)
