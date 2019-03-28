"""Ce fichier contient les fonctions du jeu de pendu"""

import pickle
import os
from random import choice
from donnees import *

def choisir_mot():
    return choice(liste_mots)

def creer_nom_utilisateur():
    nom_utilisateur = input("Inscrivez votre nom")
    nom_utilisateur.upper()
    if not nom_utilisateur.isalnum() and len(nom_utilisateur)<4:
        print("Ce nom n'est pas valide. Il doit contenir au minimum 4 caractères et seulement des lettre et/ou des chiffres")
        return creer_nom_utilisateur()
    else:
        return nom_utilisateur

def enregistrer_scores(scores):
    fichier_scores = open(pendu_fichier_scores, 'wb')
    mon_pickler = pickle.Pickler(fichier_scores)
    mon_pickler.dump(scores)
    fichier_scores.close()
    
    
def charger_scores():
    if os.path.exists(pendu_fichier_scores):
        fichier_scores = open(pendu_fichier_scores, "rb")
        mon_depickler = pickle.Unpickler(fichier_scores)
        scores = mon_depickler.load()
        fichier_scores.close()
    else:
        scores = {}
    return scores

def recup_lettre():
    lettre = input("Choisissez un lettre: ")
    lettre = lettre.lower()
    if len(lettre) > 1:
        print("Entrez une seule lettre")
        return votre_lettre
    elif not lettre.isalpha():
        print("Entrez une lettre et pas autre chose!")
        return votre_lettre
    else:
        return lettre


def recup_mot_masque(mot_complet, lettres_trouvees):
    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvees:
            mot_masque += lettre
        else:
            mot_masque += "*"
    return mot_masque
