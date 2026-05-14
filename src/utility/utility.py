"""questo è un modulo di funzioni utili allo svolgimento del programma"""

import sys
import os

def checkInput(input_utente):
        """
        Valida l'input del giocatore.
        Ritorna il tipo di azione o None se non valido.
        """
        # Caso muro: 3 caratteri (es. a1h)
        if len(input_utente) == 3:
            if 'a' <= input_utente[0] <= 'h':
                if '1' <= input_utente[1] <= '9':
                    if input_utente[2] == 'h' or input_utente[2] == 'v':
                        return "wall"

        # Caso movimento: 2 caratteri (es. e2)
        elif len(input_utente) == 2:
            if 'a' <= input_utente[0] <= 'i':
                if '1' <= input_utente[1] <= '9':
                    return "move"

        # Comandi speciali con slash (stile chat/console)
        elif input_utente == "/help":
            return "help"
        elif input_utente == "/quit":
            return "quit"
        elif input_utente == "/bye":
            return "bye"

        return None

def convertiCoordinate(scelta: str, tipoAzione: str):
    """
    Converte l'input testuale nelle coordinate della matrice di gioco.
    
    Args:
        scelta: Stringa della mossa inserita dall'utente.
        tipoAzione: Tipo di azione da eseguire ('move' o 'wall').
    
    Returns:
        Tupla (riga, colonna) con le coordinate calcolate, oppure (None, None) se l'azione non è supportata.
    """
    if tipoAzione not in ("move", "wall"):
        return None, None
        
    c = (ord(scelta[0]) - 97) * 2
    r = (9 - int(scelta[1])) * 2
    
    if tipoAzione == "wall":
        c += 1
        r += 1
        
    return r, c

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


def clearScreen():
    """Pulisce lo schermo"""
    os.system('cls' if os.name == 'nt' else 'clear')


def waitKey():
    """Mette in pausa attendendo un input dell'utente"""
    if os.name == 'nt':
        os.system('pause')
    else:
        input("Premi invio per continuare...")
