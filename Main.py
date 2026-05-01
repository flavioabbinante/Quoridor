import sys

# Funzione per gestire l'uscita definitiva dal gioco
def esci_dal_gioco():
    # Chiedo conferma all'utente come richiesto dai criteri di accettazione
    print("\n[SISTEMA] Sei sicuro di voler uscire?")
    conferma = input("Scrivi 'si' per confermare l'uscita: ").lower().strip()
    
    if conferma == "si":
        print("Chiusura del processo in corso... Grazie per aver giocato!")
        # Interrompe definitivamente il programma (Criterio 2)
        sys.exit(0)
    else:
        # Se l'utente non scrive 'si', l'uscita viene annullata
        print("[SISTEMA] Uscita annullata. Il gioco continua.")

# --- STRUTTURA PER TESTARE IL COMANDO ---
def main():
    print("--- QUORIDOR GAME ---")
    
    while True:
        # In questo Sprint, l'utente può digitare 'esci' in qualsiasi momento
        comando = input("\nInserisci comando: ").lower().strip()
        
        if comando == "esci":
            esci_dal_gioco()
        else:
            print(f"Hai digitato '{comando}'. (Solo il comando 'esci' è attivo in questa Issue)")

# Avvio del programma
if __name__ == "__main__":
    main()
