"""questo è un modulo di funzioni utili allo svolgimento del programma"""


def checkInput(input: str):
    """controlla che l'input sia corretto e che segua un certo ordine"""
    pass

def abbandonaPartita():
    """permette al giocatore di abbandonare la partita in corso"""
    scelta = input(f"{turno_attuale}, vuoi davvero abbandonare la partita? (s/n): ").lower()
    if scelta == 's':
        vincitore = "Giocatore 2" if turno_attuale == "Giocatore 1" else "Giocatore 1"
        print(f"Il {turno_attuale} ha abbandonato.")
        print(f"Vincitore: {vincitore}!")
        return True
    else:
        return False

def esciGioco():
    """permette al giocatore di uscire dal gioco"""
    pass
