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
