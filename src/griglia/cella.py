"""Gestisce le singole celle della griglia."""
class Cella:
    """Rappresenta una singola casella fisica sulla scacchiera.
    
    Viene utilizzata per tracciare la posizione dei pedoni.
    """

    def __init__(self, riga: int, colonna: int):
        """Inizializza una cella con le coordinate specificate.
        
        Args:
            riga: Indice di riga della cella (numero pari nella matrice 17x17)
            colonna: Indice di colonna della cella (numero pari nella matrice 17x17)

        """
        # Coordinate riferite alla matrice 17x17 
        # (saranno sempre numeri pari per le caselle)
        self.riga = riga
        self.colonna = colonna

    def __repr__(self):
        """Restituisce una rappresentazione stringa della cella.
        
        Returns:
            Stringa nel formato "Cella(r=riga, c=colonna)"

        """
        return f"Cella(r={self.riga}, c={self.colonna})"
        
    def __eq__(self, other):
        """Confronta due celle verificando se hanno le stesse coordinate.
        
        Args:
            other: Oggetto da confrontare con questa cella
            
        Returns:
            True se other è una Cella con stesse coordinate, False altrimenti

        """
        if isinstance(other, Cella):
            return self.riga == other.riga and self.colonna == other.colonna
        return False