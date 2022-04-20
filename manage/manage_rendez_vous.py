import mysql.connector
from classes.rendez_vous import Rendez_vous

class Manage_rendez_vous:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost",user="root",password="", database="gestion_Patients")
        # connexion à la base de donnée
        self.curseurBDD = self.conn.cursor()

    def ajouter_rendez_vous(self, rendez_vous: Rendez_vous):
        # int id_sejour /str nom et zone géographique
        # methode pour ajouter un service
        print('test fonction')
        instructionBDD = f"INSERT INTO patient (nom, prenom, date_naissance, num_secu) " \
                         f"VALUES ('{rendez_vous.nom}','{rendez_vous.prenom}', '{rendez_vous.date_naissance}', '{rendez_vous.num_secu}');"
        self.curseurBDD.execute(instructionBDD)
        print('test1')
        self.conn.commit()
        id_patient = self.curseurBDD.lastrowid
        instructionBDD = f"INSERT INTO rendezvous (num_vaccin, num_patient, date_rendez_vous, quantieme_dose) " \
                         f"VALUES ('{rendez_vous.nom_vaccin}','{id_patient}', '{rendez_vous.date_vaccination}', '{rendez_vous.dose}');"
        self.curseurBDD.execute(instructionBDD)
        print('test2')
        self.conn.commit()
        instructionBDD = f"UPDATE vaccin set quantitee_disponible = quantitee_disponible - 1 where id_vaccin = '{rendez_vous.nom_vaccin}'"
        print(instructionBDD)
        self.curseurBDD.execute(instructionBDD)
        print('test3')
        self.conn.commit()         

    def supprimer_rendez_vous(self, rendez_vous):
        # methode pour supprimer un service de la bdd en prenant en compte son id
        instructionBDD = f"DELETE * FROM rendez_vous Where id = {rendez_vous}"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()
        #si on veut aller plus loin, on peut garder les données pour les insérer dans une base de donnée dite "archive"

    #def modifier_rendez_vous(self, nom, prenom, date_naissance, num_secu, date_vaccination, nom_vaccin, dose):
        # int id_sejour /str nom et zone géographique
        # methode pour modifier un service
        #instructionBDD = f"UPDATE rendez_vous set nom = '{nom}', nom_vaccin = '{nom_vaccin}', description = '{description}', nombre_dose_max = '{nombre_dose_max}', quantitee_disponible = '{quantitee_disponible}' where id = {vaccin};"
        #self.curseurBDD.execute(instructionBDD)
        #self.conn.commit()

    def afficher_liste_rendez_vous(self):
        # methode pour afficher tous les service
        print('test')
        instructionBDD = "SELECT patient.nom, patient.prenom, patient.date_naissance, patient.num_secu, rendezvous.date_rendez_vous, vaccin.nom_vaccin, rendezvous.quantieme_dose FROM rendezvous Inner join Patient on num_patient = id_patient Inner join vaccin on num_vaccin = id_vaccin"
        self.curseurBDD.execute(instructionBDD)
        resultat = self.curseurBDD.fetchall()
        print(resultat)
        retour = []
        for element in resultat:
            retour.append({"nom":element[0], "prenom": element[1], "date_naissance": element[2], "num_secu": element[3], "date_rendez_vous": element[4], "nom_vaccin": element[5], "quantieme_dose": element[6]})
            print(retour)
        return retour