import random

argent = 100
tour = 1
max_tours = 5

print("=== MODE BUSINESS ===")
print(f"Tu démarres avec {argent}$ pour construire ton empire !\n")

while tour <= max_tours:
    print(f"--- Jour {tour} ---")
    print(f"Argent actuel : {argent}$")
    print("1) Investir dans la pub (risqué)")
    print("2) Épargner (sûr)")
    print("3) Embaucher un employé (coûte cher)")
    choix = input("Ton choix : ")

    if choix == "1":
        if random.choice(["gain", "perte"]) == "gain":
            gain = random.randint(30, 80)
            argent += gain
            print(f"La pub a cartonné ! +{gain}$\n")
        else:
            perte = random.randint(20, 50)
            argent -= perte
            print(f"La pub a flop... -{perte}$\n")
    elif choix == "2":
        argent += 15
        print("Épargne tranquille. +15$\n")
    elif choix == "3":
        if argent >= 40:
            argent -= 40
            print("Employé embauché !\n")
        else:
            print("Pas assez d'argent.\n")
    else:
        print("Choix invalide, tour perdu.\n")

    tour += 1

print("=== FIN ===")
print(f"Argent final : {argent}$")

if argent >= 250:
    titre = "🏆 Magnat des affaires !"
elif argent >= 150:
    titre = "🥈 Entrepreneur prometteur"
else:
    titre = "🥉 Petit débutant"

print(f"Récompense : {titre}")

with open("scores.txt", "a") as f:
    f.write(f"Business : {argent}$ - {titre}\n")
