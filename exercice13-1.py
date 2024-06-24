import random
player = {
    "nom": input("Entrez votre nom : "),
    "niveau": int(input("Entrez votre niveau : ")),
    "attaque": 2,
    "resistance": 1,
    "pv": 10
    }
robot = {
    "nom": (input("Entrez le nom de votre adversaire : ")),
    "niveau": int(input("Entrez le niveau de votre adversaire : ")),
    "attaque": random.randint(0, 5),
    "resistance": random.randint(0, 5),
    "pv": random.randint(5, 20)
    }
print(f"Profil de {player['nom']}:\n Niveau {player['niveau']}\n {player['pv']} points de vie\n {player['attaque']} points d'attaque\n {player['resistance']} points de résistance")
print(f"Profil de {robot['nom']}:\n Niveau {robot['niveau']}\n {robot['pv']} points de vie\n {robot['attaque']} points d'attaque\n {robot['resistance']} points de résistance")
while player['pv'] > 0 and robot['pv'] > 0:
    player['pv'] -= max(0, robot['attaque'] - player['resistance'])
    if player['pv'] <= 0:
        print(f"Votre adversaire {robot['nom']} vous a vaincu! Dommage...")
        break
    robot['pv'] -= max(0, player['attaque'] - robot['resistance'])
    if robot['pv'] <= 0:
        print(f"Bravo {player['nom']} a perdu le combat!")
        break