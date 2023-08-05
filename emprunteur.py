
class Emprunteur:
    liste_emprunteur = []

    def __init__(self, nom, prenom, email, date_inscription, livre_emprunte):
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.date_inscription = date_inscription
        self.livre_emprunte = livre_emprunte
        Emprunteur.liste_emprunteur.append(self)

    def afficher_infos(self):
        print("Nom :", self.nom)
        print("Prenom :", self.prenom)
        print("Email :", self.email)
        print("Date d'inscription :", self.date_inscription)
        print("Livre emprunte :", self.livre_emprunte)

    @classmethod
    def afficher_emprunteurs(cls):
        for emprunteur in cls.liste_emprunteur:
            emprunteur.afficher_infos()
            print()
        print("Nombre total d'emprunteurs :", len(cls.liste_emprunteur))