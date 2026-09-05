import os

def afficher_menu():
    print("=== CHALLENGEOF VICENCIA ===")
    print("1) Jeu Business")
    print("2) Jeu Quiz")
    print("3) Mini-défis rapides")
    print("4) Survie")
    print("5) Combat")
    print("6) Quitter")

while True:
    afficher_menu()
    choix = input("Ton choix : ")

    if choix == "1":
        os.system("python business.py")
    elif choix == "2":
        os.system("python quiz.py")
    elif choix == "3":
        os.system("python tiktok.py")
    elif choix == "4":
        os.system("python survie.py")
    elif choix == "5":
        os.system("python combat.py")
    elif choix == "6":
        print("À bientôt !")
        break
    else:
        print("Choix invalide.\n")
