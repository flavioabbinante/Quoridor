"""questo è un modulo di funzioni utili allo svolgimento del programma"""

import sys

def checkInput(input_utente):
        """
        Valida l'input del giocatore (US #57).
        Ritorna il tipo di azione o None se non valido.
        """
        # Caso muro: 3 caratteri (es. a1h)
        if len(input_utente) == 3:
            if 'a' <= input_utente[0] <= 'h':
                if '1' <= input_utente[1] <= '8':
                    if input_utente[2] == 'h' or input_utente[2] == 'v':
                        return "wall"

        # Caso movimento: 2 caratteri (es. e2)
        elif len(input_utente) == 2:
            if 'a' <= input_utente[0] <= 'i':
                if '1' <= input_utente[1] <= '8':
                    return "move"

        # Comandi speciali con slash (stile chat/console)
        elif input_utente == "/help":
            return "help"
        elif input_utente == "/quit":
            return "quit"
        elif input_utente == "/bye":
            return "bye"

        return None

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
    """permette al giocatore di uscire dal gioco e fermare il processo"""
    scelta = input("Sei sicuro di voler uscire dal gioco? (s/n): ").lower()
    if scelta == 's':
        print("\nChiusura del gioco in corso. A presto!")
        sys.exit()
    else:
        print("\nRitorno al gioco...")
