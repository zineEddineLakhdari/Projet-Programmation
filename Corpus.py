# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 10:51:50 2020

@author: ZineEddine
"""

import pickle
import re

from Author import Author
from Class_Document import Document


class Corpus():
    #methode init du corpus
    def __init__(self,name):
        self.name = name
        self.collection = {}
        self.authors = {}
        self.id2doc = {}
        self.id2aut = {}
        self.ndoc = 0
        self.naut = 0
    #methode ajout d'un document     
    def add_doc(self, doc):
        
        self.collection[self.ndoc] = doc
        self.id2doc[self.ndoc] = doc.get_title()
        self.ndoc += 1
        aut_name = doc.get_author()
        aut = self.get_aut2id(aut_name)
        if aut is not None:
            self.authors[aut].add(doc)
        else:
            self.add_aut(aut_name,doc)
    #methode ajout d'un autheur        
    def add_aut(self, aut_name,doc):
        
        aut_temp = Author(aut_name)
        aut_temp.add(doc)
        
        self.authors[self.naut] = aut_temp
        self.id2aut[self.naut] = aut_name
        
        self.naut += 1
    #methode retourn l'id de l'auteur selon son nom
    def get_aut2id(self, author_name):
        aut2id = {v: k for k, v in self.id2aut.items()}
        heidi = aut2id.get(author_name)
        return heidi
    #method pour récupérer le document selon un indice 
    def get_doc(self, i):
        return self.collection[i]
    #methode permet de récupérer la collection notre dictionnaire
    def get_coll(self):
        return self.collection
    #
    def __str__(self):
        return "Corpus: " + self.name + ", Number of docs: "+ str(self.ndoc)+ ", Number of authors: "+ str(self.naut)
    #
    def __repr__(self):
        return self.name
   #methode pour ordonné les titres
    def sort_title(self,nreturn=None):
        if nreturn is None:
            nreturn = self.ndoc
        return [self.collection[k] for k, v in sorted(self.collection.items(), key=lambda item: item[1].get_title())][:(nreturn)]
    #méthode pour ordonné les dates
    def sort_date(self,nreturn):
        if nreturn is None:
            nreturn = self.ndoc
        return [self.collection[k] for k, v in sorted(self.collection.items(), key=lambda item: item[1].get_date(), reverse=True)][:(nreturn)]
    #methode pour écrire dans un fichier
    def save(self,file):
            pickle.dump(self, open(file, "wb" ))
     #methode pour nettoyer le corpus   
    def nettoyer(self,txt):
        text=txt.lower()
        text=text.replace('\n','')
        text=text.replace("']",' ')
      
        while "\%'" in text:
            text=text.replace("\%", ' ')
        text=text.replace("\textit{viz.}",' ')

        return text
    #methode pour chercher dans le corpus le mot key passer en paramètre 
    def search(self, key):
        occAll=0 
        txt = self.get_coll()
        newCorpus="\t"
        corpus=[]
       
        for i in range(len(txt)):
             corpus.append([])     
             
        for cle,valeur in txt.items():
            text=self.nettoyer(str(valeur.get_text()))
            newCorpus=newCorpus+str(text)
            corpus[cle].append(str(text))
        i=0
        while(i<len(corpus)):
             
            for line in re.findall(key+".*", str(*corpus[i])):
                if(line!=None):
                    occAll=occAll+1
                    print("Document : "+str(i)+" Line  : \n")
                    print(line)
                
            i=i+1
        print(occAll)