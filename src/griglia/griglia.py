import numpy as np
from .cella import Cella

class Griglia:
    """
    Gestisce la struttura dati principale del tabellone.
    Usa una matrice numpy 17x17 per tracciare muri e spazi vuoti,
    e mantiene i riferimenti agli oggetti Cella calpestabili.
    """
    def __init__(self):
        # Matrice 17x17: 0 = vuoto, 1 = muro
        self.matrice = np.zeros((17, 17), dtype=int)
        
        # Dizionario per memorizzare le 81 celle (9x9) per i pedoni
        # Chiave: tupla (riga, colonna) -> Valore: oggetto Cella
        self.celle = {}
        self._inizializza_celle()

    def _inizializza_celle(self):
        """
        Popola il dizionario con oggetti Cella.
        Nella logica 17x17, le caselle dei pedoni si trovano solo sugli indici pari.
        """
        for r in range(0, 17, 2):
            for c in range(0, 17, 2):
                self.celle[(r, c)] = Cella(r, c)

    def get_cella(self, riga: int, colonna: int) -> Cella:
        """
        Restituisce l'oggetto Cella alle coordinate richieste.
        Utile per assegnare CellaPartenza o Posizione a un Pedone.
        """
        return self.celle.get((riga, colonna), None)