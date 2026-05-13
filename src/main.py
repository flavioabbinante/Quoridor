from rich import print
from ui.ui import UI
from pedone.pedone import Pedone
from griglia.griglia import Griglia
from griglia.cella import Cella
from muro.muro import Muro
from utility import utility as util
from os import system

class Main():

    def __init__(self):
        self.ui = UI()
        self.griglia = Griglia()
        self.p1 = Pedone("P1","red",Cella(0,5),9)
        self.p2 = Pedone("P1","blue",Cella(9,5),0)

    def run(self):
        print("[bold green]Benvenuto nel gioco del Quoridor![/bold green]\n")
        system("pause")
        system("cls")
        menuIniziale = ""
        while menuIniziale != "1":
            self.ui.menuIniziale()
            menuIniziale = input("Seleziona un'opzione: ")
            if menuIniziale == "1":
                self.ui.printGriglia(self.griglia,[self.p1,self.p2])
                break
            elif menuIniziale == "2":
                self.ui.mostraRegole()
                system("pause")
                system("cls")
            elif menuIniziale == "3":
                self.ui.crediti()
                system("pause")
                system("cls")
            elif menuIniziale == "0":
                util.esciGioco()
            else:
                self.ui.erroreMsg("Opzione non valida. Riprova.")
                system("pause")
                system("cls")


if __name__ == "__main__":
    main = Main()
    main.run()
