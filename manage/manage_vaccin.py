import mysql.connector
from classes.vaccin import Vaccin

class Manage_vaccin:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost",user="root",password="", database="gestion_Patients")
        # connexion à la base de donnée
        self.curseurBDD = self.conn.cursor()

    def afficher_liste_vaccin(self):
        # methode pour afficher tous les service

        instructionBDD = "SELECT id_vaccin, nom_vaccin, description, nombre_dose_max, quantitee_disponible FROM vaccin"
        self.curseurBDD.execute(instructionBDD)
        resultat = self.curseurBDD.fetchall()
        print(resultat)
        retour = []
        for vaccin in resultat:
            retour.append({"id_vaccin":vaccin[0], "nom_vaccin": vaccin[1], "description": vaccin[2], "nombre_dose_max": vaccin[3], "quantitee_disponible": vaccin[4]})

        return retour

    def afficher_liste_vaccin_cs(self):
        # methode pour afficher tous les service

        instructionBDD = "SELECT nom_vaccin, quantitee_disponible FROM vaccin"
        self.curseurBDD.execute(instructionBDD)
        resultat = self.curseurBDD.fetchall()
        print(resultat)
        vaccins = []
        for vaccin in resultat:
            vaccins.append({"NomVaccin":vaccin[0], "QuantiteeDisponible": vaccin[1]})
        retour = {"ListVaccins": vaccins}
        return retour