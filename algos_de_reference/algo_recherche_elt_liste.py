def recherche(elt, liste:list) -> int:
    """
    fonction de recherche de elt dans une liste
    """
    for i in range(len(liste)):
        if liste[i] == elt:
            return i
    return -1


# test de la fonction
assert recherche(5,[1,2,4,3,8,7,6,5]) == 7, "Erreur de test != 7"
assert recherche(6,[1,4,2,5,4,2,1,5]) == -1, "Erreur de test != 0"