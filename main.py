import mysql.connector

# Connexion à MySQL
connexion = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="passe",
    database="centre_formation"
)

curseur = connexion.cursor()


#fonction pour ajouter un apprenant
def ajouter_apprenant():

    while True:
        nom = input("Entrer votre nom : ").strip()
        if nom.replace(" ","").isalpha():
            break
        else:
            print("Incorrect ! Entrez votre nom (seulement des lettres).")

    while True:
        prenom = input("Entrer votre prénom : ").strip()
        if prenom.replace(" ","").isalpha():
            break
        else:
            print("Incorrect ! Entrez votre prénom (seulement des lettres).")

    while True:
        promo = input("Entrer votre promo :").strip()
        if promo.startswith("P") and promo[1:].isdigit():
            break
        else:
            print("Incorrect ! La promo doit commencer par 'P' suivi uniquement de chiffres.")


    curseur.execute(
        "INSERT INTO apprenants (nom, prenom, promo) VALUES (%s, %s, %s)",
        (nom, prenom, promo)
    )

    connexion.commit()
    print(f"Apprenant {prenom} {nom}  ajouté avec succès.")


def enregistrer_presence():
    curseur.execute("SELECT id, nom, prenom, presence FROM apprenants")
    apprenants = curseur.fetchall()
    for apprenant in apprenants:
        print(f"{apprenant[0]} - {apprenant[1]} {apprenant[2]} : {apprenant[3]}")
        rep = input("Présent ? (o/n) : ").lower()
        if rep == "o":
            curseur.execute(
                "UPDATE apprenants SET presence='Présent' WHERE id=%s",
                (apprenant[0],)
            )
    connexion.commit()
    print("Présences mises à jour avec succès.")


def afficher_present():
    curseur.execute("SELECT nom, prenom, promo FROM apprenants WHERE presence='Présent'")
    presents = curseur.fetchall()
    if presents:
        print("Apprenants présents :")
        for p in presents:
            print(f"{p[0]} {p[1]} - {p[2]}")
    else:
        print("Aucun apprenant n'est présent.")


def rechercher_apprenant():
    nom = input("Nom de l'apprenant à rechercher : ")
    curseur.execute(
        "SELECT * FROM apprenants WHERE nom LIKE %s",
        (f"%{nom}%",)
    )
    result = curseur.fetchall()
    if result:
        for r in result:
            print(f"ID: {r[0]}, Nom: {r[1]}, Prénom: {r[2]}, Promo: {r[3]}, Présence: {r[4]}")
    else:
        print("Aucun apprenant trouvé.")

    
def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Ajouter un apprenant")
        print("2. Enregistrer présence")
        print("3. Afficher présents")
        print("4. Rechercher apprenant")
        print("5. Quitter")
        choix = input("Votre choix : ")
        if choix == "1":
            ajouter_apprenant()
        elif choix == "2":
            enregistrer_presence()
        elif choix == "3":
            afficher_present()
        elif choix == "4":
            rechercher_apprenant()
        elif choix == "5":
            print("Au revoir 👋")
            break
        else:
            print("Choix invalide, réessayez.")

menu()