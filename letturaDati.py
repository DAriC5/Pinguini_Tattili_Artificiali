#import RPi.GPIO as GPIO  # Importa la libreria per controllare i GPIO della Raspberry Pi
import time  # Importa la libreria per gestire i ritardi temporali
import threading, queue  # Importa le librerie per la gestione dei thread e delle code
import serial  # Importa la libreria per la comunicazione seriale

q = queue.Queue()  # Crea una coda per la comunicazione tra thread

class Read_Microbit(threading.Thread):  # Classe per leggere dati dalla porta seriale
    def __init__(self): #crea in thread
        threading.Thread.__init__(self)
        self._running = True
    
    def terminate(self):  # Ferma il thread
        self._running = False
        
    def run(self):  # Funzione principale del thread
        port = "COM15"  # Porta seriale della micro:bit
        s = serial.Serial(port)  # Inizializza la connessione seriale
        s.baudrate = 115200  # Imposta la velocità di trasmissione dati
        while True:
            data = s.readline().decode()[:-1]  # Legge e decodifica il messaggio ricevuto
            q.put(data)  # Inserisce il messaggio nella coda
            time.sleep(0.1)  # Ritardo per evitare sovraccarico

class Coda():
    #attributi dimansione massima
    def __init__(self, max_dim = 10):
        self.max_dim = max_dim
        self.coda = []
    
    def aggiungi(self, elemento):
        if len(self.coda) < self.max_dim:
            self.coda.append(elemento)

    def rimuovi(self):
        if len(self.coda) >= 1:
            return self.coda.pop(0)

def main():
    rm = Read_Microbit()  # Crea un'istanza del thread per leggere dalla micro:bit
    rm.start()  # Avvia il thread
    
    while True:        
        message = q.get()  # Legge un messaggio dalla coda
        q.task_done()  # Segnala che il messaggio è stato elaborato
        print("Arrivato")

        message = message[:-1] # Converte il messaggio in stringa
        print(f"{q.qsize()} e {message}")

    
        

if __name__ == "__main__":  # Controlla se lo script è eseguito direttamente
    main()  # Esegue la funzione principale
