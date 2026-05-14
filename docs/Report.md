# Relazione tecnica gruppo Hamming

## Indice
- [Introduzione](#introduzione)
- [Modello di dominio](#modello-di-dominio)
- [Requisiti specifici](#requisiti-specifici)
  - [Requisiti funzionali](#31-requisiti-funzionali)
  - [Requisiti non funzionali](#32-requisiti-non-funzionali)
- [System Design](#system-design)
- [Decisioni architetturali e progettuali](#Stili-architetturali)
- [Diagramma dei package](#Diagramma-dei-package)
- [Diagramma dei componenti](#Diagramma-dei-componenti)
- [Analisi retrospettiva](#8-analisi-retrospettiva)
  - [Sprint 0](#81-sprint-0)

---

## Introduzione
Il progetto riguarda la realizzazione del gioco del Quoridor, un gioco da tavolo a turni in cui due giocatori si sfidano per arrivare al lato opposto della scacchiera, usando anche dei muri per ostacolare l’avversario.
Il software viene sviluppato in gruppo da studenti, con team composti da 5 persone. L’obiettivo è applicare le basi dell’ingegneria del software, lavorando sulla progettazione del sistema, sulla divisione in parti e su una struttura del codice chiara.
Il sistema deve rispettare le regole del gioco, gestire le partite e permettere ai giocatori di interagire correttamente. Inoltre, si cerca di creare un progetto facile da capire, modificare ed estendere.


---

## Modello di dominio
![alt text](<img/modello di dominio.png>)

---

## Requisiti specifici

### Requisiti funzionali

I requisiti funzionali descrivono le operazioni che il sistema deve eseguire per garantire il corretto svolgimento di una partita a Quoridor, coprendo le funzionalità richieste dalle User Story del progetto.

**Gestione della Partita e Visualizzazione:**
* Il sistema deve permettere di avviare una nuova partita chiedendo i nomi dei giocatori.
* Il sistema deve visualizzare a schermo la scacchiera di gioco aggiornata ad ogni turno, mostrando chiaramente le celle, la posizione dei pedoni e i muri piazzati.
* Il sistema deve alternare il turno tra il Giocatore 1 e il Giocatore 2.
* Il sistema deve verificare dinamicamente le condizioni di vittoria e decretare la fine della partita quando un pedone raggiunge la riga opposta a quella di partenza.

**Azioni dei Giocatori:**
* Il sistema deve permettere al giocatore di muovere il proprio pedone di una casella in senso ortogonale (orizzontale o verticale).
* Il sistema deve permettere al giocatore di piazzare un muro orizzontale che occupi l'equivalente di due fessure.
* Il sistema deve permettere al giocatore di piazzare un muro verticale che occupi l'equivalente di due fessure.

**Validazione e Rispetto delle Regole:**
* Il sistema deve scalare un muro dal contatore del giocatore ogni volta che ne piazza uno, impedendone il piazzamento se il contatore (MAX 10) ha raggiunto lo zero.
* Il sistema deve impedire i movimenti illegali del pedone.
* Il sistema deve impedire il piazzamento di muri sovrapposti, incidenti o che fuoriescano dalla griglia.

**Interazione dell'Utente:**
* Il sistema deve fornire un comando per mostrare un messaggio di aiuto con la lista delle istruzioni di gioco in qualsiasi momento.
* Il sistema deve permettere di abbandonare la partita in corso dichiarando la resa.
* Il sistema deve permettere di chiudere ed uscire definitivamente dall'applicazione.

### Requisiti non funzionali

I requisiti non funzionali definiscono i criteri di qualità del sistema, garantendo che l'applicazione sia efficiente, manutenibile e facile da utilizzare.

* **Usabilità (Interfaccia CLI):** L'applicazione pur essendo eseguita da terminale, deve risultare visivamente chiara e intuitiva. Deve utilizzare formattazione avanzata e colori (`rich`) per distinguere nettamente i pedoni dei due giocatori, i muri e le coordinate della scacchiera.
* **Manutenibilità e Modularità:** Il codice deve essere strutturato seguendo i principi della Programmazione Orientata agli Oggetti (OOP). Il sistema deve garantire un alto grado di disaccoppiamento (Separation of Concerns), dividendo chiaramente la logica di dominio dalla logica di presentazione.
* **Efficienza:** Il motore di gioco deve validare i movimenti e calcolare le collisioni con i muri in modo ottimizzato. A tale scopo, il sistema richiede l'uso di array efficienti gestiti tramite la libreria `numpy`.
* **Gestione degli errori:** Il sistema non deve andare in crash a fronte di input imprevisti da parte dell'utente. Deve invece intercettare l'errore e mostrare un messaggio di feedback chiaro, permettendo al giocatore di ripetere l'inserimento.
* **Portabilità:** Il gioco deve poter essere eseguit dalla maggioranza dei Terminali.

## System Design
Descrizione dell’architettura generale del sistema e dei suoi componenti principali.

---

## Stili architetturali
Spiega perché hai scelto una certa architettura (es. MVC, layered, clean architecture) e come soddisfa i requisiti.


## Diagramma dei package
![alt text](<img/Diagramma_package.png>)
### Descrizione dei package principali

L'architettura del software è suddivisa in package specifici per garantire un alto livello di disaccoppiamento. Tutti i package del dominio si trovano all'interno della directory `src/`.

| Package | Responsabilità | Dipendenze |
| :--- | :--- | :--- |
| **`griglia`** | Contiene le classi `Griglia` e `Cella`. Gestisce la scacchiera (matrice numpy), la mappatura delle celle calpestabili e la validazione fisica dei percorsi e delle collisioni. | `muro`, `numpy` |
| **`muro`** | Contiene il modello dati dell'entità `Muro` (coordinate del perno centrale e orientamento orizzontale/verticale). | Nessuna |
| **`pedone`** | Contiene lo stato del giocatore, la sua posizione attuale (`Cella`), la riga obiettivo per la vittoria e il contatore dei muri a disposizione. | `griglia.cella` |
| **`ui`** | Gestisce solo l'output visivo da terminale. Renderizza la matrice a colori, stampa i menu e i messaggi di errore.| `pedone`, `rich` |
| **`utility`** | Fornisce funzioni di supporto condivise, come il parser per validare l'input testuale dell'utente e l'algoritmo di conversione dalle coordinate umane (notazione del quoridor) agli indici della matrice. | `sys` |

## Diagramma dei componenti 
Da inserire se si usano librerie esterne

---

## 8. Analisi retrospettiva

### 8.1 Sprint 0



---