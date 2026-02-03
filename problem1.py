def analyser_phrase(phrase):
    # la je mets tout la phrase en minuscule
    phrase = phrase.lower()

    # pour decouper la phrase en mot
    mots = phrase.split()

    # pour compter le nombre total de mot
    nombre_mots = len(mots)

    # Trouver le mot le plus long
    mot_plus_long = ""
    for mot in mots:
        if len(mot) > len(mot_plus_long):
            mot_plus_long = mot

    # Compter le nombre de voyelles
    voyelles = "aeiouy"
    nombre_voyelles = 0
    for lettre in phrase:
        if lettre in voyelles:
            nombre_voyelles += 1

    # Construire une nouvelle phrase
    nouvelle_phrase = []
    for mot in mots:
        if len(mot) % 2 == 0:          # longueur paire
            nouvelle_phrase.append(mot.upper())
        else:                          # longueur impaire
            nouvelle_phrase.append(mot)

    # Retourner les résultats
    return nombre_mots, mot_plus_long, nombre_voyelles, " ".join(nouvelle_phrase)


# Programme principal
phrase_utilisateur = input("Entre une phrase : ")

nb_mots, mot_long, nb_voyelles, phrase_finale = analyser_phrase(phrase_utilisateur)

print("Nombre total de mots :", nb_mots)
print("Mot le plus long :", mot_long)
print("Nombre total de voyelles :", nb_voyelles)
print("Nouvelle phrase :", phrase_finale)
