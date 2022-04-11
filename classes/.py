import mysql.connector

class ManageDatas:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost",user="root",password="", database="gestion_Patients")
        # connexion à la base de donnée
        self.curseurBDD = self.conn.cursor()

    def afficher_donnees_patient(self, patient):
        # methode pour afficher les données d'un patient en prenant en compte son id
        instructionBDD = f"SELECT * FROM patient WHERE id_patient = {patient}"
        self.curseurBDD.execute(instructionBDD)
        dictionnaire_retour = {}
        index = 1
        # creration variable index = 1 correspond au numero du patient
        for ligne in self.curseurBDD:
            dictionnaire_ligne = {}
            dictionnaire_ligne["patient"] = index
            dictionnaire_ligne["nom"] = ligne[2]
            dictionnaire_ligne["prenom"] = ligne[3]
            dictionnaire_ligne["age"] = ligne[4]
            #dictionnaire_ligne["sejour"] = ligne[5]
            #dictionnaire_ligne["date_entree"] = ligne[6]
            #dictionnaire_ligne["date_sortie"] = ligne[7]
            #dictionnaire_ligne["probleme"] = ligne[8]
            dictionnaire_retour[index] = dictionnaire_ligne
            index += 1  # incrémente le numero d'intervention
        return dictionnaire_retour

    def ajouter_patient(self, nom, prenom, date):
        # int id_patient /str nom et prenom/date datenaissance
        # methode pour ajouter un patient
        instructionBDD = f"INSERT INTO Patient (nom, prenom, dateNaissance) " \
                         f"VALUES ('{nom}', '{prenom}', {date};)"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()

    def supprimer_patient(self, patient):
        # methode pour supprimer un patient de la bdd avec en argument l'id du patient
        instructionBDD = f"DELETE * FROM patient Where idPatient = {patient}"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()
        # si on veut aller plus loin, on peut garder les données pour les insérer dans une base de donnée dite "archive"

    def modifier_patient(self, patient, nom, prenom, date):
    # int id_patient /str nom et prenom/date datenaissance
    # methode pour modifier un patient en prenant en compte son id
        instructionBDD = f"UPDATE patient set nom = '{nom}', prenom = '{prenom}', dateNaissance = '{date}' where idPatient = {patient};"

        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()

    def ajouter_service(self, nom, zone):
        # int id_sejour /str nom et zone géographique
        # methode pour ajouter un service

        instructionBDD = f"INSERT INTO Service (nomService, ZoneGeographique) " \
                         f"VALUES ('{nom}', '{zone}';)"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()

    def supprimer_service(self, service):
        # methode pour supprimer un service de la bdd en prenant en compte son id
        instructionBDD = f"DELETE * FROM service Where idService = {service}"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()
        #si on veut aller plus loin, on peut garder les données pour les insérer dans une base de donnée dite "archive"

    def modifier_service(self, service, nom, zone):
        # int id_sejour /str nom et zone géographique
        # methode pour modifier un service
        instructionBDD = f"UPDATE patient set nom = '{nom}', zone = '{zone}' where idService = {service};"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()

    def ajouter_personnel(self, nom, prenom, date):
        # int id_personnel /str nom et prenom/date datenaissance
        # methode pour ajouter un personnel soignant
        instructionBDD = f"INSERT INTO PersonnelSoignant (nom, prenom, dateNaissance) " \
                         f"VALUES ('{nom}', '{prenom}', {date};)"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()

    def supprimer_personnel(self, personnel):
        # methode pour supprimer un personnel de la bdd en prenant en compte son id
        instructionBDD = f"DELETE * FROM PersonnelSoignant Where idPersonnel = {personnel}"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()
        #si on veut aller plus loin, on peut garder les données pour les insérer dans une base de donnée dite "archive"

    def modifier_personnel(self, personnel, nom, prenom, date):
        # int id_personnel /str nom et prenom/date datenaissance
        # methode pour modifier un personnel soignant
        instructionBDD = f"UPDATE PersonnelSoignant set nom = '{nom}', prenom = '{prenom}' date = '{date}' where idPersonnel = {personnel};"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()

    def ajouter_sejour(self, patient, service, dateEntree, dateSortie, probleme, numeroDeLit):
        # methode pour ajouter un séjour associé à un patient
        instructionBDD = f"INSERT INTO Sejour (dateEntreeSejour, DateSortieSejour, Probleme, idPatient, NumLit) " \
                         f"VALUES ('{dateEntree}', '{dateSortie}', {probleme}, {patient}, {numeroDeLit};)"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()

        instructionBDD = f"INSERT INTO Dans (DateEntreeChambre) " \
                         f"VALUES ({dateEntree};)"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()
        instructionBDD = f"INSERT INTO AuSein (DateEntreeService, idService) " \
                         f"VALUES ({dateEntree}, {service};)"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()
