import random
import os

def charger_profil():
    if os.path.exists("profil_joueur.txt"):
        with open("profil_joueur.txt", "r") as fichier:
            profil = eval(fichier.read())
        print(f"Heureux de vous revoir {profil['nom']}")
    else:
        profil = {
            "nom": input("Entrez votre nom : "),
            "niveau": int(input("Entrez votre niveau (entre 1 et 10): ")),
            "attaque": 2,
            "resistance": 1,
            "pv": 10,
            "pv_debut": 10
        }
    return profil

def sauvegarder_profil(profil):
    with open("profil_joueur.txt", "w") as fichier:
        fichier.write(str(profil))

def creer_robot():
    return {
        "nom": "Robot",
        "niveau": random.randint(1, 10),
        "attaque": random.randint(0, 5),
        "resistance": random.randint(0, 5),
        "pv": random.randint(5, 20)
    }

def afficher_profil(profil):
    print(f"Profil de {profil['nom']}:\n Niveau {profil['niveau']}\n {profil['pv']} points de vie\n {profil['attaque']} points d'attaque\n {profil['resistance']} points de résistance")

def combat(player, robot):
    while player['pv'] > 0 and robot['pv'] > 0:
        player['pv'] -= max(0, robot['attaque'] - player['resistance'])
        if player['pv'] <= 0:
            print(f"Votre adversaire {robot['nom']} vous a vaincu! Dommage...")
            return False
        robot['pv'] -= max(0, player['attaque'] - robot['resistance'])
        if robot['pv'] <= 0:
            print(f"Bravo {player['nom']}, vous avez gagné le combat!")
            player['pv'] = player['pv_debut'] 
            player['attaque'] += random.randint(1, 3)
            player['resistance'] += random.randint(1, 3)
            return True

player = charger_profil()
afficher_profil(player)

continuer = True
while continuer:
    robot = creer_robot()
    afficher_profil(robot)
    victoire = combat(player, robot)
    if victoire:
        sauvegarder_profil(player)
        choix = input("Voulez-vous continuer les combats? (oui/non) ")
        if choix.lower() != "oui":
            continuer = False
            os.remove("profil_joueur.txt")
    else:
        print("Vous avez perdu le combat!")
        sauvegarder_profil(player)
        recommencer = input("Voulez-vous recommencer? (oui/non) ")
        if recommencer.lower() != "oui":
            continuer = False
            break
        else:
            os.remove("profil_joueur.txt")
            print("Votre profil a été supprimé. Vous pouvez recommencer.")
            break