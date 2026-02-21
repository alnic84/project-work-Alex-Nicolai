\# 🎫 Classificatore Automatico di Ticket con Machine Learning



Questo progetto nasce come \*\*project work universitario\*\* con l’obiettivo di sviluppare un prototipo minimale e riproducibile per la \*\*classificazione automatica dei ticket aziendali\*\*.  

Il sistema riceve in input un testo breve composto da \*titolo\* e \*descrizione\* del ticket, e restituisce in output la \*\*categoria operativa\*\* (Amministrazione, Tecnico, Commerciale) e la \*\*priorità suggerita\*\* (Bassa, Media, Alta).  

L’intero progetto è stato realizzato in \*\*Python\*\*, utilizzando tecniche di machine learning di base e privilegiando la chiarezza del codice e la semplicità del flusso.



---



\## 🧩 Struttura del progetto



&nbsp;   ticket-classifier-ml/

&nbsp;   ├── generate\_dataset.py      → Generatore di dataset sintetico di ticket

&nbsp;   ├── train\_models.py          → Addestramento modelli ML e valutazione risultati

&nbsp;   ├── dashboard.py             → Dashboard interattiva Streamlit

&nbsp;   ├── dataset\_tickets.csv      → Dataset sintetico generato (titolo, descrizione, categoria, priorità)

&nbsp;   ├── requirements.txt         → Librerie necessarie

&nbsp;   └── README.md                → Documentazione del progetto



---



\## ⚙️ Fasi del progetto



\### 1️⃣ Generazione del dataset sintetico

Il dataset è stato creato artificialmente per simulare ticket aziendali realistici in tre ambiti operativi:

\- \*\*Amministrazione\*\*: richieste su fatture, pagamenti e rimborsi;

\- \*\*Tecnico\*\*: segnalazioni di errori, malfunzionamenti e assistenza IT;

\- \*\*Commerciale\*\*: domande su offerte, ordini e preventivi.  



Ogni ticket è composto da un titolo e una descrizione.  

La priorità viene assegnata in base a parole chiave:  

\- \*errore\*, \*bloccante\*, \*urgente\* → priorità alta  

\- \*verifica\*, \*richiesta\*, \*controllo\* → priorità media  

\- frasi neutre → priorità bassa  



Output del file: `dataset\_tickets.csv`  

(colonne: `id, title, body, category, priority`)



---



\### 2️⃣ Pipeline di Machine Learning

Il modello utilizza una pipeline di classificazione testuale basata su:

\- \*\*Pulizia e normalizzazione del testo\*\* (minuscole, rimozione punteggiatura);

\- \*\*Vettorizzazione TF-IDF\*\* per trasformare i testi in rappresentazioni numeriche;

\- \*\*Regressione Logistica\*\* per classificare categoria e priorità.  



Valutazione:

\- Suddivisione train/test 80/20;  

\- Metriche: \*accuracy\* e \*F1-score\* macro;  

\- Visualizzazione dei risultati con \*\*matrice di confusione\*\* e \*\*grafico a barre per classe\*\*.



Output del file:  

\- `model\_cat.pkl` → modello per categoria  

\- `model\_pri.pkl` → modello per priorità  

\- `vectorizer\_cat.pkl` e `vectorizer\_pri.pkl` → vettorizzatori TF-IDF  



---



\### 3️⃣ Dashboard interattiva

La dashboard, sviluppata con \*\*Streamlit\*\*, permette di:

\- Inserire titolo e descrizione di un nuovo ticket e ottenere categoria e priorità previste;

\- Visualizzare le \*\*5 parole più influenti\*\* nella decisione del modello;

\- Caricare un file CSV contenente più ticket e ottenere un file di output con le predizioni in blocco.  



Per avviarla:

```bash

streamlit run dashboard.py



