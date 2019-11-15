"""contient toutes les fonctions qui communiquent avec le serveur"""
import requests

def lister_parties(idul):
    """retourne la liste des 20 dernières parties de l'utilisateur"""
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.get(url_base+'lister/', params={'idul': idul})
    if rep.status_code == 200:
        rep = rep.json()
        if "message" in rep:
            raise RuntimeError(rep["message"])
        return rep
    print(f"Le GET sur {url_base+'lister'} a produit le code d'erreur {rep.status_code}.")


def débuter_partie(idul):
    """Retourne une nouvelle partie"""
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'

    rep = requests.post(url_base+'débuter/', data={'idul': idul})

    if rep.status_code == 200:
        rep = rep.json()
        if "message" in rep:
            raise RuntimeError(rep["message"])

        return (rep["id"], rep["état"])
    print(f"Le POST sur {url_base+'débuter'} a produit le code d'erreur {rep.status_code}.")

def jouer_coup(id_partie, type_coup, position):
    """retourne l'état de jeu actuel"""
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'

    rep=requests.post(url_base+'jouer/', data={'id': id_partie, "type": type_coup, "pos": position})

    if rep.status_code == 200:
        # la requête s'est déroulée normalement; décoder le JSON
        rep = rep.json()
        if "message" in rep:
            raise RuntimeError(rep["message"])
        elif "gagnant" in rep:
            raise StopIteration(rep["gagnant"])

        return rep["état"]
    print(f"Le POST sur {url_base+'jouer'} a produit le code d'erreur {rep.status_code}.")
