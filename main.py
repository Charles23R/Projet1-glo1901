import argparse
import api

def analyser_commande():
    # créer un analyseur de ligne de commande
    parser = argparse.ArgumentParser(description = "Jeu Quoridor - phase 1")
    
    # insérer ici avec les bons appels à la méthode add_argument
    parser.add_argument("idul", help="IDUL du joueur.")
    parser.add_argument("-l", "--lister", help = "Lister les identifiants de vos 20 dernières parties", action = "store_true")
    
    return parser.parse_args()


def afficher_damier_ascii(dico):
    damier = "Légende: 1="+dico["joueurs"].getKeys()[0]+", 2="+dico["joueurs"].getKeys()[1]+"\n"
    damier += "   "+("-" * 35)+"\n"
    
