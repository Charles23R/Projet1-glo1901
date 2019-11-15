"""Ceci est le main. Il contient la fonction analyser_commande et afficher_damier_ascii"""
import argparse
import api


def analyser_commande():
    """Analyse les commandes du terminal"""
    parser = argparse.ArgumentParser(description="Jeu Quoridor - phase 1")
    parser.add_argument("idul", help="IDUL du joueur.")
    aide = "Lister les identifiants de vos 20 dernières parties"
    st = "store_true"
    parser.add_argument("-l", "--lister", dest="affichage", help=aide, action=st)
    return parser.parse_args()

def afficher_damier_ascii(dico):
    """affiche l'état de jeu en art ascii"""
    cases = [["." for i in range(9)] for i in range(9)]
    mursh = [[" " for i in range(8)] for i in range(35)]
    mursv = [[" " for i in range(17)] for i in range(8)]
    joueurs = dico["joueurs"]
    iduljoueur = ""
    for joueur in joueurs:
        if joueur["nom"] == "robot":
            cases[joueur["pos"][0]-1][joueur["pos"][1]-1] = "2"
        else:
            cases[joueur["pos"][0]-1][joueur["pos"][1]-1] = "1"
            iduljoueur = joueur["nom"]

    dicoh = dico["murs"]["horizontaux"]
    for coordo in dicoh:
        for i in range(7):
            mursh[(4*coordo[0])-4+i][coordo[1]-1] = "-"

    dicov = dico["murs"]["verticaux"]
    for coordo2 in dicov:
        for i in range(3):
            mursv[(coordo2[0])-2][(2*coordo2[1])-2+i] = "|"

    damier = "Légende: 1=" + iduljoueur + ", 2=automate\n"
    damier += "   "+("-" * 35)+"\n"
    for i in reversed(range(17)):
        if i % 2 == 0:
            damier += str((i+2) // 2) + " |"
            for j in range(9):
                damier += " " + cases[j][(i // 2)] + " "
                if j != 8:
                    damier += mursv[j][i]
        else:
            damier += "  |"
            for j in range(35):
                if ((j-3) % 4) == 0 and mursh[j][(i // 2)] == " ":
                    damier += mursv[int((j-3) / 4)][i]
                else:
                    damier += mursh[j][(i // 2)]
        damier += "|\n"
    damier += "--|" + (35*"-") + "\n  |"
    for i in range(9):
        damier += " " + str(i+1) + "  "
    print(damier[:-2])

ANALYSEUR = analyser_commande()
if ANALYSEUR.affichage:
    print(api.lister_parties(ANALYSEUR.idul))
else:
    PARTIE = api.débuter_partie(ANALYSEUR.idul)
    ETAT = PARTIE[1]
    IDPARTIE = PARTIE[0]
    PARTIETERMINEE = False
    while not PARTIETERMINEE:
        afficher_damier_ascii(ETAT)
        ERROR = True
        while ERROR:
            try:
                print("\nQuelle action voulez-vous effectuer?")
                print("1- Vous déplacer")
                print("2- Placer un mur horizontal")
                print("3- Placer un mur vertical")
                print("\n4- Quitter")
                REPONSE = input()

                if str(REPONSE) == "1":
                    while ERROR:
                        #créer un méthode
                        print("\nEntrez les coordonnées où vous voulez vous déplacer")
                        print("sous la forme suivante: x,y")
                        INP = input()
                        COORD = (int(INP.split(",")[0]), int(INP.split(",")[1]))

                        try:
                            if (0 < int(COORD[0]) < 10) and (0 < int(COORD[1]) < 10):
                                ERROR = False
                                ETAT = api.jouer_coup(IDPARTIE, "D", COORD)
                            else:
                                print("Veuillez entrer un choix valide")
                        except TypeError:
                            print("Veuillez entrer un choix valide")
                        except ValueError:
                            print("Veuillez entrer un choix valide")

                elif str(REPONSE) == "2":
                    while ERROR:
                        print("\nEntrez les coordonnées où vous voulez placer le mur")
                        print("sous la forme suivante: x,y")
                        INP = input()
                        COORD = (int(INP.split(",")[0]), int(INP.split(",")[1]))
                        try:
                            if (0 < int(COORD[0]) < 10) and (0 < int(COORD[1]) < 10):
                                ERROR = False
                                ETAT = api.jouer_coup(IDPARTIE, "MH", COORD)
                            else:
                                print("Veuillez entrer un choix valide")
                        except TypeError:
                            print("Veuillez entrer un choix valide")
                        except ValueError:
                            print("Veuillez entrer un choix valide")

                elif str(REPONSE) == "3":
                    while ERROR:
                        print("\nEntrez les coordonnées où vous voulez vous placer le mur")
                        print("sous la forme suivante: x,y")
                        INP = input()
                        COORD = (int(INP.split(",")[0]), int(INP.split(",")[1]))
                        try:
                            if (0 < int(COORD[0]) < 10) and (0 < int(COORD[1]) < 10):
                                ERROR = False
                                ETAT = api.jouer_coup(IDPARTIE, "MV", COORD)
                            else:
                                print("Veuillez entrer un choix valide")
                        except TypeError:
                            print("Veuillez entrer un choix valide")
                        except ValueError:
                            print("Veuillez entrer un choix valide")
                elif str(REPONSE) == "4":
                    ERROR = False
                    PARTIETERMINEE = True
                else:
                    print("Veuillez entrer un choix valide")
            except RuntimeError as err:
                print("\n"+str(err)+"\n")
            except StopIteration as err:
                print(str(err) + " a remporté la PARTIE!")
                PARTIETERMINEE = True
