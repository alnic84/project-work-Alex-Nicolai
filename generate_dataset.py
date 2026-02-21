 
import random 
import pandas as pd 
  
NUM_TICKETS = 500 
  
# Vocabolari semantici per categoria 
vocabolario = { 
    "Amministrazione": [ 
        ["fattura","documento","ricevuta","nota contabile"], 
        ["pagamento","saldo","versamento","transazione"], 
        ["rimborso","credito","restituzione"], 
        ["scadenza","termine","data limite"] 
    ], 
    "Tecnico": [ 
        ["errore","anomalia","malfunzionamento","problema"], 
        ["accesso","login","autenticazione"], 
        ["server","sistema","piattaforma"], 
        ["blocco","interruzione","crash"] 
    ], 
    "Commerciale": [ 
        ["offerta","proposta","promozione"], 
        ["ordine","acquisto","richiesta prodotto"], 
        ["preventivo","stima","quotazione"], 
        ["contratto","abbonamento","piano"] 
    ] 
} 
  
intro = [ 
    "Buongiorno, segnalo che", 
    "Salve, avrei bisogno di assistenza perché", 
    "Non riesco a capire perché", 
    "Scrivo per segnalare che", 
    "Potete verificare perché", 
    "Avrei necessità di sapere perché", 
    "Vorrei chiarimenti dato che", 
    "Si è verificato il seguente problema:", 
    "Gentile supporto,", 
    "Chiedo supporto in quanto" 
] 
  
ending = [ 
    "potete controllare?", 
    "attendo riscontro", 
    "grazie", 
    "resto in attesa", 
    "potete aiutarmi?", 
    "fatemi sapere", 
    "serve supporto", 
    "quando possibile", 
    "appena potete", 
    "grazie mille" 
] 
  
rumore = ["", "", "", " gentilmente", " appena possibile", " per favore"] 
  
def assegna_priorita(testo): 
    testo = testo.lower() 
  
    alta = ["urgente","impossibile","blocco","crash","non funziona"] 
    media = ["problema","errore","verifica","accesso"] 
  
    if any(w in testo for w in alta): 
        return "alta" 
    elif any(w in testo for w in media): 
        return "media" 
    else: 
        return random.choice(["bassa","media"]) 
  
  
data = [] 
  
for i in range(1, NUM_TICKETS+1): 
  
    categoria = random.choice(list(vocabolario.keys())) 
  
    # parola principale 
    gruppo = random.choice(vocabolario[categoria]) 
    parola = random.choice(gruppo) 
  
    # 🔁 sovrapposizione semantica (rende il task realistico) 
    if random.random() < 0.30: 
        categoria_alt = random.choice(list(vocabolario.keys())) 
        gruppo = random.choice(vocabolario[categoria_alt]) 
        parola = random.choice(gruppo) 
  
    # Titolo realistico 
    title_templates = [ 
        f"Problema relativo a {parola}", 
        f"Richiesta su {parola}", 
        f"Verifica {parola}", 
        f"Segnalazione {parola}", 
        f"Informazioni su {parola}" 
    ] 
    title = random.choice(title_templates) 
  
    # Corpo testo realistico 
    body = f"{random.choice(intro)} {parola}{random.choice(rumore)}. {random.choice(ending)}." 
  
    priorita = assegna_priorita(body) 
  
    data.append([i, title, body, categoria, priorita]) 
  
# dataframe 
df = pd.DataFrame(data, columns=["id","title","body","category","priority"]) 
  
# salva csv 
df.to_csv("dataset_tickets.csv", index=False, encoding="utf-8") 
  
print(f"Dataset generato correttamente con {NUM_TICKETS} ticket.") 
 
