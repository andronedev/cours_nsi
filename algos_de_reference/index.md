# TAD Arbre[E]

[Raw](algos_de_reference/Algo_references_poo_arbre_binaire.py)

```python
# TAD Arbre[E]
#
# premières Opérations
#       créerArbre: → Arbre[E]]
#       assembler :Arbre[E]x Arbre[E] → Arbre[E]
#       estVide : Arbre[E] → Booléen
#       racine : Arbre[E] → E
#       sag : Arbre[E] → Arbre[E]
#       sad: Arbre[E] → Arbre[E]




class Arbre:

    # créerArbre: → Arbre[E]
    def __init__(self,valeur=None):
        self._racine = valeur
        self._gauche=None
        self._droit=None

    # assembler :Arbre[E]x Arbre[E] → Arbre[E]
    def assembler(self,ag,ad):
        self._gauche=ag
        self._droit=ad

    # estVide : Arbre[E] → Booléen
    def estVide(self):
        return self._racine is None


    # racine : Arbre[E] → E
    def racine(self):
        assert not self.estVide(), "l'arbre est vide"
        return self._racine

    # sag : Arbre[E] → Arbre[E]
    def sag(self):
        assert not self.estVide(), "l'arbre est vide"
        return self._gauche

    # sad: Arbre[E] → Arbre[E]
    def sad(self):
        assert not self.estVide(), "l'arbre est vide"
        return self._droit

    # retourne une chaine de caractères représentative de l'état de l'instance
    def __str__(self):
        return "({},{},{})".format(self._gauche, self._racine, self._droit)

    # donne le schéma de construction de l'instance
    def __repr__(self):
        return "Arbre()"

    def taille(self):
        if self.estVide():
            return 0
        else :
            return 1 + self._gauche.taille() + self._droit.taille()


    def hauteur(self):
        if self.estVide():
            return -1
        else :
            return 1 + max(self._gauche.hauteur(),self._droit.hauteur())


    def feuille(self):
        assert not self.estVide(), "l'arbre est vide"
        if self.sag().estVide() and self.sag().estVide() :
            return True
        else:
            return False

    def compte_feuille(self):
        assert not self.estVide(), "l'arbre est vide"
        if self.feuille():
            return 1
        else :
            return self.sag().compte_feuille() + self.sad().compte_feuille()


    def parcours_prefixe(self):
        if self.estVide():
            return
        else :
            print(self.racine())
            self.sag().parcours_prefixe()
            self.sad().parcours_prefixe()

    def parcours_infixe(self):
        if self.estVide():
            return
        else :
            self.sag().parcours_infixe()
            print(self.racine())
            self.sad().parcours_infixe()


    def parcours_suffixe(self):
        if self.estVide():
            return
        else :

            self.sag().parcours_suffixe()
            self.sad().parcours_suffixe()
            print(self.racine() ,end=' ')
```

# Algo glouton de Rendu monnaie

[Raw](../Algo_glouton_de_Rendu_monnaie.py)

```python
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
```

# Algo min.py

[Raw](./Algo_min.py)

```python
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
```

# Algo recherche d'un élément dans une liste

[Raw](./algo_recherche_elt_liste.py)

```python
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
```

# Tri recherche dichotomique

[Raw](./algo_tri_recherche_dichotomique.py)

```python
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
```

# Tri insertion

[Raw](./Tri_insertion.py)

```python

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
```

# Tri par selection

[Raw](./Tri_selection.py)

```python
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

```