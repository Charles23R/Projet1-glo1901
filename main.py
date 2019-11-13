import argparse
import api

def analyser_commande():
    # créer un analyseur de ligne de commande
    parser = argparse.ArgumentParser(description = "Jeu Quoridor - phase 1")
    
    # insérer ici avec les bons appels à la méthode add_argument
    parser.add_argument("idul", help = "IDUL du joueur.")
    parser.add_argument("-l", "--lister", help = "Lister les identifiants de vos 20 dernières parties", action = "store_true")
    
    return parser.parse_args()

#pas encore fait
def afficher_damier_ascii(dico):
    print(dico)
    #damier = "Légende: 1="+dico["joueurs"].getKeys()[0]+", 2="+dico["joueurs"].getKeys()[1]+"\n"
    #damier += "   "+("-" * 35)+"\n"
    

analyseur = analyser_commande()

rejouer = True

while rejouer:

    partie = api.débuter_partie(analyseur.idul)
    etat = partie[1]
    idPartie = partie[0]

    partieTerminee = False

    while not partieTerminee:
        afficher_damier_ascii(etat)

        error = True
        while error:
            print("\nQuelle action voulez-vous effectuer?")
            print("\n1- Vous déplacer")
            print("\n2- Placer un mur horizontal")
            print("\n3- Placer un mur vertical")
            print("\n\n4- Quitter")

            reponse = input()

            if str(reponse) == "1":
                while error:
                    #créer un méthode
                    print("\nEntrez les coordonnées où vous voulez vous déplacer")
                    print("\nsous la forme suivante: x,y")
                    inp = input()
                    coord = (int(inp.split(",")[0]), inp.split(",")[1])

                    if (0 < int(coord[0] < 10)) and (0 < int(coord[1]) < 10):
                        error = False
                        api.jouer_coup(idPartie, "D", coord)
                    
                    else:
                        print("Veuillez entrer un choix valide")

            elif str(reponse) == "2":
                while error:
                    print("\nEntrez les coordonnées où vous voulez placer le mur")
                    print("\nsous la forme suivante: x,y")
                    inp = input()
                    coord = (int(inp.split(",")[0]), inp.split(",")[1])

                    if (0 < int(coord[0] < 10)) and (0 < int(coord[1]) < 10):
                        error = False
                        api.jouer_coup(idPartie, "MH", coord)
                    
                    else:
                        print("Veuillez entrer un choix valide")

            elif str(reponse) == "3":
                while error:
                    print("\nEntrez les coordonnées où vous voulez vous placer le mur")
                    print("\nsous la forme suivante: x,y")
                    inp = input()
                    coord = (int(inp.split(",")[0]), inp.split(",")[1])

                    if (0 < int(coord[0] < 10)) and (0 < int(coord[1]) < 10):
                        error = False
                        api.jouer_coup(idPartie, "MV", coord)
                    
                    else:
                        print("Veuillez entrer un choix valide")

            elif str(reponse) == "4":
                error = False
                partieTerminee = True

            else:
                print("Veuillez entrer un choix valide")

        #condition de victoire

    valide = False
    while not valide:
        print("\nPartie terminée. Voulez-vous rejouer?")
        print("\n1- Oui")
        print("\n2- Non")
        inp = input()

        if int(inp) == 2:
            valide = True
            print("À la prochaine!")
            rejouer = False
        
        elif int(inp) == 1:
            valide = True

        else:
            print("Veuillez entrer un choix valide")