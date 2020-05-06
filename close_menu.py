#!/usr/bin/commandes.txt
# -*- coding: utf-8 -*-
"""menu de fermeture

Affiche un message d'aurevoir.
Pourrait sauvegarder des données mais ne fait rien de tel pour l'instant.
"""
import json
from Menus.abstract_vue import AbstractVue



class Close(AbstractVue):
    """menu de fermeture

    Affiche un message d'aurevoir.
    Pourrait sauvegarder des données mais ne fait rien de tel pour l'instant.
    """

    def __init__(self, memory):
        """construction du menu

        :param memory: mémoire stockant les données de la session
        :type memory: Dictionnaire
        """
        super().__init__(memory)

    def run(self):
        data = json.dumps(self.memory["data"])
        f = open("BaseDeDonnees\\data_propre.json","w")
        f.write(data)
        f.close()
        correction = json.dumps(self.memory["Corrections"])
        f = open("BaseDeDonnees\\corrections.json","w")
        f.write(correction)
        f.close()
        liste_comptes = json.dumps(self.memory["Liste_comptes"])
        f = open("BaseDeDonnees\\Liste_comptes.json","w")
        f.write(liste_comptes)
        f.close()
        return None
