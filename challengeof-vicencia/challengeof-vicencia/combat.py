import random

vie_joueur = 100
vie_boss = 100
tour = 1

print("=== MODE COMBAT ===")
print("Un boss redoutable apparaît devant toi !\n")

while vie_joueur > 0 and vie_boss > 0:
    print(f"--- Tour {tour} ---")
    print(f"Ta vie : {vie_joueur} | Vie du boss : {vie_boss}")
    print("1) Attaque normale  2) Attaque puissante (risquée)  3) Se soigner")
    choix = input("Ton choix : ")

    if choix == "1":
        degats = random.randint(10, 20)
        vie_boss -= degats
        print(f"Tu infliges {degats} dégâts !\n")
    elif choix == "2":
        if random.random() < 0.6:
            degats = random.randint(25, 40)
            vie_boss -= degats
            print(f"Coup critique ! {degats} dégâts !\n")
        else:
            print("Raté ! Ton attaque échoue.\n")
    elif choix == "3":
        soin = random.randint(15, 25)
        vie_joueur = min(100, vie_joueur + soin)
        print(f"Tu récupères {soin} de vie.\n")
    else:
        print("Choix invalide, tu perds ton tour.\n")

    if vie_boss > 0:
        degats_boss = random.randint(10, 25)
        vie_joueur -= degats_boss
        print(f"Le boss t'inflige {degats_boss} dégâts !\n")

    tour += 1

print("=== FIN DU COMBAT ===")
if vie_joueur <= 0:
    print("💀 Tu as été vaincu...")
    titre = "🥉 Combattant tombé"
else:
    print("🎉 Tu as vaincu le boss !")
    titre = "🏆 Champion du combat !"

print(f"Récompense : {titre}")

with open("scores.txt", "a") as f:
    f.write(f"Combat : {titre}\n")

