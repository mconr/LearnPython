from biblio import *


f=open("test_fichier.txt","w")

f.write("premiere ligne \n")
f.write("deuxieme ligne \n")
f.write("troisieme ligne \n")

f.close()

#similaire  a

with open("test_fichier.txt","w") as f:
    f.write("premiere ligne \n")
    f.write("deuxieme ligne \n")
    f.write("troisieme ligne \n")

f=open("test_fichier.txt","r")
    

z=f.readline()

print("z")
print(z)

y=f.read(5)

print("y")
print(y)

x=f.readlines()
print("X")
for i in x:
    print(i)


f.close()

F= isFile("test_fichier.txt")
print(F)