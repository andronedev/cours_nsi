# Créé par bourgf, le 24/09/2021 en Python 3.7
Liste01 = [101,115,30,63,47,20]

def Tri_Selection(Liste_Ini:list) ->list:
    '''
    Fonction qui reçoit en argument une liste
    et qui retourne en sortie une liste triée par la méthode
    de sélection.
    '''
    # test pour s'assurer que la liste de départ n'est pas vide
    assert len(Liste_Ini)>0, 'Liste vide'

    for i in range(0,len(Liste_Ini)-1):

        # on cherche le plus petit élément de la liste
        # pour les éléments d'indice i à la fin de la liste

        min = Liste_Ini[i]
        indice = i

        for k in range(i+1,len(Liste_Ini)):
            if Liste_Ini[k] < min :
                min = Liste_Ini[k]
                indice = k

        # on met en position i le min qui était à la position
        # stocké dans la variable indice et on le permute
        # avec l'autre élément

        temp = Liste_Ini[i]
        Liste_Ini[i] = min
        Liste_Ini[indice] = temp
    return(Liste_Ini)

Liste01 = [101,115,30,63,47,20]
print(Liste01)
Tri_Selection(Liste01)
print(Liste01)
