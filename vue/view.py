class IhmMenu:

    @staticmethod
    def saisie_int(message):
        """
        Méthode qui permet de verouiller les saisies int
        :param message: le message écrit
        :return: la saisie en int
        """
        try:
            return int(input(message))
        except ValueError:
            print("attention ce n'est pas un nombre ")
            return IhmMenu.saisie_int(message)

    @staticmethod
    def saisie_int_next_round(message):
        """
        Méthode de la classe IhmMenu qui permet de verouiller les saisies
        entre les rounds
        :param message: le message ecrit
        :return: la saisie en int
        """
        boole = True
        while boole:
            try:
                number = int(input(message))
                if number < 1 or number > 3:
                    print("attention le chiffre n'est pas 1 ou 2 ")
                else:
                    return number
                    boole = False
            except ValueError:
                print("attention ce n'est pas un chiffre ")

    @staticmethod
    def saisie_string(message):
        try:
            return str(input(message))
        except Exception:
            print("what are you fking doing")
            return IhmMenu.saisie_string(message)

    @staticmethod
    def print_string(message):
        """
        Méthode de la classe IhmMenu pour afficher des messages
        :param message: le message écrit
        """
        print(message)

    @staticmethod
    def menu_generale():
        """
        méthode de la classe IhmMenu qui permet d'afficher le menu générale
        """
        print("************BIENVENUE AU TOURNOI D'ECHEC**************\n")
        print("1-Créer et demarrer le tournoi")
        print("2-Reprendre le tournois en cours")
        print("3-Afficher les rapports de fin de tournoi")
        print("4-Changer le classement des joueurs en fin de tournoi")
        print("5-Quitter le programme")

    @staticmethod
    def menu_entrer_joueur():
        """
        Méthode de la classe IhmMenu qui permet d'afficher les inputs des Players
        """
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
        """
        Méthode de la classe IhmMenu qui permet d'afficher les inputs du tournois
        """
        print("******************RENTRER LA DESCRIPTION DU TOURNOI********************\n")
        choix_tournois_nom = IhmMenu.saisie_string("1-Entrer le nom du tournois\n")
        choix_tournois_lieu = IhmMenu.saisie_string("2-Entrer le lieu du tournois\n")
        choix_tournois_date = IhmMenu.saisie_string("3-Entrer la date du tournois\n")
        choix_tournois_time_control = IhmMenu.saisie_string(
            "4-Entrer le time_control du tournois(blitz,bullet,quick)\n")
        choix_tournois_description = IhmMenu.saisie_string("5-Entrer la description du tournois\n")

        list_choix = [choix_tournois_nom, choix_tournois_lieu, choix_tournois_date,
                      choix_tournois_time_control, choix_tournois_description, ]

        return list_choix

    @staticmethod
    def menu_rapport():
        """
        Méthode de la classe IhmMenu qui permet d'afficher la première
        partie du rapport
        """
        print("1-Liste de tous les joueurs par ordre alphabétique")
        print("2-Liste de tous les joueurs par classement")
        print("3-Liste de tous les joueurs par tournois par ordre alphabétique")
        print("4-Liste de tous les joueurs par tournois par classement")
        print("5-Passer à la suite du menu")

    @staticmethod
    def menu_rapport_2():
        """
        Méthode de la classe IhmMenu qui permet d'afficher la deuxième
        partie du rapport
        """
        print("6-Liste de tous les tournois ")
        print("7-Liste de toutes les rounds par tournois ")
        print("8-Liste de tous les matchs par tournois")
        print("9- revenir au menu générale")

    @staticmethod
    def between_round():
        """
        Méthode de la classe IhmMenu qui permet d'afficher le menu
        entre chaque round
        """
        print("1-continuer le tournois")
        print("2-arreter le tournois et quitter le logiciel")
        print("3-Afficher le rapport du tournois en cours")

    @staticmethod
    def change_rank_player():
        choix_nom_famille = IhmMenu.saisie_string("1-Entrer le nom de famille du joueur\n")
        choix_rank = IhmMenu.saisie_int("2-Entrer le nouveau classement du joueur\n")
        list_data = [choix_nom_famille, choix_rank]
        return list_data
