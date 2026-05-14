"""Gestisce la logica dei muri e del loro inserimento nella griglia."""
class Muro:
    """Rappresenta un muro da piazzare sulla scacchiera.

    Le coordinate indicano il 'Perno Centrale' (l'incrocio tra 4 celle).
    """

    def __init__(self, riga_centro: int, colonna_centro: int, orientamento: str):
        self.riga = riga_centro
        self.colonna = colonna_centro
        self.orientamento = orientamento.lower()

    def __repr__(self):
        """Restituisce una rappresentazione in stringa del muro."""
        return f"Muro(dir='{self.orientamento}', centro=({self.riga},{self.colonna}))"