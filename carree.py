import turtle

t=turtle.Turtle()

def carree(n):
    for i in range(1,5):
     t.forward(n)
     t.left(90)
#carree(50)

def carrees(taille,nbr):
    for i in range(1,5):
        taille=i*taille
        carree(taille)
carrees(25,5)   
#pour garder la fenetre ouverte
turtle.done()