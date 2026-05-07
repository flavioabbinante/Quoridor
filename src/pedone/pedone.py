"""Gestisce il pedone e le azioni che può compiere"""

class Pedone:
    "costruttore della classe pedone"
    def __init__(self, nome, cellaPartenza, posizione, obiettivo):
        self.nome = nome
        self.cellapartenza = cellaPartenza
        self.posizione = posizione
        self.muri = 10
        self.obiettivo = obiettivo

    def __repr__(self):
        return f"Pedone(n={self.nome}, cp={self.cellapartenza}, pos={self.posizione}, muri={self.muri}, obiettivo={self.obiettivo})"
    
    "getters"
    def getNome(self):
        return self.nome
    
    def getCellaPartenza(self):
        return self.cellapartenza
    
    def getPosizione(self):
        return self.posizione
    
    def getMuri(self):
        return self.muri
    
    def getObiettivo(self):
        return self.obiettivo
    

    "setter posizione"
    def setPosizione(self, nuovaPosizione):
        self.posizione = nuovaPosizione


    "metodo per muovbere il pedone"
    def muoviPedone(self, direzione):
        if direzione == "su":
            self.posizione.riga -= 1
        elif direzione == "giu":
            self.posizione.riga += 1
        elif direzione == "sinistra":
            self.posizione.colonna -= 1
        elif direzione == "destra":
            self.posizione.colonna += 1
      
                
    "metodo per posizionare un muro sulla griglia"
    def usaMuro(self):
        if self.muri > 0:
            self.muri -= 1
            return True
        else:
            return "Muri esauriti"