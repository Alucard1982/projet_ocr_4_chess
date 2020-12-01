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
    def menu_generale():
        print = ("BIENVENUE AU TOUNROIS D'ECHEC\n")
        print("1-Demarrrer le tournois")
        print("2-Afficher les rapport")
        print("3-quitter le programme")



    @staticmethod
    def menu_entrer_joueur():
        print("rentrer les joueurs")
        choix_joueur_nom = IhmMenu.saisie_string("1-Entrer le Prenom du joueur\n")
        choix_joueur_prenom = IhmMenu.saisie_string("2-Entrer le Nom du joueur\n")
        choix_joueur_date = IhmMenu.saisie_string("3-Entrer la date d'anniversaire du joueur\n")
        choix_joueur_sex = IhmMenu.saisie_string("4-Entrer le sex du joueur\n")
        choix_joueur_rank = IhmMenu.saisie_int("5-Enrtrer le rang du joueur\n")

        list_choix = [choix_joueur_nom, choix_joueur_prenom, choix_joueur_date,
                      choix_joueur_sex, choix_joueur_rank]
        return list_choix

    @staticmethod
    def menu_description_tournement():
        choix_tournois_nom = IhmMenu.saisie_string("1-Entrer le nom du tournois\n")
        choix_tournois_lieu = IhmMenu.saisie_string("2-Entrer le lieu du tournois\n")
        choix_tournois_date = IhmMenu.saisie_string("3-Entrer la date du tournois\n")
        choix_tournois_description = IhmMenu.saisie_string("4-Entrer la description du tournois\n")

        list_choix = [choix_tournois_nom , choix_tournois_lieu, choix_tournois_date,
                      choix_tournois_description]
        return list_choix

    @staticmethod
    def menu_rapport():
        pass

    @staticmethod
    def menu_round():
        print("commencer le round")
        print("comment le next_round")