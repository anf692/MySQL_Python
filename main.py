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