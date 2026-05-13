"""questo è un modulo di funzioni utili allo svolgimento del programma"""


def checkInput(input: str):
    """controlla che l'input sia corretto e che segua un certo ordine"""
    pass

def abbandonaPartita(turno):
    """permette al giocatore di abbandonare la partita in corso"""
    if turno % 2 == 0:
        print("P2 ha abbandonato")
        vincitore = "P1"
    else:
        print("P1 ha abbandonato")
        vincitore = "P2"
        
    return vincitore


def esciGioco():
    """permette al giocatore di uscire dal gioco"""
    pass
