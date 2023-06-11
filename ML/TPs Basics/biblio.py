def somme(a,b):
    return(a+b)
    
def mul(a,b):
    return(a*b)
    
def sous(a,b):
    return(a-b)
    
def div(a,b):
    if (type(a)==int and type(b)==int):
        return(a/b)
    else:
        raise Exception("cette fonction n'accepte que les entiers")

def isFile(fname):
    try:
        f_log = open(fname,'r') #essaie d'ouvrir fname
        f_log.close() #puis le ferme
        return (fname,True) #le fichier existe et retourne son nom et True
    except IOError:
        return (fname,False)#le fichier n'existe pas et retourne False
