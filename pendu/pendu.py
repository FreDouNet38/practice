"""ce fichier contient le jeu du pendu"""

from donnees import *
from fonctions import *

scores = charger_scores()

utilisateur = creer_nom_utilisateur()

if utilisateur not in scores.keys():
    scores[utilisateur] = 0

continuer_partie = 'o'

while continuer_partie != 'n':
    print("Joueur {0} : {1} point(s)".format(utilisateur, scores[utilisateur]))
    mot_a_trouver = choisir_mot()
    lettres_trouvees = []
    mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)
    nb_chances = nb_coups
    while mot_a_trouver != mot_trouve and nb_chances>0:
        print("Mot à trouver {0} (encore{1} chances)".format(mot_trouve, nb_chances))
        lettre = recup_lettre()
        if lettre in lettres_trouvees:
            print("Vous avez déjà choisi cette lettre.")
        elif lettre in mot_a_trouver:
            lettres_trouvees.append(lettre)
            print("Bien joué!")
        else:
            nb_chances -= 1
            print("non, cette lettre ne se trouve pas dans le mot")
        mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)
                                      
    if mot_a_trouver==mot_trouve:
        print("Félicitations!")
    else:
        print("PENDU")
    scores[utilisateur] += nb_chances

    continuer_partie = input("Souhaitez-vous continuer (O/N) ? ")
    continuer_partie = continuer_partie.lower()

enregistrer_scores(scores)

print("Vous finissez la partie avec {0} points.".format(scores[utilisateur]))
    
