import random
import time

defis = [
    "Tape le mot 'BANANE' le plus vite possible",
    "Trouve un animal qui commence par 'L'",
    "Cite une couleur en 3 secondes",
    "Tape n'importe quel nombre pair",
]

points = 0
print("=== MODE MINI-DÉFIS ===\n")

random.shuffle(defis)
for defi in defis[:3]:
    print(defi)
    debut = time.time()
    input("Ta réponse : ")
    duree = time.time() - debut
    if duree <= 4:
        print(f"Rapide ! ({duree:.1f}s) +15 points\n")
        points += 15
    else:
        print(f"Un peu lent ({duree:.1f}s) +5 points\n")
        points += 5

print("=== FIN ===")
print(f"Score : {points} points")

if points >= 40:
    titre = "🏆 Roi de la rapidité !"
elif points >= 20:
    titre = "🥈 Assez rapide"
else:
    titre = "🥉 Prends ton temps"

print(f"Récompense : {titre}")

with open("scores.txt", "a") as f:
    f.write(f"Mini-défis : {points} pts - {titre}\n")   
      
