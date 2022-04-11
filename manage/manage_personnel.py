import mysql.connector
from classes.personnel import Personnel

class Manage_personnel:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost",user="root",password="", database="gestion_Patients")
        # connexion à la base de donnée
        self.curseurBDD = self.conn.cursor()

    def afficher_liste_personnel(self):
        # methode pour afficher tous les personnels
        instructionBDD = "SELECT personnel_soigant.id, nom, prenom, date_naissance, nom_service, adresse_mail FROM personnel_soigant INNER JOIN service ON personnel_soigant.id_service=service.id"
        self.curseurBDD.execute(instructionBDD)
        resultat = self.curseurBDD.fetchall()
        retour = []
        for personnel_soignant in resultat:
            retour.append({"id":personnel_soignant[0], "nom":personnel_soignant[1], "prenom":personnel_soignant[2], "date_naissance":personnel_soignant[3], "service":personnel_soignant[4], "mail":personnel_soignant[5]})
        return retour
    
    
    def ajouter_personnel(self, personnel):
        # methode pour ajouter un personnel soignant
        instructionBDD = f"INSERT INTO personnel_soigant (nom, prenom, date_naissance, id_service, adresse_mail, mot_de_passe) " \
                         f"VALUES ('{personnel.nom}', '{personnel.prenom}', '{personnel.date}', {personnel.service}, '{personnel.email}', '{personnel.password}')"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()

    # def supprimer_personnel(self, personnel):
    #     # methode pour supprimer un personnel de la bdd en prenant en compte son id
    #     instructionBDD = f"DELETE * FROM PersonnelSoignant Where idPersonnel = {personnel}"
    #     self.curseurBDD.execute(instructionBDD)
    #     self.conn.commit()
    #     #si on veut aller plus loin, on peut garder les données pour les insérer dans une base de donnée dite "archive"

    def modifier_personnel(self, personnel, id_personnel):
        # int id_personnel
        # methode pour modifier un personnel soignant
        instructionBDD = f"UPDATE PersonnelSoignant set nom = '{personnel.nom}', prenom = '{personnel.prenom}', date = '{personnel.date}', id_service = {personnel.service} where id = {id_personnel};"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()
        
    def get_user(self, email):
        instructionBDD = f"SELECT adresse_mail, mot_de_passe FROM personnel_soigant WHERE adresse_mail= '{email}'"
        self.curseurBDD.execute(instructionBDD)
        resultat = self.curseurBDD.fetchall()
        if len(resultat) == 0:
            return {}
        else:
            return {'email': resultat[0][0], 'password': resultat[0][1]}