# Definizione dei codici di escape ANSI per i colori
R = "\u001b[0m"
RED = "\u001b[31m"
CYAN = "\u001b[36m"
G = "\u001b[90m"

def stampa_griglia(griglia):
    for riga in griglia:
        print("|".join(riga))
        print("-----------")

def mossa_giocatore(griglia, simbolo_giocatore):
    while True:
        casella = int(input("Inserisci il numero casella (0 - 9): "))
        riga = int(casella/3)
        colonna = int(casella%3)

        if griglia[riga][colonna] not in {'X', 'O'}:
            griglia[riga][colonna] = simbolo_giocatore
            break
        else:
            print("La cella è occupata. Riprova.")

def verifica_vittoria(griglia, simbolo_giocatore):
    for i in range(3):
        if griglia[i][0] == griglia[i][1] == griglia[i][2] == simbolo_giocatore:
            return True
        if griglia[0][i] == griglia[1][i] == griglia[2][i] == simbolo_giocatore:
            return True
    if griglia[0][0] == griglia[1][1] == griglia[2][2] == simbolo_giocatore:
        return True
    if griglia[0][2] == griglia[1][1] == griglia[2][0] == simbolo_giocatore:
        return True
    return False

def gioca_tris():
    griglia = [[G+" 0 "+R, G+" 1 "+R, G+" 2 "+R],
               [G+" 3 "+R, G+" 4 "+R, G+" 5 "+R],
               [G+" 6 "+R, G+" 7 "+R, G+" 8 "+R]]
    simboli = [RED+" X "+R, CYAN+" O "+R]
    turno = 0
    finito = False

    while not finito:
        stampa_griglia(griglia)
        simbolo_giocatore = simboli[turno % 2]
        mossa_giocatore(griglia, simbolo_giocatore)

        if verifica_vittoria(griglia, simbolo_giocatore):
            stampa_griglia(griglia)
            print("Giocatore", simbolo_giocatore, "ha vinto!")
            finito = True
        elif turno == 8:
            stampa_griglia(griglia)
            print("Pareggio!")
            finito = True

        turno += 1

# Avvia il gioco del tris
gioca_tris()