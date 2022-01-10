
L1 = [20, 101, 115, 30, 63, 47, 20]
print(L1)

def Tri_Insertion(List:list)->list:
    '''
    Fonction qui reçoit en argument un liste et qui
    la retourne triée par ordre croissant avec la méthode
    d'insertion
    '''
    # On vérifie que la liste à trier est non vide
    assert len(List)>0,'Liste vide'

    # on parcourt les elt de la liste jusqu'à en trouver un
    # qui est n'est pas trié

    for i in range(len(List)):
        k=i-1
        elt_a_trier = List[i]
        # on décale vers la droite tous les termes triés
        #pour insérer elt_non_tri à sa place

        while elt_a_trier < List[k] and k>=0 :
            List[k+1]=List[k]
            k=k-1
        List[k+1]= elt_a_trier

    return(List)

print(Tri_Insertion(L1))

