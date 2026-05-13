from os import system

from rich import print

from griglia.cella import Cella
from griglia.griglia import Griglia
from pedone.pedone import Pedone
from ui.ui import UI
from utility import utility as util


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
        """Gestisce la logica di una partita in corso."""
        turno = 1
        # while self.p1.checkVittoria() == False and self.p2.checkVittoria() == False:
        self.ui.printGriglia(self.griglia.matrice,[self.p1,self.p2])
        if turno % 2 == 0: # TURNO DI P1
            currPedone = self.p1
        else: # TURNO DI P2
            currPedone = self.p2
        self.ui.mostraTurno(currPedone)
        result = None
        while result == None:
            scelta = input("Mossa da effettuare [/help per visualizzare i comandi] :").lower()

        
        turno += 1

if __name__ == "__main__":
    main = Main()
    main.run()
