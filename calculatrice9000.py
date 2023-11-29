def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b 

def division(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Division par zéro")

def calculatrice():
    # permette a la function de se lancer en boucle
    while True:

        # Demander à l'utilisateur les informations nécessaires
        nombre1 = float(input("Entrez le premier nombre : "))
        operateur = input("Entrez l'opérateur (+, -, *, /) : ")
        nombre2 = float(input("Entrez le deuxième nombre : "))

        # Effectuer l'opération en fonction de l'opérateur
        if operateur == '+':
            resultat = addition(nombre1, nombre2)
        elif operateur == '-': 
            resultat = soustraction(nombre1, nombre2)
        elif operateur == '*':
            resultat = multiplication(nombre1, nombre2)
        elif operateur == '/':
            resultat = division(nombre1, nombre2)
        else:
            raise ValueError("Opérateur non valide")

        # Afficher le résultat
        print(f"Le résultat de {nombre1} {operateur} {nombre2} est : {resultat}")

calculatrice()
