import mysql.connector
from classes.vaccin import Vaccin

class Manage_vaccin:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost",user="root",password="", database="gestion_Patients")
        # connexion à la base de donnée
        self.curseurBDD = self.conn.cursor()

    def ajouter_vaccin(self, service):
        # int id_sejour /str nom et zone géographique
        # methode pour ajouter un service

        instructionBDD = f"INSERT INTO Vaccin (id_vaccin, nom_vaccin, description, nombre_dose_max, quantitee_disponible) " \
                         f"VALUES ('{vaccin.id_vaccin}','{vaccin.nom_vaccin}', '{vaccin.description}', '{vaccin.nombre_dose_max}', '{vaccin.quantitee_disponible}';)"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()

    def supprimer_vaccin(self, vaccin):
        # methode pour supprimer un service de la bdd en prenant en compte son id
        instructionBDD = f"DELETE * FROM vaccin Where id = {vaccin}"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()
        #si on veut aller plus loin, on peut garder les données pour les insérer dans une base de donnée dite "archive"

    def modifier_vaccin(self, id_vaccin, nom_vaccin, description, nombre_dose_max, quantitee_disponible):
        # int id_sejour /str nom et zone géographique
        # methode pour modifier un service
        instructionBDD = f"UPDATE service set id_vaccin = '{id_vaccin}', nom_vaccin = '{nom_vaccin}', description = '{description}', nombre_dose_max = '{nombre_dose_max}', quantitee_disponible = '{quantitee_disponible}' where id = {vaccin};"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()

    def afficher_liste_vaccin(self):
        # methode pour afficher tous les service
        print('test')
        instructionBDD = "SELECT id_vaccin, nom_vaccin, description, nombre_dose_max, quantitee_disponible FROM vaccin"
        self.curseurBDD.execute(instructionBDD)
        resultat = self.curseurBDD.fetchall()
        print(resultat)
        retour = []
        for vaccin in resultat:
            retour.append({"id_vaccin":vaccin[0], "nom_vaccin": vaccin[1], "description": vaccin[2], "nombre_dose_max": vaccin[3], "quantitee_disponible": vaccin[4]})
            print(retour)
        return retour