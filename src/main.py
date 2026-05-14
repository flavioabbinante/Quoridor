from os import system

from rich import print

from griglia.cella import Cella
from griglia.griglia import Griglia
from pedone.pedone import Pedone
from ui.ui import UI
from utility import utility as util
from muro.muro import Muro


class Main:

    def __init__(self):
        """Costruttore della classe Main, inizializza le componenti principali del gioco."""
        self.ui = UI()
        self.griglia = Griglia()
        self.p1 = Pedone("P2","red",Cella(0,8),16)
        self.p2 = Pedone("P1","blue",Cella(16,8),0)

    def run(self):
        """Avvia il gioco, mostrando il menu iniziale."""
        print("[bold green]Benvenuto nel gioco del Quoridor![/bold green]\n")
        system("pause")
        system("cls")
        menuIniziale = ""
        while menuIniziale != "1":
            self.ui.menuIniziale()
            menuIniziale = input("Seleziona un'opzione: ")
            if menuIniziale == "1": # Qui si gestisce la nuova partita
                self.partita() # Inizio della nuova partita

            elif menuIniziale == "2": # Regole del gioco
                self.ui.mostraRegole()
                system("pause")
                system("cls")

            elif menuIniziale == "3": # Autori del progetto
                self.ui.crediti()
                system("pause")
                system("cls")
            elif menuIniziale == "0":
                util.esciGioco() # Esco dal gioco e fermo il processo
            else:
                self.ui.erroreMsg("Opzione non valida. Riprova.")
                system("pause")
                system("cls")

    def partita(self):

        """Gestisce il loop di una partita, alternando i turni dei giocatori e verificando le condizioni di vittoria."""

        turno = 1
        
        while not self.p1.checkVittoria() and not self.p2.checkVittoria():
            self.ui.printGriglia(self.griglia.matrice, [self.p1, self.p2])
            
            if turno % 2 != 0:
                currPedone = self.p1
            else:
                currPedone = self.p2
                
            self.ui.mostraTurno(currPedone)
            
            mossaCompletata = False
            while not mossaCompletata:
                scelta = input("Mossa da effettuare [/help per visualizzare i comandi]: ").lower()
                esito = self.eseguiMossa(scelta, currPedone)
                
                if esito == "quit":
                    vincitore = util.abbandonaPartita(turno)
                    self.ui.schermataVittoria(vincitore)
                    return
                
                if esito == True:
                    mossaCompletata = True
            
            turno += 1
            
        if self.p1.checkVittoria():
            vincitore = self.p1.getNome()
        else:
            vincitore = self.p2.getNome()
            
        self.ui.schermataVittoria(vincitore)


        
        turno += 1

if __name__ == "__main__":
    main = Main()
    main.run()
