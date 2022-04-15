import mysql.connector
from classes.chambre import Chambre

class Manage_chambre:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost",user="root",password="", database="gestion_Patients")
        # connexion à la base de donnée
        self.curseurBDD = self.conn.cursor()

    def afficher_liste_chambre(self):
        # methode pour afficher toutes les chambres
        instructionBDD = "SELECT chambre.id_chambre, num_chambre, nombre_lits, nom_service FROM Chambre INNER JOIN Service ON chambre.num_service=service.id_service "
        self.curseurBDD.execute(instructionBDD)

        resultat = self.curseurBDD.fetchall()
        
        retour = []
        print(resultat)
        for chambre in resultat:
            retour.append({"id":chambre[0], "num_chambre":chambre[1], "nblits": chambre[2] ,"service": chambre[3]})
        return retour;