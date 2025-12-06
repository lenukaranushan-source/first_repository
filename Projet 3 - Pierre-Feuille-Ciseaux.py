import random
ret2 = 1
while ret2 == 1:
    ret = int(input("En combien de manches souhaitez-vous jouer ?"))
    ret1 = ret
    score = 0
    score_r = 0
    while ret > 0:
        num = random.randint(1,3)
# Coup du robot : Pierre
        if num == 1:
            print("Le robot a choisi son coup.")
            coup = input("Quel coup souhaitez-vous jouer ? (Pierre/Feuille/Ciseaux)")
            if coup == "Pierre":
                print("Le robot avait joué pierre. Vous avez joué pierre. C'est une égalité.")
                score += 0
                score_r += 0
                ret -= 1
            elif coup == "Feuille":
                print("Le robot avait joué pierre. Vous avez joué feuille. Vous avez gagné la manche !")
                score += 1
                score_r -= 1
                ret -= 1
            elif coup == "Ciseaux":
                print("Le robot avait joué pierre. Vous avez joué ciseaux. Vous avez perdu la manche !")
                score -= 1
                score_r += 1
                ret -= 1
            else:
                print("Le coup joué n'est pas reconnu")
# Coup du robot : Feuille
        elif num == 2:
            print("Le robot a choisi son coup.")
            coup = input("Quel coup souhaitez-vous jouer ? (Pierre/Feuille/Ciseaux)")
            if coup == "Pierre":
                print("Le robot avait joué feuille. Vous avez joué pierre. Vous avez perdu la manche !")
                score -= 1
                score_r += 1
                ret -= 1
            elif coup == "Feuille":
                print("Le robot avait joué feuille. Vous avez joué feuille. C'est une égalité.")
                score += 0
                score_r += 0
                ret -= 1
            elif coup == "Ciseaux":
                print("Le robot avait joué feuille. Vous avez joué ciseaux. Vous avez gagné la manche !")
                score += 1
                score_r -= 1
                ret -= 1
            else:
                print("Le coup joué n'est pas reconnu")
# Coup du robot : Ciseaux
        elif num == 3:
            print("Le robot a choisi son coup.")
            coup = input("Quel coup souhaitez-vous jouer ? (Pierre/Feuille/Ciseaux)")
            if coup == "Pierre":
                print("Le robot avait joué ciseaux. Vous avez joué pierre. Vous avez gagné la manche !")
                score += 1
                score_r -= 1
                ret -= 1
            elif coup == "Feuille":
                print("Le robot avait joué ciseaux. Vous avez joué feuille. Vous avez perdu la manche !")
                score -= 1
                score_r += 1
                ret -= 1
            elif coup == "Ciseaux":
                print("Le robot avait joué ciseaux. Vous avez joué ciseaux. C'est une égalité.")
                score += 0
                score_r += 0
                ret -= 1
            else:
                print("Le coup joué n'est pas reconnu")
    print("Votre score est de", score)
    print("Le score du robot est de", score_r)
    ratio = (score/ret1)*100
    print("Votre taux de victoire est de", ratio,"%")
    rep = input("Souhaitez-vous refaire une partie ? (Oui/Non)")
    if rep == "Oui":
        ret2 = 1
    else: 
        ret2 = 0