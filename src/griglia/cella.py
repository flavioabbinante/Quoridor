""" Gestisce le singole celle della griglia """
class Cella:
    """
    Rappresenta una singola casella fisica sulla scacchiera.
    Viene utilizzata per tracciare la posizione dei pedoni.
    """
    def __init__(self, riga: int, colonna: int):
        # Coordinate riferite alla matrice 17x17 (saranno sempre numeri pari per le caselle)
        self.riga = riga
        self.colonna = colonna

    def __repr__(self):
        return f"Cella(r={self.riga}, c={self.colonna})"
        
    def __eq__(self, other):
        if isinstance(other, Cella):
            return self.riga == other.riga and self.colonna == other.colonna
        return False