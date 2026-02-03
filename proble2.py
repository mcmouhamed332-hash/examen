students = [
    ("ali", 12),
    ("fatou", 17),
    ("moussa", 9),
    ("awa", 14),
    ("ibrahim", 7)
]

# la j'affiche les etudiants et leurs notes
def afficher_etudiants(liste):
    for nom, note in liste:
        print(nom, ":", note)

# la je fait le calcule de notes 
def analyser_notes(liste):
    total = 0
    notes = []
    admis = []
    ajournes = []

    for nom, note in liste:
        total += note
        notes.append(note)

        if note >= 10:
            admis.append(nom)
        else:
            ajournes.append(nom)

    moyenne = total / len(liste)
    note_max = max(notes)
    note_min = min(notes)

    admis.sort()

    print("\nMoyenne de la classe :", moyenne)
    print("Note maximale :", note_max)
    print("Note minimale :", note_min)

    print("\nÉtudiants admis :", admis)
    print("Étudiants ajournés :", ajournes)

    print("\nNoms des étudiants admis (ordre alphabétique) :", admis)


# Programme principal
print("Liste des étudiants et leurs notes :")
afficher_etudiants(students)

analyser_notes(students)
