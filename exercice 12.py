import random
state = "lost"
prenom = input("Entrez votre prénom : ")
nom = input("Entrez votre nom :")
while state == "lost":
    nombre_ordi = random.randint(1, 50)
    nombre_utilisateur = int(input("Choisissez un nombre entre 1 et 50: "))
    if nombre_utilisateur > 50 or nombre_utilisateur < 1:
        print("Le nombre doit être compris entre 1 et 50.")
        nombre_utilisateur = int(input("Choisissez un nombre entre 1 et 50: "))

    print(f"Vous avez choisit le nombre {nombre_utilisateur}.")
    for i in range(1, 10):
            if nombre_utilisateur < nombre_ordi:
                print("C'est plus")
            else:
                print("C'est moins")
            nombre_utilisateur = int(input("Choisissez un nombre entre 1 et 50: "))
            if nombre_utilisateur == nombre_ordi:
                print(f"Vous avez gagné {nom} {prenom} Bravo!!!")
                state = "won"
                break
    else:
            print(f"Vous avez perdu {nom} {prenom} dommage")
            state = "lost"