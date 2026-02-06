import mysql.connector

# Connexion à MySQL
connexion = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="tresbienmerci",
    database="centre_formation"
)

curseur = connexion.cursor()


def ajouter_apprenant():
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    promo = input("Promo : ")
    curseur.execute(
        "INSERT INTO apprenants (nom, prenom, promo) VALUES (%s, %s, %s)",
        (nom, prenom, promo)
    )
    connexion.commit()
    print(f"Apprenant {nom} {prenom} ajouté avec succès.")


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