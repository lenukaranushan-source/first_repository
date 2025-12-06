import random
ret = 1
choix = input("Souhaitez-vous jouer aux dés ou faire un pile ou face (Dés/Pile ou face)")
if choix == "Dés":
    while ret == 1:
        number = random.randint(1,6)
        print(number)
        rep = input("Souhaitez-vous relancer le dé ? (Oui/Non)")
        if rep == "Oui":
            ret = 1
        else :
            ret = 0
elif choix == "Pile ou face":
    while ret == 1:
        cote = random.randint(0,1)
        if cote == 0:
            print("Pile")
            rep = input("Souhaitez-vous relancer la pièce ? (Oui/Non)")
            if rep == "Oui":
                ret = 1
            else :
                ret = 0
        if cote == 1:
            print("Face")
            rep = input("Souhaitez-vous relancer le dé ? (Oui/Non)")
            if rep == "Oui":
                ret = 1
            else :
                ret = 0