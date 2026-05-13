"""Gestisce l'interfaccia grafica relativa ai menu e gli input del gioco"""
from rich.console import Console
from pedone.pedone import Pedone

class UI:
    def __init__(self):
        """Initialize the game's UI with default settings."""
        self.console = Console()
        self._ACCENT_COLOR: str = "red"

    def set_accent_color(self, accent_color: str):
        """Set the accent color for the game's UI."""
        RICH_COLORS: set[str] = {
            "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white",
            "bright_black", "bright_red", "bright_green", "bright_yellow",
            "bright_blue", "bright_magenta", "bright_cyan", "bright_white",
        }

        if accent_color in RICH_COLORS:
            self._ACCENT_COLOR = accent_color
        else:
            raise ValueError(
                f"Invalid accent color '{accent_color}'. "
                "Please choose a color supported by the Rich library!"
            )

    def get_accent_color(self) -> str:
        """Get the accent color for the game's UI."""
        return self._ACCENT_COLOR

    def menuIniziale(self):
        """Mostra il menu iniziale del gioco."""
        self.console.print(f"[bold {self._ACCENT_COLOR}]1.[/bold {self._ACCENT_COLOR}] Nuova partita")
        self.console.print(f"[bold {self._ACCENT_COLOR}]2.[/bold {self._ACCENT_COLOR}] Regole del gioco")
        self.console.print(f"[bold {self._ACCENT_COLOR}]3.[/bold {self._ACCENT_COLOR}] Crediti   ")
        self.console.print("[bold red]0.[/bold red] Esci dal gioco")

    def mostraRegole(self):
        """Mostra le regole del gioco Quoridor"""
        self.console.print(f"""
        [bold {self._ACCENT_COLOR}]REGOLE DEL QUORIDOR[/bold {self._ACCENT_COLOR}]

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
           - Un muro occupa due segmenti consecutivi e l'incrocio centrale.
           - Non è possibile chiudere completamente il percorso
             verso l'obiettivo: deve sempre esistere almeno una strada.

        Vince il primo giocatore che raggiunge il lato opposto.
        """)

    def crediti(self):
        """Mostra gli autori del progetto."""
        self.console.print(f"""
        [bold {self._ACCENT_COLOR}]CREDITI[/bold {self._ACCENT_COLOR}]

Autori del progetto:
- Flavio Abbinante
- Domenico Casamassima
- Gabriele Cotugno
- Alessandro De Marzo
- Giovanni Luca Dell'Aquila
        """)

    def erroreMsg(self, message: str):
        """Mostra un messaggio di errore."""
        self.console.print(f"[bold red]ERRORE: {message}[/bold red]")

    def schermataVittoria(self, vincitore: str):
        """Mostra la schermata di vittoria."""
        self.console.print(
            f"\n[bold black on bright_green] 🎉 PARTITA TERMINATA 🎉 [/bold black on bright_green]\n"
            f"[bold white]VINCITORE:[/bold white] [bold bright_green]{vincitore}[/bold bright_green]\n"
        )

    def helpMessage(self):
        """Mostra il messaggio di aiuto con i comandi e le regole del gioco."""
        print("\n=== MENU DI AIUTO ===")
        print("Comandi disponibili:")
        print("- muovi [cella]: Muove il pedone (es. muovi g3)")
        print("- muro [cella] [orientamento]: Piazza un muro (es. muro f4h)")
        print("- /help: Mostra questo messaggio")
        print("- /bye: Esci dal gioco")
        print("- /quit: Abbandona la partita")

        
        # Richiamo della funzione corretta per evitare doppioni
        self.mostraRegole() 
        
        print("=====================\n")

    def mostraTurno(self, pedone: Pedone):
        """Mostra di chi è il turno usando l'accent color per evidenziare."""
        colore = pedone.getColore()
        nome = pedone.getNome()
        muri = pedone.getMuri()
        
        self.console.print(
            f"👉 [bold reverse {colore}] TURNO DI: {nome} [/bold reverse {colore}] "
            f"[white]| Muri rimanenti:[/white] [bold yellow]{muri}[/bold yellow]\n"
        )

    def printGriglia(self, matrice_griglia, pedoni: list[Pedone]):
        """Stampa la griglia di gioco."""
        self.console.print(f"     [bold {self._ACCENT_COLOR}]a   b   c   d   e   f   g   h   i[/bold {self._ACCENT_COLOR}]")
        self.console.print("   [dim]" + "-" * 37 + "[/dim]")

        for r in range(17):
            riga_str = ""
            if r % 2 == 0:
                numero_riga = 9 - (r // 2)
                riga_str += f" [bold {self._ACCENT_COLOR}]{numero_riga}[/bold {self._ACCENT_COLOR}] [dim]|[/dim]"
            else:
                riga_str += "   [dim]|[/dim]" 

            for c in range(17):
                if r % 2 == 0 and c % 2 == 0:
                    simbolo = "." 
                    colore = "bright_black" 
                    
                    for pedone in pedoni:
                        pos = pedone.getPosizione() 
                        if pos.riga == r and pos.colonna == c:
                            simbolo = pedone.getNome() 
                            colore = pedone.getColore()
                            break
                            
                    testo_casella = f" {simbolo} " if len(simbolo) == 1 else f" {simbolo}"
                    riga_str += f"[{colore}]{testo_casella}[/{colore}]"
                
                elif r % 2 == 0 and c % 2 != 0:
                    riga_str += "[bold yellow]║[/bold yellow]" if matrice_griglia[r, c] == 1 else " "
                elif r % 2 != 0 and c % 2 == 0:
                    riga_str += "[bold yellow]═══[/bold yellow]" if matrice_griglia[r, c] == 1 else "   "
                else:
                    riga_str += "[bold yellow]╬[/bold yellow]" if matrice_griglia[r, c] == 1 else " "
            
            if r % 2 == 0:
                riga_str += f"[dim]|[/dim] [bold {self._ACCENT_COLOR}]{9 - (r // 2)}[/bold {self._ACCENT_COLOR}]"
            else:
                riga_str += "[dim]|[/dim]"
                
            self.console.print(riga_str) 
            
        self.console.print("   [dim]" + "-" * 37 + "[/dim]")
        self.console.print(f"     [bold {self._ACCENT_COLOR}]a   b   c   d   e   f   g   h   i[/bold {self._ACCENT_COLOR}]\n")
