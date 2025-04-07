# PINGUINI TATTICI ARTIFICIALI

## Descrizione

**PINGUINI TATTICI ARTIFICIALI** è un progetto di videogioco sviluppato per PLACEHOLDER. Il gioco incorpora intelligenza artificiale per PLACEHOLDER.

## Struttura della Repository

La repository è organizzata come segue:

- **`img/`**: Contiene immagini e risorse grafiche utilizzate nel progetto.

- **`AlberoRotazione.ipynb`**: Notebook Jupyter che esplora l'implementazione di alberi di decisione per la gestione della rotazione del personaggio nel gioco.

- **`GiocoConAI.zip`**: Archivio contenente il codice sorgente del gioco con l'integrazione dell'intelligenza artificiale.

- **`Legenda-dataset`**: File che descrive le variabili presenti nei dataset utilizzati.

- **`VideoGameDM65_2.zip`**: Versione alternativa o aggiornata del codice sorgente del gioco.

- **`concept.txt`**: Documento che illustra il concept e le idee alla base del gioco.

- **`cosaFarexAI.txt`**: Appunti sulle implementazioni e miglioramenti da apportare all'intelligenza artificiale nel gioco.

- **`dsAccellerazioneDx.csv`**, **`dsAccellerazioneSx.csv`**, **`dsRotazioneDx.csv`**, **`dsRotazioneSx.csv`**: Dataset contenenti dati di accelerazione e rotazione per l'addestramento dei modelli di IA.

- **`evirorment.py`**: Script che definisce l'ambiente di gioco.

- **`letturaDati.py`**: Script per la lettura e l'elaborazione dei dati dai dataset.

- **`mittenteFinale.py`**: Script responsabile dell'invio dei dati elaborati.

- **`modello_accellerazioniDx.joblib`**, **`modello_accellerazioniSx.joblib`**, **`modello_rotazioniDx.joblib`**, **`modello_rotazioniSx.joblib`**: Modelli di machine learning pre-addestrati per prevedere le accelerazioni e le rotazioni.

- **`movimenti.txt`**: File contenente informazioni sui movimenti implementati nel gioco.

- **`provaAlbero.ipynb`**: Notebook Jupyter per testare e visualizzare l'output degli alberi di decisione.

- **`riceventeFinale.py`**: Script che gestisce la ricezione dei dati nel gioco.

## Requisiti

Per eseguire il progetto, assicurati di avere installato:

- Python 3.x
- Librerie: `numpy`, `pandas`, `scikit-learn`, `matplotlib`, `joblib`

## Installazione

1. Clona questa repository in locale:

   ```bash
   git clone https://github.com/DAriC5/videogiocoDM65.git
   ```

2. Accedi alla directory del progetto:

   ```bash
   cd videogiocoDM65
   ```

3. Installa le dipendenze richieste (se presente un file requirements):

   ```bash
   pip install -r requirements.txt
   ```

   > Se non c'è un file `requirements.txt`, puoi installare manualmente le librerie con:

   ```bash
   pip install numpy pandas scikit-learn matplotlib joblib
   ```

## Utilizzo

1. Addestra o carica i modelli di machine learning inclusi (`*.joblib`).
2. Esegui lo script `riceventeFinale.py` per avviare il ricevitore del sistema di controllo.
3. Esegui `evirorment.py` per avviare il gioco vero e proprio.
4. Puoi utilizzare i notebook `.ipynb` per esplorare i dataset e visualizzare l'albero di decisione utilizzato.

## Contributi

Contributi e suggerimenti sono benvenuti! Apri una Pull Request descrivendo le tue modifiche suggerite

## Licenza

Questo progetto è distribuito sotto la licenza MIT. Vedi il file `LICENSE` per maggiori dettagli.

## Contatti

Per ulteriori informazioni o domande:

- Email: arianna.dutto@itiscuneo.edu.it
         - matteo.dutto.i@itiscuneo.edu.it
         - michele.tuberga@itiscuneo.edu.it
         - tommaso.spada@itiscuneo.edu.it

- GitHub: [DAriC5](https://github.com/DAriC5)
          - [maatteodutto](https://github.com/maatteodutto)
          - [micheletuberga](https://github.com/micheletuberga)
          - [TommySpadaITIS](https://github.com/TommySpadaITIS)
