from IncorrectCodePostal import *

class Adresse:
    def __init__(self, r, v, cp):
        self.__rue=r
        self.__ville=v
        if (len(cp)!=5):
            #exception personalisé
            
            #methode 1
            raise IncorrectCodePostal(cp)
            
            #methode 2
            raise Exception("le code postale doit contenir exactement 5 chiffres")
        self.__code_postale=cp


