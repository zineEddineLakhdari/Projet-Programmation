# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 16:38:54 2021

@author: ZineEddine & Libasse
"""
import unittest
from datetime import datetime

 
# Le code à tester doit être importable. On
# verra dans une autre partie comment organiser
# son projet pour cela.
from Corpus import Corpus
from Author import Author
from Class_Document import Document 
from Document import RedditDocument 
from Document import ArxivDocument

 
# Cette classe est un groupe de tests. Son nom DOIT commencer
# par 'Test' et la classe DOIT hériter de unittest.TestCase.
class TestUnitaire(unittest.TestCase):
 
    # Chaque méthode dont le nom commence par 'test_' est un test.
    def test_Document(self):
        
        doc = Document(datetime.now(), 'Lyon2', 'Velcin', 'Projet M2 Python', 'http://export.arxiv.org/api/query')

        chaine = 'Lyon2'
        le_test = doc.get_title()
        secon_test = doc.get_text()
 
        # Le test le plus simple est un test d'égalité. On se
        # sert de la méthode assertEqual pour dire que l'on
        # s'attend à ce que les deux éléments soient égaux. Sinon le test échoue.
        self.assertEqual(le_test, chaine)
        self.assertEqual(secon_test, 'Projet M2 Python')
        
    def test_Document2(self):
        
        doc = Document(datetime.now(), 'Lyon2', 'Velcin', 'Projet M2 Python', 'http://export.arxiv.org/api/query')
        secon_test = doc.get_text()
        self.assertEqual(secon_test, 'Projet M2 Python')
        
    def test_Author(self):
        
        libasse =  Author("Libasse")
        mboup = libasse.__repr__()
        self.assertEqual(mboup, "Libasse")
    
    def test_Corpus(self):
        
        corpus = Corpus("sénégal")
        string = "projet|88python``motivant^doing;en-janvier2021[]"
        chaine = corpus.nettoyer_texte(string)
        self.assertEqual(chaine, "projet python motivant doing en janvier ")
        
     
    def test_Arxiv(self):
        
        arxiv = ArxivDocument(datetime.now(), 'Lyon2', 'Velcin', 'Projet M2 Python', 'http://export.arxiv.org/api/query',{'mboup','lakhdari', 'velcin', 'gourru' })
        x = arxiv.get_size_coAuthors()
        self.assertTrue(x, 3)
        
    def test_Reddit(self):
        
        reddit = RedditDocument(datetime.now(), 'Lyon2', 'Velcin', 'Projet M2 Python', 'http://export.arxiv.org/api/query',18)
        x = reddit.get_comments()
        self.assertTrue(x, 18)   
        
    def test_print(self):
        
        author = Author("Julien") 
        author.add("Machine Learning")
        author.add("POO")
        self.assertTrue(author.__str__(), 'Auteur: Julien, Number of docs: 2')
        
# Ceci lance le test si on exécute le script
# directement.
if __name__ == '__main__':
    unittest.main()