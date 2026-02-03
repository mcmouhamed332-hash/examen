import turtle
import random

# Création de l’écran
ecran = turtle.Screen()
ecran.setup(800, 800)
ecran.title("Formes géométriques aléatoires")

# Création du crayon
t = turtle.Turtle()
t.speed(0)
t.width(2)

# Se déplacer vers une position aléatoire à l’écran
def position_aleatoire():
    x = random.randint(-350, 350)
    y = random.randint(-350, 350)
    t.penup()
    t.goto(x, y)
    t.pendown()

# Choisir une couleur au hasard
def couleur_aleatoire():
    t.color(random.random(), random.random(), random.random())

# Dessiner un carré
def dessiner_carre():
    taille = random.randint(20, 400)
    for _ in range(4):
        t.forward(taille)
        t.right(90)

# Dessiner un triangle
def dessiner_triangle():
    taille = random.randint(20, 400)
    for _ in range(3):
        t.forward(taille)
        t.left(120)

# Dessiner un cercle
def dessiner_cercle():
    rayon = random.randint(20, 200)
    t.circle(rayon)

# Demande du nombre de formes
N = int(input("Entrez un nombre entier entre 0 et 9 : "))

# Dessin des formes
for _ in range(N):
    position_aleatoire()
    couleur_aleatoire()

    forme = random.choice(["carre", "triangle", "cercle"])

    if forme == "carre":
        dessiner_carre()
    elif forme == "triangle":
        dessiner_triangle()
    else:
        dessiner_cercle()

# Garder la fenêtre ouverte
turtle.done()
