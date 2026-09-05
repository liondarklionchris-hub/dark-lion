import random

vie = 100
tour = 1
points = 0

print("=== MODE SURVIE ===")
print("Tu dois survivre 5 tours en évitant les dangers !\n")

while tour <= 5 and vie > 0:
    print(f"--- Tour {tour} --- Vie : {vie}")
    evenement = random.choice(["danger", "objet", "rien"])

    if evenement == "danger":
        print("⚠️ Un obstacle apparaît !")
        choix = input("1) Esquiver  2) Foncer\nTon choix : ")
        if choix == "1":
            print("Esquivé de justesse !\n")
            points += 10
        else:
            degats = random.randint(10, 30)
            vie -= degats
            print(f"Aïe ! -{degats} vie\n")

    elif evenement == "objet":
        print("✨ Tu trouves un objet !")
        choix = input("1) Le ramasser  2) Ignorer\nTon choix : ")
        if choix == "1":
            gain = random.randint(10, 20)
            vie = min(100, vie + gain)
            points += 5
            print(f"+{gain} vie récupérée !\n")
        else:
            print("Tu continues ton chemin.\n")
    else:
        print("Rien de spécial ce tour-ci.\n")

    tour += 1

print("=== FIN ===")
if vie <= 0:
    print("💀 Tu n'as pas survécu...")
    titre = "🥉 Éliminé"
else:
    print(f"Tu as survécu ! Vie restante : {vie}, Points : {points}")
    if points >= 30:
        titre = "🏆 Survivant légendaire !"
    elif points >= 15:
        titre = "🥈 Bon survivant"
    else:
        titre = "🥉 Survivant chanceux"

print(f"Récompense : {titre}")

with open("scores.txt", "a") as f:
    f.write(f"Survie : {points} pts - {titre}\n")

