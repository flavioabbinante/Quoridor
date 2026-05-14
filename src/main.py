from rich import print

from griglia.cella import Cella
from griglia.griglia import Griglia
from muro.muro import Muro
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
        util.waitKey()
        util.clearScreen()
        menuIniziale = ""
        while True:
            self.ui.menuIniziale()
            menuIniziale = input("Seleziona un'opzione: ")
            util.clearScreen()
            if menuIniziale == "1": # Qui si gestisce la nuova partita
                self.partita() # Inizio della nuova partita
                util.waitKey()
                util.clearScreen()
            elif menuIniziale == "2": # Regole del gioco
                self.ui.mostraRegole()
                util.waitKey()
                util.clearScreen()
            elif menuIniziale == "3": # Autori del progetto
                self.ui.crediti()
                util.waitKey()
                util.clearScreen()
            elif menuIniziale == "0":
                util.esciGioco() # Esco dal gioco e fermo il processo
            else:
                self.ui.erroreMsg("Opzione non valida. Riprova.")
                util.waitKey()
                util.clearScreen()

    def partita(self):
        """Gestisce il loop di una partita, alternando i turni dei giocatori e verificando le condizioni di vittoria."""
        turno = 1
        
        while not self.p1.checkVittoria() and not self.p2.checkVittoria():
            self.ui.printGriglia(self.griglia.matrice, [self.p1, self.p2])
            
            if turno % 2 == 0:
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

    def eseguiMossa(self, scelta: str, pedone: Pedone):

        azione = util.checkInput(scelta) # Controllo che l'input sia valido e capisco quale azione si vuole eseguire
        
        # Se devo piazzare un muro o muovere il pedone
        if azione == "move" or azione == "wall":
            r, c = util.convertiCoordinate(scelta, azione) # Converto le coordinate da stringa a indici
            
            if azione == "move":
                destinazione = self.griglia.get_cella(r, c)
                posizioneAttuale = pedone.getPosizione()

                # Verifica che la cella sia esattamente adiacente (ortogonale)
                distanzaValida = abs(destinazione.riga - posizioneAttuale.riga) + abs(destinazione.colonna - posizioneAttuale.colonna) == 2

                if destinazione and distanzaValida and self.griglia.passaggio_libero(posizioneAttuale, destinazione):
                    pedone.muoviPedone(destinazione)
                    return True
                else:
                    self.ui.erroreMsg("Movimento non consentito. Puoi spostarti solo in una cella adiacente.")

            else: # Piazzamento muro
                orientamento = scelta[2] # l'ordine è riga, colonna, orientamento
                nuovoMuro = Muro(r, c, orientamento)
                
                if pedone.usaMuro() == True:
                    # Tenta il piazzamento fisico sulla griglia
                    if self.griglia.piazza_muro(nuovoMuro):
                        return True
                    else:
                        # Restituisce il muro se il piazzamento fallisce (collisione o fuori limiti)
                        pedone.muri += 1
                        self.ui.erroreMsg("Non è possibile piazzare il muro in questa posizione.")
                else:
                    self.ui.erroreMsg("Non hai più muri a disposizione.")
                    
        # Comandi speciali
        elif azione == "help":
            self.ui.helpMessage()   
        elif azione == "quit":
            return "quit"    
        elif azione == "bye":
            util.esciGioco()
        else:
            self.ui.erroreMsg("Comando non riconosciuto.")
            
        return False

if __name__ == "__main__":
    main = Main()
    main.run()
