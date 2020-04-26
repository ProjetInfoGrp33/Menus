from menu.close_menu import Close
from menu.start import Start
from metier.acteur import Acteur
from metier.data_manimulation import DataManipulation
from metier.super_acteur import SuperActeur
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
            "action_options": [(lambda memory: DataManipulation(memory).add_data()),
                               (lambda memory: DataManipulation(memory).remove_last_data()),
                               (lambda memory: DataManipulation(memory).print_statistics()),
                               (lambda memory: Close(memory))
                               ]
        }

        nb_actions = len(menu_actions["options"])
        menu_acteurs = {
            "question": "Quel est votre statut?",
            "options": ["Consultant", "Super acteur", "Quitter"],
            "action_options": [lambda memory: Consultant(1).set_indices_taches([0, 1]),
                               lambda memory: classe_abstraite_connexion.connexion(),
                               #connexion doit donc renvoyer les indices des tâches
                               lambda memory: Close(memory)]
        }
        menu_correction = {
            "question": "Acceptez-vous ou refusez-vous la correction ?",
            "options": ["Accepter", "Refuser", "Ne rien faire et quitter"],
            "action_options": [lambda memory: modifier liste_correction et modifier pays,
                               lambda memory: modifier liste_correction,
                               lambda memory: menu_actions.run()]}
       menu_suppression = {
            "question": "Confirmez-vous la suppression du pays ?",
            "options": ["Confirmer et Supprimer", "Abandonner la procédure"],
            "action_options": [lambda memory: suppression,
                               lambda memory: menu_actions.run()]}
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