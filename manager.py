from Menus.close_menu import Close
from Menus.start import Start
from ClassesActeur.Consultant import Consultant
from ClassesActeur.Geographe import Geographe
from ClassesActeur.DataScientist import DataScientist
from ClassesActeur.Admin import Admin
from ClassesActeur.classe_abstraite_connexion import classe_abstraite_connexion
import numpy as np

class Manager:
    """
    Cette classe g-re la relation entre les acteurs et leur taches autorisées
    """
    def __init__(self):
        pass

    def preparer_contexte(self):
        """
        On fait ici l'hypothèse que chaque menu comprenne au moins trois composante:
        -  question: La question à poser qui est une chaine de charactère
        -  options: la liste de possibilités qui est une liste de chaines de charactères
        -  action_options: la liste
        :return:
        """
        menu_actions = {
            "question": "Que désirez-vous faire ?",
            "options": ["Afficher un pays",
                        "Proposer une correction",
                        "Examiner les corrections",
                        "Ajouter un pays",
                        "Modifier un pays",
                        "Supprimer un pays",
                        "Créer un compte",
                        "Supprimer un compte",
                        "Obtenir un résumé d'informations",
                        "Obtenir une représentation graphique",
                        "Accéder à la fonctionnalité avancée",
                        "Quitter"
                        ],
            "action_options": [(lambda memory: memory["acteur"].afficher_pays(memory)),
                               (lambda memory: memory["acteur"].proposer_correction(memory)),
                               (lambda memory: memory["acteur"].accepter_refuser_proposition(memory)),
                               (lambda memory: memory["acteur"].ajouter_pays(memory)),
                               (lambda memory: memory["acteur"].modifier_pays(memory)),
                               (lambda memory: memory["acteur"].supprimer_pays(memory)),
                               (lambda memory: memory["acteur"].creer_compte(memory)),
                               (lambda memory: memory["acteur"].supprimer_compte(memory)),
                               (lambda memory: memory["acteur"].resume_informations(memory)),
                               (lambda memory: memory["acteur"].representation_graphique(memory)),
                               (lambda memory: memory["acteur"].fonc_avancee(memory)),
                               (lambda memory: Close(memory))
                               ]
        }

        nb_actions = len(menu_actions["options"])
        menu_acteurs = {
            "question": "Quel est votre statut?",
            "options": ["Consultant", "Super acteur", "Quitter"],
            "action_options": [lambda a,memory: return (Consultant(a), [0, 1]),
                               lambda a,memory: classe_abstraite_connexion().connexion(memory),
                               #connexion doit donc renvoyer l'acteur et les indices des tâches
                               lambda a,memory: Close(memory)]
        }
        menu_correction = {
            "question": "Acceptez-vous ou refusez-vous la correction ?",
            "options": ["Accepter", "Refuser", "Ne rien faire et quitter"],
            "action_options": [lambda memory: modifier liste_correction et modifier pays,
                               lambda memory: modifier liste_correction,
                               lambda memory: open_menu.Menu(memory)]} #menu pas forcément utile selon la structure de la fonction
       menu_suppression = {
            "question": "Confirmez-vous la suppression du pays ?",
            "options": ["Confirmer et Supprimer", "Abandonner la procédure"],
            "action_options": [lambda memory: suppression,
                               lambda memory: open_menu.Menu(memory)]} #menu pas forcément utile selon la structure de la fonction
       menu_preselection = {
            "question": "Voulez vous modifier la liste préselectionnée ?",
            "options": ["Valider la liste", "Ajouter un pays", "Retirer un pays"],
            "action_options": [lambda memory: lancer le résumé,
                               lambda memory: lancer correction(parametre1),
                               lambda memory: lancer correction(parametre2)]}
        
        return menu_acteurs, menu_actions

    def bienvenu(self):
        # affiche le message de bienvenue
        with open('assets/banner.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def aurevoir(self):
        with open('assets/cat.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def bordure(self):
        with open('assets/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def creat_menu(self, info_menus , auto_iter=False):
        current_vue = Start(info_menus)
        if auto_iter:
            max_iter = np.inf
        else:
            max_iter = 1
        i = 0
        # tant qu'on a un écran à afficher et qu'on n'a pas dépassé le nb max d'iterations, on continue
        while current_vue and (i < max_iter):
            # on affiche une bordure pour séparer les menu
            self.bordure()

            # le menu agit (demande d'action à effectuer, réalisation de l'action, préparation du prochain menu, ...)
            current_vue = current_vue.run()
            i += 1
        return current_vue
