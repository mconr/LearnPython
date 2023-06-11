from biblio import *
from Adresse import *

try :
    #essayer d'executer la fonction div(a,b)
    x=div('e',2)
    print(x)
    
#lors d'une division par 0
except ZeroDivisionError as e:
    print(e)
    
#lorsqu'il y'a une exception de type
except ValueError as e:
    print(e)
    
# tout type d'erreur
except Exception as e:
    print(e)
    
#pas de division par 0
else:
    print("pas d'exception")
#dans tous les cas
finally:    
    print("FIN")
    
    
    
try:
    adr= Adresse("gueliz","marrakech","123")
except Exception as e:
    print(e)