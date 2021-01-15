# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 10:34:17 2020

@author: ZineEddine & Libasse
"""

# package permettant d'incrémenter l'identifiant unique à attribuer à un document
 

from Class_Document import Document
class RedditDocument(Document):
    
    def __init__(self, date, title, author, text, url, nb_comments):
        super().__init__(date, title, author ,text, url)
        self.nb_comments = nb_comments
        self.source = "Reddit"
    
    # getters
    def get_comments(self):
        return self.nb_comments
    
    def get_Type():
        return "REDDIT"
      
    def __str__(self):
        return super().__str__(self) + "[" + str(self.nb_comments) + "commentaires ]"   
    

class ArxivDocument(Document):
    
    def __init__(self, date, title, author, text, url, co_authors):
        super().__init__(date, title, author ,text, url)
        self.co_authors = co_authors
        self.source = "Arxiv"
    
    # getters
    def get_size_coAuthors(self):
        if self.co_authors is None:
            return(0)
        return (len(self.co_authors) - 1)
    
    def get_coAuthors(self):
        if self.co_authors is None:
            return([])
        return self.co_authors
    
    def get_Type():
        return "ARXIV"

    def __str__(self):
        
        string = super().__str__(self)
        
        if(self.get_size_coAuthors() > 0):
            return string + "[" + str(self.get_size_coAuthors()) + " co-Authors ]"   

        return string    

            
    
