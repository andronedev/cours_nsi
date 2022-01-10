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




#Exercice 1

#premier arbre :

N_vide=Arbre()
N_4=Arbre(4)
N_4.assembler(N_vide,N_vide)
N_1=Arbre(1)
N_1.assembler(N_vide,N_vide)
N_2=Arbre(2)
N_2.assembler(N_1,N_4)
print(N_2)

#deuxième arbre, on remarque qu'un de ses sous arbre a déjà été construit,
# il s'agit de l'arbre précédent !

N_6=Arbre(6)
N_7=Arbre(7)
N_7.assembler(N_vide,N_vide)

N_6.assembler(N_vide,N_7)
N_5=Arbre(5)
N_5.assembler(N_2,N_6)
print(N_5)

#troisième arbre :
n_vide=Arbre()
n_0=Arbre(0)
n_0.assembler(n_vide,n_vide)
n_1=Arbre(1)
n_1.assembler(n_vide,n_vide)
n_2=Arbre(2)
n_2.assembler(n_vide,n_vide)
n_3=Arbre(3)
n_4=Arbre(4)
n_5=Arbre(5)
n_6=Arbre(6)
n_7=Arbre(7)
n_7.assembler(n_vide,n_vide)
n_8=Arbre(8)
n_8.assembler(n_vide,n_vide)
n_9=Arbre(9)
n_9.assembler(n_vide,n_2)
n_3.assembler(n_0,n_9)
n_6.assembler(n_1,n_7)
n_4.assembler(n_8,n_6)
n_5.assembler(n_4,n_3)
print(n_5)

#exercice 2 : méthode taille : nombre de noeuds de l'arbre
# Pour calculer le nombre de noeuds d'un arbre, on ajoute 1 au le nombre
# de noeud du sad et celui du sag. On utilise donc une programmation récursive.
# Si l'arbre est vide, on retourne 0

#exercice 3 : méthode hauteur : hauteur de l'arbre
# Pour calculer la hauteur d'un arbre, on ajoute 1 à la valeur la plus grande entre
# la hauteur du sad et celle du sag. On utilise donc une programmation récursive.
# Si l'arbre est vide, on retourne -1

#exercice 4 : feuilles
# pour savoir si un noeud est une feuille, on teste si son sad et son sag sont vide.
# Pour calculer le noombre de feuilles, on ajoute le nombre de feuilles du sad
# et celles du sag. On utilise donc une programmation récursive.
# Si le noeud est une feuille on retourne 1

#exercice 5 - parcours en profondeur d'un arbre

