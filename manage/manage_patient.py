from dis import Instruction
import mysql.connector
from classes.patient import Patient
from datetime import datetime

class Manage_patient:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost",user="root",password="", database="gestion_Patients")
        # connexion à la base de donnée
        self.curseurBDD = self.conn.cursor()

    def afficher_donnees_patient(self, patient):
        # methode pour afficher les données d'un patient en prenant en compte son id
        instructionBDD = f"SELECT * FROM patient WHERE id_patient = {patient}"
        self.curseurBDD.execute(instructionBDD)
        dictionnaire_retour = {}
        patient = self.curseurBDD.fetchone()
        print(patient);
        return {'id':patient[0], 'nom':patient[1], 'prenom': patient[2], 'date':patient[3].strftime("%Y-%m-%d")}
         
    def afficher_liste_patient(self):
        instructionBDD = "SELECT id_patient, nom, prenom from Patient"
        self.curseurBDD.execute(instructionBDD)
        resultat = self.curseurBDD.fetchall()
        retour = []
        for patient in resultat:
            retour.append({"id": patient[0], "nom": patient[1], "prenom": patient[2]})
        return retour

    def afficher_liste_patient_sejour(self):
        # methode pour afficher tous les patients
        instructionBDD = "SELECT patient.id_patient, nom, prenom, date_naissance, sejour.id_sejour, num_chambre, num_lit FROM (Patient INNER JOIN Sejour ON Patient.id_patient=Sejour.num_patient INNER JOIN lit ON Sejour.num_lit=lit.id_lit) INNER JOIN sejour_chambre ON sejour.id_sejour=sejour_chambre.num_sejour INNER JOIN chambre ON sejour_chambre.num_chambre=chambre.id_chambre WHERE sejour.date_sortie_sejour>NOW() "
        self.curseurBDD.execute(instructionBDD)
        resultat = self.curseurBDD.fetchall()
        
        retour = []
        print(resultat)
        for patient in resultat:
            retour.append({"id":patient[0], "nom": patient[1], "prenom": patient[2], "date": patient[3], "id_sejour": patient[4], "num_chambre": patient[5], "num_lit": patient[6]})
        return retour

    def ajouter_patient(self, patient):
        # methode pour ajouter un patient
        instructionBDD = f"INSERT INTO Patient (nom, prenom, date_naissance) VALUES ('{patient.nom}', '{patient.prenom}', '{patient.date}');"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()

    # def supprimer_patient(self, patient):
    #     # methode pour supprimer un patient de la bdd avec en argument l'id du patient
    #     instructionBDD = f"DELETE * FROM patient Where idPatient = {patient}"
    #     self.curseurBDD.execute(instructionBDD)
    #     self.conn.commit()
    #     # si on veut aller plus loin, on peut garder les données pour les insérer dans une base de donnée dite "archive"

    def modifier_patient(self, patient, id_patient):
    # int id_patient
    # methode pour modifier un patient en prenant en compte son id
        instructionBDD = f"UPDATE patient set nom = '{patient.nom}', prenom = '{patient.prenom}', date_naissance = '{patient.date}' where id_patient = {id_patient};"

        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()


