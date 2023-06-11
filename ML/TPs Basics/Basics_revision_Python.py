# Mise en données sous forme d'un dictionnaire
# Clé       : question
# Attributs : Liste de réponses dont seulement une est correcte

#q1: -1, q2:-6, q3:-3, q4:un antécédent de 9 par f, q5:f(x) = 4x²–12x–7
#q6: f(x) = (2x–7)(2x+1), q7: -47, q8:(0;-1), q9: parallèles, q10: sécantes

quiz_2de={"Soit f la fonction affine définie par f(x) = -x + 2. Quel est son coefficient directeur ?":["4/3","-1","1","-2"],
              "f est définie par f(x)=x^2−6x+2.L'image de 2 par f est":["2","-6","6","-2"],
              "f est définie par f(x)=x^2−6x+2.L'image de −1 par f est":["9","-5","-3","4"],
              "f est définie par f(x)=x^3+1. 2 est":["un antécédent de 9 par f","l'image de 9 par f","est un antécédent de 5 par f","l'image de 5 par f"],
              "On considére la fonction f(x) = (2x–3)²–16 Après développement on obtient :":["f(x) = 2x²–12x–7","f(x) = 4x²–12x–7","f(x) = 4x²–25","f(x) = 9x²–69"],
              "On considére la fonction f(x) = (2x–3)²–16 Après factorisation on obtient :":["f(x) = (4x–34)²"," f(x) = (2x–19)(2x+13)"," f(x) = (2x–19)²"," f(x) = (2x–7)(2x+1)"],
              "On considére la fonction f(x) = (2x–3)²–16 L'image de –2 par f est :":["33","-47","1","13"],
              "On considére la fonction f(x) = x²–1. Parmi ces points lquel appartient à la courbe de f :":["(0;-1)"," (-1;0)","(0;0)","(1;1)"],
              "Les droite D1 : y=-2x+3 et D2:y=-2x+1 sont :":["parallèles","perpendiculaires","sécantes","On ne peut pas savoir"],
              "Les droite D1 : y=-2x+3 et D2:y=-0.5x+1 sont :":["perpendiculaires","parallèles","sécantes","On ne peut pas savoir"]
              }
bonnes_rep=[2,3,3,1,1,2,1,4,3,1]
reponses=[]
num_quest=1
score=0
for c,v in quiz_2de.items():
    print("question "+str(num_quest)+" : "+c)
    num_quest+=1
    num_rep=1
    for r in v:
        print(str(num_rep)+" : "+r)
        num_rep+=1
        
    rep=input("la reponse est :")
    
    if (rep.isdigit()): rep=int(rep) #tester si la reponse saisie est nulle si non la convertir en un entier

  
    while (  not(isinstance(rep, int)) or (rep<1) or (rep>4)  ):
        rep=input("la reponse est :")
        if (rep.isdigit()): rep=int(rep) #tester si la reponse saisie est nulle si non la convertir en un entier
     
    
    reponses.append(rep)
   
    
for i in range(0,len(bonnes_rep)-1):
    if (reponses[i]==bonnes_rep[i]):
        score+=1

print("tu as obtenu " + str(score)+" /13")
        
    
    