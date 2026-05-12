import numpy as np

from .cella import Cella
from src.muro.muro import Muro

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

    def passaggio_libero(self, cella_partenza, cella_destinazione):
        """
        Verifica se c'è un muro tra due celle adiacenti.
        Restituisce True se si può passare, False se c'è un muro.
        """
        riga_mezzo = (cella_partenza.riga + cella_destinazione.riga) // 2
        col_mezzo = (cella_partenza.colonna + cella_destinazione.colonna) // 2
        
        
        if self.matrice[riga_mezzo, col_mezzo] == 1:
            return False # Muro
        else:
            return True  # Libero
        


def piazza_muro(self, muro: Muro) -> bool:
        """
        Tenta di piazzare un Muro nella matrice NumPy espandendolo dal centro.
        Restituisce True se ha successo, False se illegale.
        """
        indici_da_occupare = []
        r = muro.riga
        c = muro.colonna


        #Aggiunta muro orizzontale ('h')
        if muro.orientamento == 'h':
            indici_da_occupare = [
                (r, c - 1),(r, c),(r, c + 1)   
            ]
        elif muro.orientamento == 'v': #Aggiunta muro verticale ('v')
            indici_da_occupare = [
                (r - 1, c),(r, c),(r + 1, c)
            ]
            
        # 2. Controllo Collisioni
        for rind, cind in indici_da_occupare:
            if rind < 0 or rind >= 17 or cind < 0 or cind >= 17:
                return False
            
            if self.matrice[rind, cind] == 1:
                return False 
                
        # 3. Piazzamento effettivo 
        for rind, cind in indici_da_occupare:
            self.matrice[rind, cind] = 1
            
        return True