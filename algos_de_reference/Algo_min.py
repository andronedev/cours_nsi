def min(L:list):
    '''
    algo de recherche du min d'une liste
    '''
    #préconditions
    assert len(L)>0,'liste vide'
    min = L[0]
    for i in range(1,len(L)):
        if min > L[i]:
            min = L[i]
    return min

#Tests
assert min([2,3,6,1,4,12,11])==1,'erreur'
assert min([1,2,3])==1,'erreur'
assert min([3,2,1])==1,'erreur'