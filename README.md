[![Continuous Integration and Continuous Delivery (CI/CD)](https://github.com/softeng2526-inf-uniba/proj-hamming/actions/workflows/CI-CD.yml/badge.svg)](https://github.com/softeng2526-inf-uniba/proj-hamming/actions/workflows/CI-CD.yml)

---

> 
Quoridor CLI è un progetto universitario sviluppato in team da 5 studenti nell'ambito del corso di Ingegneria del Software, con l'obiettivo di applicare in modo rigoroso i principi dell'ingegneria del software moderna a un dominio di gioco non banale.
Il progetto consiste nella realizzazione di una versione testuale del celebre gioco da tavolo Quoridor, con piena gestione della logica di movimento dei pedoni, del piazzamento dei muri e della validazione dei percorsi tramite algoritmi di pathfinding su matrice 17×17 (NumPy). Il sistema è strutturato secondo il pattern architetturale MVC, con una netta separazione tra logica di dominio, presentazione e controllo del flusso applicativo.

---

## 📁 Struttura dei Moduli

| Modulo | Ruolo | Descrizione |
|--------|-------|-------------|
| `src/main.py` | Controller | Punto di ingresso dell'applicazione. Inizializza i componenti, gestisce lo stato dei turni e smista i comandi. |
| `src/griglia/` | Model | Contiene la logica spaziale. Sfrutta una matrice bidimensionale ottimizzata per tracciare percorsi e ostacoli liberi. |
| `src/pedone/` & `src/muro/` | Model | Classi pure di dominio (Anemic/Rich Models) che incapsulano lo stato fisico dei giocatori e dei singoli blocchi. |
| `src/ui/` | View | Si occupa della formattazione estetica del tabellone e dell'interazione testuale con l'utente. |
| `src/utility/` | Utility | Contiene funzioni matematiche pure per la conversione rapida delle stringhe umane (es. `e2`) negli indici reali dell'array NumPy O(1). |

---

## 🛠 Tecnologie e Stack Tecnologico

- **Linguaggio:** Python 3.11+
- **Librerie Core:**
  - `numpy` — Per la manipolazione e l'analisi super efficiente della scacchiera sotto forma di matrice 17×17.
  - `rich` — Per dare stile, formattazione avanzata, tabelle e colori vivaci al terminale.
- **Testing:** `pytest` per la scrittura ed esecuzione automatizzata dei test unitari di QA.
- **Package & Project Management:** `uv`
- **DevOps:** Docker per garantire la riproducibilità totale dell'ambiente di esecuzione su qualsiasi OS.

---

## 🚀 Installazione e Configurazione

È possibile clonare il progetto ed eseguirlo localmente attraverso due modalità differenti.

### Opzione A: Utilizzo di `uv` (Consigliato)

Clonare la repository ed entrare nella directory:

```bash
git clone https://github.com/USERNAME/Quoridor.git
cd quoridor-cli
```

Avviare direttamente il gioco:

```bash
uv run src/main.py
```

### Opzione B: Ambiente Virtuale standard

Creare e attivare un ambiente virtuale:

```bash
python -m venv .venv

# Su Windows:
.venv\Scripts\activate

# Su Mac/Linux:
source .venv/bin/activate
```

Installare le dipendenze richieste:

```bash
pip install -r requirements.txt
```

Avviare il gioco:

```bash
python src/main.py
```

---

## 🗺 Guida ai Comandi di Gioco

Una volta avviata la partita, i giocatori inseriscono a turno i propri comandi testuali.

### Movimento del Pedone

Inserisci la cella di destinazione nel formato `Lettera + Numero`.

```
e2    →  si sposta nella cella e2
```

### Piazzamento del Muro

Inserisci la cella pivot seguita dall'orientamento (`h` per orizzontale, `v` per verticale).

```
e7h   →  piazza un muro orizzontale sotto la cella e7
```

### Comandi Console

| Comando | Descrizione |
|---------|-------------|
| `/help` | Mostra la legenda dei comandi e le regole senza perdere il turno. |
| `/quit` | Permette di dichiarare la resa; assegna la vittoria istantanea all'avversario. |
| `/bye`  | Interrompe il processo e chiude l'applicazione chiedendo conferma. |

---

## 👥 Il Team di Sviluppo

Il progetto è stato ideato, progettato e implementato in stretta collaborazione da **5 studenti** come membri paritari del team di sviluppo Scrum.
