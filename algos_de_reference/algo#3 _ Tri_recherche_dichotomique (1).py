def test_liste_triee(L):
    for i in range(len(L)-1):
        if L[i]>L[i+1]:
            return False
    return True

def recherche_dichotomique(L:list,elt:int):
    '''
    fonction qui reçoit en argument une liste et un element
    et qui retourne l'indice de l'élément s'il est présent
    dans une liste par dichotomie et -1 sinon.
    '''
    #preconditions
    assert len(L)>0,"erreur liste vide"
    assert test_liste_triee(L), "liste non triée"
    assert type(elt)==int, "element recherché non entier"

    indice_debut=0
    indice_fin=len(L)-1


    while indice_fin-indice_debut>=0:
        indice_milieu=(indice_debut+indice_fin)//2
        if elt==L[indice_milieu]:
            return indice_milieu
        elif elt>L[indice_milieu] :
            indice_debut=indice_milieu + 1
        else :
            indice_fin=indice_milieu - 1


    return -1


L1=[2,15,26,53,64,69,78,88,91,101,145,156]

#Tests : on teste les "valeurs limites", liste avec 1 seul élément
assert recherche_dichotomique(L1,156)==11,'erreur'
assert recherche_dichotomique(L1,2)==0,'erreur'
assert recherche_dichotomique(L1,69)==5,'erreur'
assert recherche_dichotomique(L1,300)==-1,'erreur'
assert recherche_dichotomique([1],0)==-1,'erreur'
assert recherche_dichotomique([1],1)==0,'erreur'
