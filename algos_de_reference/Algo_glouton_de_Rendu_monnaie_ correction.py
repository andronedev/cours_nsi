# valeurs des pièces
systeme_monnaie = [1,2,5,10,20,50,100]

def pieces_a_rendre(somme_a_rendre, systeme_monnaie):

    # liste des pièces à rendre, initialement vide
    lst_pieces = []

    # La première pièce à rendre est potentiellement la dernière pièce
    # du tableau systeme_monnaie. Une variable i de type entier est
    # initialisée avec l’indice du dernier élément de ce tableau
    # indice de la première pièce comparée à la somme à rendre
    i = len(systeme_monnaie) - 1

    # boucle de construction de la liste des pièces :
    # Chaque fois qu’une pièce de systeme_monnaie n’est plus utilisable, la valeur 
    # de i sera diminuée de 1. Le programme s’arrête quand i atteint la valeur 0.
    # Ce qui mène à l’écriture d’une boucle conditionnelle pour remplir la liste
    # des pièces choisies. 

    while somme_a_rendre > 0:
        valeur = systeme_monnaie[i]
        if somme_a_rendre < valeur:
            i = i - 1
        else:
            lst_pieces.append(valeur)
            somme_a_rendre = somme_a_rendre - valeur
    return lst_pieces