liste = ["bonjour", "au revoir", "bonsoir", "bonne nuit", "salut"]
dictionnaire = {"nom": "Berthodin", "prenom": "Paul", "age": 16, "ville": "Lyon"}

for _ in range(5):
    print("Je teste la boucle")

for _ in range(10):
    print("Je teste la boucle")

for element in liste:
    print(element)

for cle, valeur in dictionnaire.items():
    print(f"{cle}: {valeur}")