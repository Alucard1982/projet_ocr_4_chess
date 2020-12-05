class IhmMenu:

    @staticmethod
    def saisie_int(message):
        try:
            return int(input(message))
        except ValueError:
            print("attention ce n'est pas un nombre ")
            return IhmMenu.saisie_int(message)

    @staticmethod
    def saisie_string(message):
        try:
            return str(input(message))
        except Exception:
            print("what are you fking doing")
            return IhmMenu.saisie_string(message)

    @staticmethod
    def print_string(message):
        print(message)



    @staticmethod
    def menu_generale():
        print("************BIENVENUE AU TOURNOIS D'ECHEC**************\n")
        print("1-Créer et demarrer le tournois")
        print("2-Afficher les rapports")
        print("3-Quitter le programme")



    @staticmethod
    def menu_entrer_joueur():
        print("***************RENTRER LES JOUEURS*************")
        choix_joueur_nom = IhmMenu.saisie_string("1-Entrer le Prenom du joueur\n")
        choix_joueur_prenom = IhmMenu.saisie_string("2-Entrer le Nom du joueur\n")
        choix_joueur_date = IhmMenu.saisie_string("3-Entrer la date d'anniversaire du joueur\n")
        choix_joueur_sex = IhmMenu.saisie_string("4-Entrer le sex du joueur\n")
        choix_joueur_rank = IhmMenu.saisie_int("5-Entrer le rang du joueur\n")
        choix_joueur_id = IhmMenu.saisie_int("6-Entrer l'id du joueur\n")

        list_choix = [choix_joueur_nom, choix_joueur_prenom, choix_joueur_date,
                      choix_joueur_sex, choix_joueur_rank, choix_joueur_id]
        return list_choix

    @staticmethod
    def menu_description_tournement():
        print("******************WELCOME TO THE TOURNEMENT SOFTWARE********************\n")
        choix_tournois_nom = IhmMenu.saisie_string("1-Entrer le nom du tournois\n")
        choix_tournois_lieu = IhmMenu.saisie_string("2-Entrer le lieu du tournois\n")
        choix_tournois_date = IhmMenu.saisie_string("3-Entrer la date du tournois\n")
        choix_tournois_time_control = IhmMenu.saisie_string(
            "4-Entrer le time_control du tournois(blitz,bullet,quick)\n")
        choix_tournois_description = IhmMenu.saisie_string("5-Entrer la description du tournois\n")

        list_choix = [choix_tournois_nom , choix_tournois_lieu, choix_tournois_date,
                      choix_tournois_time_control, choix_tournois_description, ]

        return list_choix

    @staticmethod
    def menu_rapport():
        print("1-Liste de tous les joueurs par ordre alphabétique")
        print("2-Liste de tous les joueurs par classement")
        print("3-Liste de tous les joueurs par tournois par ordre alphabétique")
        print("4-Liste de tous les joueurs par tournois par classement")
        print("5-Liste de tous les tournois ")
        print("6-Liste de toutes les rounds par tournois ")
        print("7-Liste de tous les matchs par tournois")
        print("8- revenir au menu générale")


