import argparse
import api

def analyser_commande():
    # créer un analyseur de ligne de commande
    parser = argparse.ArgumentParser(description = "Jeu Quoridor - phase 1")
    
    # insérer ici avec les bons appels à la méthode add_argument
    parser.add_argument("idul", help = "IDUL du joueur.")
    parser.add_argument("-l", "--lister", help = "Lister les identifiants de vos 20 dernières parties", action = "store_true")
    
    return parser.parse_args()


def afficher_damier_ascii(dico):
    damier = "Légende: 1="+dico["joueurs"].getKeys()[0]+", 2="+dico["joueurs"].getKeys()[1]+"\n"
    damier += "   "+("-" * 35)+"\n"
    

analyseur = analyser_commande()

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
            error = False
            api.jouer_coup(idPartie, "D", (3, 9))

        elif str(reponse) == "2":
            error = False
            api.jouer_coup(idPartie, "D", (3, 9))

        elif str(reponse) == "3":
            error = False
            api.jouer_coup(idPartie, "D", (3, 9))

        elif str(reponse) == "4":
            error = False

        else:
            print("Veuillez entrer un choix valide")
