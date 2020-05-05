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

    def run(self,memory):
        json = json.dumps(memory["data"])
        f = open("BaseDeDonnees\\data_propre.json","w")
        f.write(json)
        f.close()
        json = json.dumps(memory["Corrections"])
        f = open("corrections.json","w")
        f.write(json)
        f.close()
        json = json.dumps(memory["Liste_comptes"])
        f = open("Liste_comptes.json","w")
        f.write(json)
        f.close()
        return None
