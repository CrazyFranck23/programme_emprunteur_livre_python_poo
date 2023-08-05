import re
import datetime
from emprunteur import Emprunteur

print("""       Bonjour et bienvenue ! """)


choice = 0
while choice == 0:
    choice = input("Voulez vous ajouter un nouvel emprunteur (oui ou non) ? ")
    if choice == 'oui':
        # Boucle qui demande à l'utilisateur de ressaisir son nom et prenom au cas où il fait une saisie vide ou
        # s'il saisit des chiffres, nombres.. etc
        while True:
            nom = input("Veuillez saisir le nom de l'emprunteur : ")
            prenom = input("Veuillez saisir le prénom de l'emprunteur : ")
            if not nom or not prenom:
                print("Erreur : le nom et le prénom ne peuvent pas être vides. Veuillez réessayer.")
            elif not nom.isalpha() or not prenom.isalpha():
                print("Erreur : le nom et le prénom ne doivent contenir que des lettres. Veuillez réessayer.")
            else:
                break

        # Boucle qui demande à l'utilisateur de ressaisir l'email au cas où il fait une saisie incorrecte
        while True:
            email = input("Veuillez saisir l'adresse e-mail de l'emprunteur : ")
            # Utilisation d'une expression reguliere pour verifier le format de l'adresse email
            if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                break
            else:
                print("Erreur : l'adresse e-mail saisie n'est pas valide. Veuillez réessayer.")

        # Boucle qui demande à l'utilisateur de ressaisir la date d'inscription au cas où il fait une saisie incorrecte
        while True:
            date_inscription = input("Veuillez saisir la date d'inscription au format dd/mm/yyyy : ")
            try:
                day, month, year = date_inscription.split('/')
                date = f"{day}/{month}/{year}"
                # Vérification que la date est valide
                datetime.datetime.strptime(date, '%d/%m/%Y')
                break
            except ValueError:
                print("Erreur : la date saisie n'est pas au format dd/mm/yyyy. Veuillez réessayer.")

        # Boucle qui demande à l'utilisateur de ressaisir le nom du livre au cas où il fait un saisi vide
        while True:
            livre_emprunte = input("Veuillez saisir le nom du livre emprunte : ")
            if not livre_emprunte:
                print("Erreur : le nom du livre emprunte ne peut pas être vide. Veuillez réessayer.")
            else:
                break

        emprunteur1 = Emprunteur(nom, prenom, email, date_inscription, livre_emprunte)
        print()
        choice = 0
    elif choice == 'non':
        print()
        choice3 = input("Voulez-vous voir la liste des emprunteurs (oui ou non) ? ")
        if choice3 == 'oui':
            Emprunteur.afficher_emprunteurs()
            print()
            print("Au revoir !")
        else:
            print("Au revoir !")
    else:
        print("Vous devez choisir uniquement entre < oui > et < non >.")
        print()
        choice = 0