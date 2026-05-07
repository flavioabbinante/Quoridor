"""Gestisce l'interfaccia grafica relativa ai menu e gli input del gioco"""

from rich.console import Console

class UI:

    def __init__(self):
        """Costruttore della classe UI"""
        self.console = Console()

    def menuIniziale(self):
        """Mostra il menu iniziale"""

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
        """Mostra i crediti del gioco"""

        self.console.print("""
        [bold cyan]CREDITI[/bold cyan]

Autori del progetto:
- Flavio Abbinante
- Domenico Casamassima
- Gabriele Cotugno
- Alessandro De Marzo
- Giovanni Luca Dell'Aquila
        """)

    def mostraTurno(self, pedone,color, muriRimanenti):
        """Mostra il turno corrente"""

        self.console.print(
            f"Turno di [bold {color}]{pedone}[/bold {color}] "
            f"[white]| Muri rimanenti:[/white] [bold yellow]{muriRimanenti}[/bold yellow]"
        )

    def erroreMsg(self,message:str):
        self.console.print(f"[bold red]{message}[/bold red]")

    def schermataVittoria(self, vincitore):
        """Mostra la schermata di vittoria"""

        self.console.print(
            f"\n[bold black on yellow]PARTITA TERMINATA: [/bold black on yellow] \n VINCITORE: [bold]{vincitore}[/bold] \n"
        )


