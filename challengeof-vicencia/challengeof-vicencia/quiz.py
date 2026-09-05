questions = [
    {"q": "Quelle est la capitale de la France ?", "r": "paris"},
    {"q": "Combien font 5 x 6 ?", "r": "30"},
    {"q": "Quel langage utilises-tu pour coder ce jeu ?", "r": "python"},
    {"q": "Quelle planète est surnommée la planète rouge ?", "r": "mars"},
]

points = 0

print("=== MODE QUIZ ===\n")

for item in questions:
    reponse = input(item["q"] + " ")
    if reponse.lower().strip() == item["r"]:
        print("Correct ! +10 points\n")
        points += 10
    else:
        print(f"Faux, c'était {item['r']}.\n")

print("=== FIN DU QUIZ ===")
print(f"Score : {points}/{len(questions)*10}")

if points == len(questions) * 10:
    titre = "🏆 Génie du quiz !"
elif points >= len(questions) * 5:
    titre = "🥈 Bien joué"
else:
    titre = "🥉 Peut mieux faire"

print(f"Récompense : {titre}")

with open("scores.txt", "a") as f:
    f.write(f"Quiz : {points} pts - {titre}\n")
