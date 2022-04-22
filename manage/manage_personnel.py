import mysql.connector
from classes.personnel import Personnel

class Manage_personnel:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost",user="root",password="", database="gestion_Patients")
        # connexion à la base de donnée
        self.curseurBDD = self.conn.cursor()

    def afficher_liste_personnel(self):
        # methode pour afficher tous les personnels
        instructionBDD = "SELECT personnelsoignant.id_personnel, nom, prenom, date_naissance, nom_service, adresse_mail FROM personnelsoignant INNER JOIN service ON personnelsoignant.num_service=service.id_service"
        self.curseurBDD.execute(instructionBDD)
        resultat = self.curseurBDD.fetchall()
        retour = []
        for personnel_soignant in resultat:
            retour.append({"id":personnel_soignant[0], "nom":personnel_soignant[1], "prenom":personnel_soignant[2], "date_naissance":personnel_soignant[3], "service":personnel_soignant[4], "mail":personnel_soignant[5]})
        return retour
    
    
    def ajouter_personnel(self, personnel):
        # methode pour ajouter un personnel soignant
        instructionBDD = f"INSERT INTO personnelsoignant (nom, prenom, date_naissance, num_service, adresse_mail, mot_de_passe) " \
                         f"VALUES ('{personnel.nom}', '{personnel.prenom}', '{personnel.date}', {personnel.service}, '{personnel.email}', '{personnel.password}')"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()

    # def supprimer_personnel(self, personnel):
    #     # methode pour supprimer un personnel de la bdd en prenant en compte son id
    #     instructionBDD = f"DELETE FROM PersonnelSoignant Where idPersonnel = {personnel}"
    #     self.curseurBDD.execute(instructionBDD)
    #     self.conn.commit()
    #     #si on veut aller plus loin, on peut garder les données pour les insérer dans une base de donnée dite "archive"

    def modifier_personnel(self, personnel, id_personnel):
        # int id_personnel
        # methode pour modifier un personnel soignant
        instructionBDD = f"UPDATE PersonnelSoignant set nom = '{personnel.nom}', prenom = '{personnel.prenom}', date_naissancce = '{personnel.date}', num_service = {personnel.service} where id_personnel = {id_personnel};"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()
        
    def get_user(self, email):
        instructionBDD = f"SELECT adresse_mail, mot_de_passe, nom_role FROM personnelsoignant INNER JOIN role ON personnelsoignant.num_role=role.id_role WHERE adresse_mail= '{email}'"
        self.curseurBDD.execute(instructionBDD)
        resultat = self.curseurBDD.fetchall()
        if len(resultat) == 0:
            return {}
        else:
            return {'email': resultat[0][0], 'password': resultat[0][1], 'roles':[resultat[0][2]]}



    def afficher_liste_compte_cs(self):
        # methode pour afficher tous les comptes
        instructionBDD = "SELECT personnelsoignant.id_personnel, nom, prenom, date_naissance, adresse_mail, num_role, num_service, nom_role, nom_service FROM personnelsoignant INNER JOIN Role on num_role = id_role INNER JOIN Service on num_service = id_service"
        self.curseurBDD.execute(instructionBDD)
        resultat = self.curseurBDD.fetchall()
        personnels_soignants = []
        for personnel_soignant in resultat:
            personnels_soignants.append({"IdCompte":personnel_soignant[0], "Nom":personnel_soignant[1], "Prenom":personnel_soignant[2], "DateNaissance":personnel_soignant[3], "AdresseMail":personnel_soignant[4], "Role":personnel_soignant[5], "Service":personnel_soignant[6], "NomRole":personnel_soignant[7], "NomService":personnel_soignant[8]})
        retour = {"ListComptes": personnels_soignants}
        return retour

    def ajouter_compte_cs(self, personnel):
        # methode pour ajouter un personnel compte
        instructionBDD = f"INSERT INTO personnelsoignant (nom, prenom, date_naissance, adresse_mail, num_role, num_service, mot_de_passe) " \
                         f"VALUES ('{personnel.nom}', '{personnel.prenom}', '{personnel.date}', '{personnel.email}', {personnel.role}, {personnel.service}, '{personnel.password}')"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()
        id = self.curseurBDD.lastrowid
        return id


    def supprimer_compte_cs(self, personnel):
        # methode pour supprimer un personnel de la bdd en prenant en compte son id
        instructionBDD = f"DELETE FROM personnelsoignant Where id_personnel = {personnel}"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()

    def modifier_compte_cs(self, personnel, id_personnel):
        # int id_personnel
        # methode pour modifier un personnel soignant
        instructionBDD = f"UPDATE PersonnelSoignant set nom = '{personnel.nom}', prenom = '{personnel.prenom}', date_naissance = '{personnel.date}', adresse_mail = '{personnel.email}', num_role = '{personnel.role}', num_service = '{personnel.service}' where id_personnel = {id_personnel};"
        print(instructionBDD)
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()
