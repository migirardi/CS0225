import datetime

def assistente_virtuale(comando):
    comando = comando.lower().strip()
    if comando == "qual è la data di oggi?":
        oggi = datetime.date.today()
        risposta = "La data di oggi è " + oggi.strftime("%d/%m/%Y")
    elif comando == "che ore sono?":
        ora_attuale = datetime.datetime.now().time()
        risposta = "L'ora attuale è " + ora_attuale.strftime("%H:%M")
    elif comando == "come ti chiami?":
        risposta = "Mi chiamo Assistente Virtuale"
    else:
        risposta = "Non ho capito la domanda."
    return risposta

def opzioni():
    print("Opzioni disponibili:")
    print("Qual è la data di oggi?")
    print("Che ore sono?")
    print("Come ti chiami?")
    
print("Ciao sono il tuo Assistente Virtuale,\npotrò esserti utile in svariati modi!\n")
opzioni()
while True:
    comando_utente=input("\nQuale azione vuoi farmi svolgere?\n\nScrivi 'esci' se vuoi chiudere.\n\n")
    if comando_utente.lower() == "esci":
        print("Arrivederci!")
        break
    else:
        print(assistente_virtuale(comando_utente))