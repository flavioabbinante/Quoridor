"""Gestisce l'interfaccia grafica relativa ai menu e gli input del gioco"""

from rich.console import Console
from pedone.pedone import Pedone

class UI:

    def __init__(self):
        """
        Inizializza la console "Rich" per la gestione dell'interfaccia.
        """
        self.console = Console()

    def menuIniziale(self):
        """
        Mostra il menu iniziale del gioco.
        """
        self.console.print("[bold cyan]1.[/bold cyan] Nuova partita")
        self.console.print("[bold cyan]2.[/bold cyan] Regole del gioco")
        self.console.print("[bold cyan]3.[/bold cyan] Crediti   ")
        self.console.print("[bold red]0.[/bold red] Esci dal gioco")

    def mostraRegole(self):
        """Mostra le regole del gioco Quoridor"""

        self.console.print("""
        [bold cyan]REGOLE DEL QUORIDOR[/bold cyan]

        - Il gioco si svolge su una griglia 9x9.
        - Ogni giocatore controlla un pedone e dispone di 10 muri.
        - Lo scopo è raggiungere il lato opposto della scacchiera prima
          dell'avversario.

        Durante il proprio turno un giocatore può:

        [bold green]1.[/bold green] Muovere il pedone
           - Il pedone si muove di una casella in alto, basso,
             destra o sinistra.
           - Non può attraversare i muri.
           - Se il pedone avversario è adiacente, è possibile saltarlo
             se dietro c'è una casella libera.

        [bold green]2.[/bold green] Posizionare un muro
           - I muri bloccano il passaggio tra le caselle.
           - Un muro occupa due segmenti consecutivi.
           - I muri possono essere verticali o orizzontali.
           - Non è possibile chiudere completamente il percorso
             verso l'obiettivo: deve sempre esistere almeno una strada.

        Vince il primo giocatore che raggiunge il lato opposto.
        """)

    def crediti(self):
        """
        Mostra gli autori del progetto.
        """
        self.console.print("""
        [bold cyan]CREDITI[/bold cyan]

Autori del progetto:
- Flavio Abbinante
- Domenico Casamassima
- Gabriele Cotugno
- Alessandro De Marzo
- Giovanni Luca Dell'Aquila
        """)

    def mostraTurno(self, pedone: Pedone, muriRimanenti):
        """
        Mostra il turno corrente.

        Args:
            pedone (str): Nome o simbolo del pedone.
            muriRimanenti (int): Numero di muri rimasti al giocatore.
        """
        self.console.print(
            f"Turno di [bold {pedone.getColore()}]{pedone.getNome()}[/bold {pedone.getColore()}] "
            f"[white]| Muri rimanenti:[/white] [bold yellow]{muriRimanenti}[/bold yellow]"
        )

    def erroreMsg(self, message: str):
        """
        Mostra un messaggio di errore.

        Args:
            message (str): Testo dell'errore da visualizzare.
        """
        self.console.print(f"[bold red]{message}[/bold red]")

    def schermataVittoria(self, vincitore):
        """
        Mostra la schermata di vittoria.

        Args:
            vincitore (str): Nome del giocatore vincente.
        """
        self.console.print(
            f"\n[bold black on yellow]PARTITA TERMINATA: [/bold black on yellow] \n VINCITORE: [bold]{vincitore}[/bold] \n"
        )

   def helpMessage(self):
        """
        Mostra il messaggio di aiuto durante la partita.
        """
        self.stampaRegole() # Richiama le regole già implementate
        
        self.console.print("\n[bold yellow]— GUIDA RAPIDA AI COMANDI —[/bold yellow]")
        self.console.print("[cyan]MOVIMENTO PEDONE:[/cyan] Inserisci la coordinata (es. [bold]e2[/bold], [bold]f5[/bold])")
        self.console.print("[cyan]POSIZIONA MURO:[/cyan] Intersezione + orientamento (es. [bold]e4h[/bold] o [bold]c2v[/bold])")
        self.console.print("      (h = orizzontale, v = verticale)")
        
        self.console.print("\n[bold yellow]— REGOLE E VITTORIA —[/bold yellow]")
        self.console.print("[white]OBIETTIVO:[/white] Vince chi raggiunge per primo il lato opposto.")
        self.console.print("[white]MURI:[/white] Ogni giocatore ha 10 muri. Vietato bloccare totalmente l'avversario.")
        self.console.print("[bold yellow]—————————————————————————————[/bold yellow]\n")

    def printGriglia():
        """Stampa la griglia di gioco"""
        pass

