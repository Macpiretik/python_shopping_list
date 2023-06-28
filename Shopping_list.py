import sys
import json
import os.path

CUR_DIR= os.path.dirname(__file__)

liste_json= CUR_DIR + "/" + "shopping-list.json"

LISTE = []

if os.path.isfile(liste_json) :
    with open(liste_json, "r", encoding='utf-8') as f:
        LISTE = json.load(f)

MENU = """Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Sauvegarder et quitter
👉 Votre choix : """

MENU_CHOICES = ["1", "2", "3", "4", "5"]



while True:
    user_choice = ""
    while user_choice not in MENU_CHOICES:
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICES:
            print("Veuillez choisir une option valide...")

    if user_choice == "1":  # Ajouter un élément
        item = input("Entrez le nom d'un élément à ajouter à la liste de courses : ").capitalize()
        LISTE.append(item)
        print(f"L'élément {item} a bien été ajouté à la liste.")
    elif user_choice == "2":  # Retirer un élément
        item = input("Entrez le nom d'un élément à retirer de la liste de courses : ").capitalize()
        if item in LISTE:
            LISTE.remove(item)
            print(f"L'élément {item} a bien été supprimé de la liste.")
        else:
            print(f"L'élément {item} n'est pas dans la liste.")
    elif user_choice == "3":  # Afficher la liste
        if LISTE:
            print("Voici le contenu de votre liste :")
            for i, item in enumerate(LISTE, 1):
                print(f"{i}. {item}")
        else:
            print("Votre liste ne contient aucun élément.")
    elif user_choice == "4":  # Vider la liste
        LISTE.clear()
        print("La liste a été vidée de son contenu.")
    elif user_choice == "5":  # Quitter
        with open(liste_json, "w") as f:
            json.dump(LISTE, f,indent=4)
        print("À bientôt !")
        sys.exit()

    print("-" * 50)