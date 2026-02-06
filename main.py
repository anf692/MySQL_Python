import mysql.connector

# Connexion à MySQL
connexion = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="tresbienmerci",
    database="centre_formation"
)

# Vérifiez si la connexion est réussie
if connexion.is_connected():    
    print("Connecté à la base de données MySQL")
else:    
    print("Échec de la connexion à la base de données MySQL")

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
        promo = input("Entrer votre promo :").strip().upper()
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


#fonction pour enregistrer une presence
def enregistrer_presence():
    curseur.execute("SELECT id, nom, prenom, presence FROM apprenants")
    apprenants = curseur.fetchall()

    for apprenant in apprenants:
        print(f"{apprenant[0]} - {apprenant[1]} {apprenant[2]} : {apprenant[3]}")

        while True:
            pointage = input("Présent ? (o/n) : ").lower()
            if pointage == "o":
                curseur.execute(
                    "UPDATE apprenants SET presence='Présent' WHERE id=%s",
                    (apprenant[0],)
                )
                break

            elif pointage == "n":
                break
            else:
                print("Saisie incorrecte veuillez reessayer!! ")

    connexion.commit()
    print("Présences mises à jour avec succès.")

#fonction pour afficher les presents
def afficher_present():
    curseur.execute("SELECT nom, prenom, promo FROM apprenants WHERE presence='Présent'")
    presents = curseur.fetchall()
    if presents:
        print("Apprenants présents :")
        for p in presents:
            print(f"{p[0]} {p[1]} - {p[2]}")
    else:
        print("Aucun apprenant n'est présent.")


#fonction pour rechercher un apprenant
def rechercher_apprenant():
    while True:
        nom = input("Entrer le nom de l'apprenant a rechercher: ").strip()
        if nom.replace(" ","").isalpha():
            break
        else:
            print("Incorrect ! entrer (seulement des lettres).")

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

#fonction pour supprimer un apprenants
def supprimer_apprenants():
    curseur.execute("SELECT id, nom, prenom FROM apprenants")
    apprenants = curseur.fetchall()

    if not apprenants:
        print("Aucun apprenant à supprimer.")
        return

    print("Liste des apprenants :")
    for a in apprenants:
        print(f"{a[0]} - {a[1]} {a[2]}")

    while True:
        id_app = input("Entrer l'identifiant de l'apprenant à supprimer : ").strip()

        if not id_app.isdigit():
            print("Erreur : l'identifiant doit être un nombre.")
            continue

        # Vérifier l'existence
        curseur.execute(
            "SELECT id FROM apprenants WHERE id = %s",
            (id_app,)
        )
        apprenant = curseur.fetchone()

        if apprenant is None:
            print("Aucun apprenant avec cet ID. Réessayez.")
            continue

        # Supprimer
        curseur.execute(
            "DELETE FROM apprenants WHERE id = %s",
            (id_app,)
        )

        connexion.commit()
        print(f"Utilisateur avec ID {id_app} supprimé avec succès.")
        break


#fonction pour fermer la base de donnnees
def fermeture():
    if connexion.is_connected():
        connexion.close()
        print("Connexion à la base de données MySQL fermée.")

    
#fonction principal
def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Ajouter un apprenant")
        print("2. Enregistrer présence")
        print("3. Afficher présents")
        print("4. Rechercher apprenant")
        print("5. Supprimer un apprenant")
        print("6. Quitter")
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
            supprimer_apprenants()
        elif choix == "6":
            fermeture()
            print("Au revoir 👋")
            break
        else:
            print("Choix invalide, réessayez.")

menu()