"""Gestisce il pedone e le azioni che può compiere"""
from typing import Literal

from griglia.cella import Cella

class Pedone:
    def __init__(self, nome: str, colore: Literal["red", "blue"], cellaPartenza: Cella, obiettivo: int):
        """Costruttore della classe Pedone.
        
        Args:
            nome: Nome del pedone
            colore: Colore del pedone ('Red', 'Blue')
            cellaPartenza: Cella di partenza
            posizione: Posizione attuale
            obiettivo: Obiettivo da raggiungere
        """
        self.nome = nome
        self.colore = colore
        self.cellapartenza = cellaPartenza
        self.posizione = cellaPartenza
        self.muri = 10
        self.obiettivo = obiettivo

    def __repr__(self):
        return f"Pedone(n={self.nome}, c={self.colore}, cp={self.cellapartenza}, pos={self.posizione}, muri={self.muri}, obiettivo={self.obiettivo})"

    def getNome(self):
        """Restituisce il nome del pedone."""
        return self.nome
    
    def getColore(self):
        """Restituisce il colore del pedone."""
        return self.colore
    
    def getCellaPartenza(self):
        """Restituisce la cella di partenza."""
        return self.cellapartenza
    
    def getPosizione(self):
        """Restituisce la posizione attuale."""
        return self.posizione
    
    def getMuri(self):
        """Restituisce il numero di muri rimanenti."""
        return self.muri
    
    def getObiettivo(self):
        """Restituisce l'obiettivo da raggiungere."""
        return self.obiettivo


    def muoviPedone(self, posizione: Cella):
        """Muove il pedone nella posizione specificata.
        
        Args:
            posizione: Posizione di destinazione
        """
        self.posizione = posizione


    def usaMuro(self):
        """Usa un muro e lo decrementa dal contatore.
        
        Returns:
            True se il muro è stato usato, 'Muri esauriti' se non ci sono muri disponibili
        """
        if self.muri > 0:
            self.muri -= 1
            return True
        else:
            return "Muri esauriti"  #TODO: aggiungere Errore UI
        
    def checkVittoria(self) -> bool:
        """Controlla se il pedone ha raggiunto l'obiettivo.

        Returns:
            bool: True se il pedone ha raggiunto la riga obiettivo, False altrimenti.
        """
        if self.posizione.riga == self.obiettivo:
            return True
        
        return False
