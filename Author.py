#!/usr/bin/env python3
 
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 11:40:16 2020

@author:ZineEddine & Libasse
"""
#Classe author qui contient les différentes méthodes
class Author():
    #initialiser l'objet
    def __init__(self,name):
        self.name = name
        self.production = {}
        self.ndoc = 0
        
    def add(self, doc):     
        self.production[self.ndoc] = doc
        self.ndoc += 1
        #méthode str permet d'afficher le nom de l'autheur et le nombre de documents ou son nom est apparue 
    def __str__(self):
        return "Auteur: " + self.name + ", Number of docs: "+ str(self.ndoc)
    #return son nom
    def __repr__(self):
        return self.name
    
    
author = Author("Julien")
print(author)
    