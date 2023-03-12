
age=0;
nom=""

def afficheinfo(nom,age):
    try:
        return("votre nom est : " + nom + " et vous avez " + str(age))
    except ValueError:
        print("vous avez pas d'information")
    

def function_nom():
    nom=""
    while nom=="":
        try:
            nom=input("entrer votre nom: " )
        except ValueError:
            print("votre nom est incorrect")    
    return nom

retun_nom=function_nom()

def function_age(nomparams):
    age=0;
    while age==0:
        ages = input(nomparams + " vous avez quel age : " )
        try:
            age=int(ages)
        except ValueError:
            print("veillez entrer un entier pour votre âge? ")
    return age
        
agess=function_age(retun_nom)
affiche=afficheinfo(retun_nom,agess)
print(affiche)



#on demande le nom et l'age de la personne