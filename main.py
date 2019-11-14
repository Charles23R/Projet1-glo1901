import argparse
import api


def analyser_commande():
    # créer un analyseur de ligne de commande
    parser = argparse.ArgumentParser(description = "Jeu Quoridor - phase 1")
    
    # insérer ici avec les bons appels à la méthode add_argument
    parser.add_argument("idul", help = "IDUL du joueur.")
    parser.add_argument("-l", "--lister", dest = "affichage", help = "Lister les identifiants de vos 20 dernières parties", action = "store_true")
    
    return parser.parse_args()


def afficher_damier_ascii(dico):

    cases = [["." for i in range(9)] for i in range(9)]
    mursH = [[" " for i in range(8)] for i in range(35)]
    mursV = [[" " for i in range(17)] for i in range(8)]

    joueurs = dico["joueurs"]
    idulJoueur = ""
    for joueur in joueurs:
        if joueur["nom"] == "robot":
            cases[joueur["pos"][0]-1][joueur["pos"][1]-1] = "2"
        else:
            cases[joueur["pos"][0]-1][joueur["pos"][1]-1] = "1"
            idulJoueur = joueur["nom"]

    dicoH = dico["murs"]["horizontaux"]
    for coord in dicoH:
        for i in range(7):
            mursH[(4*coord[0])-4+i][coord[1]-1] = "-"

    dicoV = dico["murs"]["verticaux"]
    for coord in dicoV:
        for i in range(3):
            mursV[(coord[0])-2][(2*coord[1])-2+i] = "|"

    damier = "Légende: 1=" + idulJoueur + ", 2=automate\n"
    damier += "   "+("-" * 35)+"\n"

    for i in reversed(range(17)):
        if i % 2 == 0:
            damier += str((i+2) // 2) + " |"
            for j in range(9):
                damier += " " + cases[j][(i // 2)] + " "
                if j != 8:
                    damier += mursV[j][i]

        else:
            damier +="  |"
            for j in range(35):
                if ((j-3) % 4) == 0 and mursH[j][(i // 2)] == " ":
                    damier += mursV[int((j-3) / 4)][i]
                else:
                    damier += mursH[j][(i // 2)]
        
        damier += "|\n"

    damier += "--|" + (35*"-") + "\n  |"
    for i in range (9):
        damier += " " + str(i+1) + "  "
    
    print(damier[:-2])

        
analyseur = analyser_commande()

if analyseur.affichage:
    print(api.lister_parties(analyseur.idul))

else:
    partie = api.débuter_partie(analyseur.idul)
    etat = partie[1]
    idPartie = partie[0]

    partieTerminee = False

    
    while not partieTerminee:
        afficher_damier_ascii(etat)

        error = True
        while error:
            try:
                print("\nQuelle action voulez-vous effectuer?")
                print("1- Vous déplacer")
                print("2- Placer un mur horizontal")
                print("3- Placer un mur vertical")
                print("\n4- Quitter")

                reponse = input()

                if str(reponse) == "1":
                    while error:
                        #créer un méthode
                        print("\nEntrez les coordonnées où vous voulez vous déplacer")
                        print("sous la forme suivante: x,y")
                        inp = input()
                        coord = (int(inp.split(",")[0]), int(inp.split(",")[1]))

                        try:
                            if (0 < int(coord[0]) < 10) and (0 < int(coord[1]) < 10):
                                error = False
                                etat = api.jouer_coup(idPartie, "D", coord)
                                        
                            else:
                                print("Veuillez entrer un choix valide")
                        except TypeError or ValueError:
                            print("Veuillez entrer un choix valide")

                elif str(reponse) == "2":
                    while error:
                        print("\nEntrez les coordonnées où vous voulez placer le mur")
                        print("sous la forme suivante: x,y")
                        inp = input()
                        coord = (int(inp.split(",")[0]), int(inp.split(",")[1]))

                        try:
                            if (0 < int(coord[0]) < 10) and (0 < int(coord[1]) < 10):
                                error = False
                                etat = api.jouer_coup(idPartie, "MH", coord)
                                        
                            else:
                                print("Veuillez entrer un choix valide")
                        except TypeError or ValueError:
                            print("Veuillez entrer un choix valide")

                elif str(reponse) == "3":
                    while error:
                        print("\nEntrez les coordonnées où vous voulez vous placer le mur")
                        print("sous la forme suivante: x,y")
                        inp = input()
                        coord = (int(inp.split(",")[0]), int(inp.split(",")[1]))

                        try:
                            if (0 < int(coord[0]) < 10) and (0 < int(coord[1]) < 10):
                                error = False
                                etat = api.jouer_coup(idPartie, "MV", coord)
                                        
                            else:
                                print("Veuillez entrer un choix valide")
                        except TypeError or ValueError:
                            print("Veuillez entrer un choix valide")

                elif str(reponse) == "4":
                    error = False
                    partieTerminee = True

                else:
                    print("Veuillez entrer un choix valide")

            except RuntimeError as err:
                print("\n"+str(err)+"\n")
            except StopIteration as err:
                print(str(err) + " a remporté la partie!")
                partieTerminee = True