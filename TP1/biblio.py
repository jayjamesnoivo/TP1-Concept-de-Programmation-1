# === SYSTÈME DE GESTION DE BIBLIOTHÈQUE PERSONNELLE ===
# Contraintes respectées :
# - Utilisation de for, while
# - Utilisation de break, continue, pass
# - Utilisation de range() et enumerate()
# - if / elif / else, opérateurs logiques
# - AUCUNE fonction personnalisée (pas de def)
# - AUCUNE classe
# - AUCUN import

# ----------------------------
# PARTIE 1 : Initialisation
# ----------------------------
livres = [
    {"titre": "Harry Potter", "auteur": "JK Rowling", "statut": "disponible", "note": 5},
    {"titre": "1984", "auteur": "George Orwell", "statut": "emprunté", "note": 4},
    {"titre": "Le Seigneur des Anneaux", "auteur": "J.R.R. Tolkien", "statut": "disponible", "note": 5},
    {"titre": "Fahrenheit 451", "auteur": "Ray Bradbury", "statut": "disponible", "note": 3},
    {"titre": "Fondation", "auteur": "Isaac Asimov", "statut": "emprunté", "note": 4},
]

MAX_EMPRUNTS = 3  # limite d’emprunts simultanés

# ----------------------------
# PARTIE 3 : Boucle principale (while)
# ----------------------------
while True:
    print("\n=== MA BIBLIOTHÈQUE PERSONNELLE ===")
    print("1. Afficher tous les livres")
    print("2. Afficher seulement les livres disponibles")
    print("3. Recherche par titre")
    print("4. Recherche par auteur")
    print("5. Afficher les livres empruntés")
    print("6. Statistiques (total / disponibles / empruntés)")
    print("7. Emprunter un livre")
    print("8. Retourner un livre")
    print("9. Rapports + Top 3 (range / enumerate)")
    print("10. Défi 1 : Livres bien notés (4+)")
    print("11. Défi 2 : Recherche avancée (titre ET auteur)")
    print("12. Défi 3 : Sauvegarde de session (résumé)")
    print("0. Quitter")

    choix = input("\nVotre choix : ")

    # ----------------------------
    # QUITTER (utilise break)
    # ----------------------------
    if choix == "0":
        print("Au revoir !")
        break  # sortir de la boucle principale

    # ----------------------------
    # OPTION 1 : Tous les livres (Partie 1)
    # ----------------------------
    elif choix == "1":
        print("\n--- TOUS LES LIVRES ---")
        # enumerate pour liste numérotée
        for index, livre in enumerate(livres, start=1):
            print(f"{index}. {livre['titre']} - {livre['auteur']} [{livre['statut'].upper()}] (note: {livre['note']}/5)")

    # ----------------------------
    # OPTION 2 : Livres disponibles (Partie 1)
    # ----------------------------
    elif choix == "2":
        print("\n--- LIVRES DISPONIBLES ---")
        trouve = False
        for index, livre in enumerate(livres, start=1):
            if livre["statut"] == "disponible":
                print(f"{index}. {livre['titre']} - {livre['auteur']} [DISPONIBLE]")
                trouve = True
        if not trouve:
            print("Aucun livre disponible pour le moment.")

    # ----------------------------
    # OPTION 3 : Recherche par titre (Partie 2)
    # ----------------------------
    elif choix == "3":
        recherche = input("Entrez une partie du titre : ").lower()
        print(f"\n--- RECHERCHE PAR TITRE contenant '{recherche}' ---")
        trouve = False
        for livre in livres:
            if recherche in livre["titre"].lower():
                print(f"- {livre['titre']} - {livre['auteur']} [{livre['statut'].upper()}]")
                trouve = True
        if not trouve:
            print("Aucun livre ne correspond à cette recherche de titre.")

    # ----------------------------
    # OPTION 4 : Recherche par auteur (Partie 2)
    # ----------------------------
    elif choix == "4":
        auteur_recherche = input("Entrez le nom de l'auteur : ").lower()
        print(f"\n--- RECHERCHE PAR AUTEUR '{auteur_recherche}' ---")
        trouve = False
        for livre in livres:
            if auteur_recherche in livre["auteur"].lower():
                print(f"- {livre['titre']} - {livre['auteur']} [{livre['statut'].upper()}]")
                trouve = True
        if not trouve:
            print("Aucun livre trouvé pour cet auteur.")

    # ----------------------------
    # OPTION 5 : Afficher les livres empruntés (Partie 2)
    # ----------------------------
    elif choix == "5":
        print("\n--- LIVRES EMPRUNTÉS ---")
        trouve = False
        for livre in livres:
            if livre["statut"] == "emprunté":
                print(f"- {livre['titre']} - {livre['auteur']} [EMPRUNTÉ]")
                trouve = True
        if not trouve:
            print("Aucun livre n'est emprunté.")

    # ----------------------------
    # OPTION 6 : Statistiques (Partie 2 + 4)
    # ----------------------------
    elif choix == "6":
        total = len(livres)
        dispo = 0
        empruntes = 0

        for livre in livres:
            if livre["statut"] == "disponible":
                dispo += 1
            elif livre["statut"] == "emprunté":
                empruntes += 1
            else:
                # utilisation de pass pour un cas inattendu
                pass

        print("\n--- STATISTIQUES ---")
        print(f"Total livres   : {total}")
        print(f"Disponibles    : {dispo}")
        print(f"Empruntés      : {empruntes}")

    # ----------------------------
    # OPTION 7 : Emprunter un livre (Partie 3)
    # ----------------------------
    elif choix == "7":
        # calcul des livres déjà empruntés
        nb_empruntes = 0
        for livre in livres:
            if livre["statut"] == "emprunté":
                nb_empruntes += 1

        if nb_empruntes >= MAX_EMPRUNTS:
            print(f"\nVous avez atteint la limite d'emprunts ({MAX_EMPRUNTS}).")
            # continue : on revient au menu
            continue

        titre_emprunt = input("Entrez le titre du livre à emprunter : ").lower()
        trouve = False

        for livre in livres:
            if titre_emprunt in livre["titre"].lower():
                trouve = True
                if livre["statut"] == "disponible":
                    livre["statut"] = "emprunté"
                    print(f"Vous avez emprunté : {livre['titre']}")
                else:
                    print("Ce livre est déjà emprunté.")
                # break : on sort de la boucle dès qu'on a trouvé
                break

        if not trouve:
            print("Aucun livre ne correspond à ce titre pour l'emprunt.")

    # ----------------------------
    # OPTION 8 : Retourner un livre (Partie 3)
    # ----------------------------
    elif choix == "8":
        titre_retour = input("Entrez le titre du livre à retourner : ").lower()
        trouve = False
        for livre in livres:
            if titre_retour in livre["titre"].lower():
                trouve = True
                if livre["statut"] == "emprunté":
                    livre["statut"] = "disponible"
                    print(f"Vous avez retourné : {livre['titre']}")
                else:
                    print("Ce livre n'est pas emprunté.")
                break
        if not trouve:
            print("Aucun livre ne correspond à ce titre pour le retour.")

    # ----------------------------
    # OPTION 9 : Rapports + Top 3 (Partie 4 : range + enumerate)
    # ----------------------------
    elif choix == "9":
        print("\n--- LISTE NUMÉROTÉE (enumerate) ---")
        for i, livre in enumerate(livres, start=1):
            print(f"{i}. {livre['titre']} - {livre['auteur']} [{livre['statut'].upper()}]")

        print("\n--- TOP 3 DES LIVRES (simulation avec range) ---")
        limite = 3
        if len(livres) < 3:
            limite = len(livres)

        for i in range(limite):
            livre = livres[i]
            print(f"Top {i+1} : {livre['titre']} - {livre['auteur']} (note: {livre['note']}/5)")

    # ----------------------------
    # OPTION 10 : Défi 1 – Livres bien notés (≥ 4/5)
    # ----------------------------
    elif choix == "10":
        print("\n--- LIVRES BIEN NOTÉS (note >= 4) ---")
        somme_notes = 0
        nb_notes = 0
        trouve = False

        for livre in livres:
            note = livre["note"]
            somme_notes += note
            nb_notes += 1

            if note >= 4:
                trouve = True
                print(f"- {livre['titre']} (note: {note}/5)")

        if not trouve:
            print("Aucun livre n'a une note supérieure ou égale à 4.")

        if nb_notes > 0:
            moyenne = somme_notes / nb_notes
            print(f"\nNote moyenne de la bibliothèque : {moyenne:.2f}/5")
        else:
            print("\nAucune note disponible pour calculer une moyenne.")

    # ----------------------------
    # OPTION 11 : Défi 2 – Recherche avancée (titre ET/OU auteur)
    # ----------------------------
    elif choix == "11":
        print("\n--- RECHERCHE AVANCÉE (TITRE ET/OU AUTEUR) ---")
        crit_titre = input("Entrez une partie du titre (laisser vide si aucun critère) : ").lower()
        crit_auteur = input("Entrez une partie du nom de l'auteur (laisser vide si aucun critère) : ").lower()

        trouve = False

        for livre in livres:
            titre_ok = True
            auteur_ok = True

            # Si un critère de titre est donné, il doit être respecté
            if crit_titre != "":
                titre_ok = crit_titre in livre["titre"].lower()

            # Si un critère d'auteur est donné, il doit être respecté
            if crit_auteur != "":
                auteur_ok = crit_auteur in livre["auteur"].lower()

            # Les deux critères doivent être vrais si renseignés
            if titre_ok and auteur_ok:
                print(f"- {livre['titre']} - {livre['auteur']} [{livre['statut'].upper()}] (note: {livre['note']}/5)")
                trouve = True

        if not trouve:
            print("Aucun livre ne correspond aux critères avancés.")

    # ----------------------------
    # OPTION 12 : Défi 3 – Sauvegarde de session
    # ----------------------------
    elif choix == "12":
        print("\n========== SAUVEGARDE DE SESSION (SIMULÉE) ==========")

        total = len(livres)
        dispo = 0
        empruntes = 0
        somme_notes = 0
        nb_notes = 0

        for livre in livres:
            if livre["statut"] == "disponible":
                dispo += 1
            elif livre["statut"] == "emprunté":
                empruntes += 1
            else:
                pass

            somme_notes += livre["note"]
            nb_notes += 1

        print(f"Total de livres           : {total}")
        print(f"Livres disponibles        : {dispo}")
        print(f"Livres empruntés          : {empruntes}")

        if nb_notes > 0:
            moyenne = somme_notes / nb_notes
            print(f"Note moyenne globale      : {moyenne:.2f}/5")
        else:
            print("Note moyenne globale      : N/A")

        print("\n--- DÉTAIL DES LIVRES ---")
        for i, livre in enumerate(livres, start=1):
            print(f"{i}. {livre['titre']} - {livre['auteur']} [{livre['statut'].upper()}] (note: {livre['note']}/5)")

        print("\n--- LISTE DES LIVRES EMPRUNTÉS ---")
        un_emprunte = False
        for livre in livres:
            if livre["statut"] == "emprunté":
                print(f"- {livre['titre']} - {livre['auteur']} (note: {livre['note']}/5)")
                un_emprunte = True
        if not un_emprunte:
            print("Aucun livre n'est actuellement emprunté.")

        print("\n=== FIN DE LA SAUVEGARDE (AFFICHAGE SIMULÉ) ===")

    # ----------------------------
    # OPTION NON RECONNUE
    # ----------------------------
    else:
        print("Choix invalide. Veuillez réessayer.")
