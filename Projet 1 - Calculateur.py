retour = 1
while retour == 1:
    nombre_1 = float(input("Entrez le premier nombre :"))
    operation = input("Entrez l'opération souhaité (+, -, *, /) :")
    nombre_2 = float(input("Entrez le second nombre :"))
    if operation == "+":
        resultat = nombre_1+nombre_2
        print("Le résultat est ", resultat)
        reponse = input("Souhaitez-vous faire un autre calcul ? (Oui/Non)")
        if reponse == "Oui":
            retour = 1
        else:
            retour = 0
    elif operation == "-":
        resultat = nombre_1-nombre_2
        print("Le résultat est ", resultat)
        reponse = input("Souhaitez-vous faire un autre calcul ? (Oui/Non)")
        if reponse == "Oui":
            retour = 1
        else:
            retour = 0
    elif operation == "*":
        resultat = nombre_1*nombre_2
        print("Le résultat est ", resultat)
        reponse = input("Souhaitez-vous faire un autre calcul ? (Oui/Non)")
        if reponse == "Oui":
            retour = 1
        else:
            retour = 0
    elif operation == "/":
        resultat = nombre_1/nombre_2
        print("Le résultat est ", resultat)
        reponse = input("Souhaitez-vous faire un autre calcul ? (Oui/Non)")
        if reponse == "Oui":
            retour = 1
        else:
            retour = 0
    else:
        print("L'opération souhaitée n'est pas reconnue ou n'est pas disponible.")
        reponse = input("Souhaitez-vous faire un autre calcul ? (Oui/Non)")
        if reponse == "Oui":
            retour = 1
        else:
            retour = 0