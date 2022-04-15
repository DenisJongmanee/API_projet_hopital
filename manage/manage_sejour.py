import mysql.connector
from classes.sejour import Sejour
from datetime import datetime
class Manage_sejour:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost",user="root",password="", database="gestion_Patients")
        # connexion à la base de donnée
        self.curseurBDD = self.conn.cursor()

    def ajouter_sejour(self, sejour : Sejour):
    
        # methode pour ajouter un séjour associé à un patient + lit
        instructionBDD = f"INSERT INTO Sejour (date_entree_sejour, date_sortie_sejour, probleme, num_patient, num_lit) " \
                        f"VALUES ('{sejour.dateEntree}', '{sejour.dateSortie}', '{sejour.probleme}', {sejour.patient}, {sejour.num_lit});"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()

        #id du sejour généré
        idsejour = self.curseurBDD.lastrowid
        
        #chambre
        instructionBDD2 = f"INSERT INTO sejour_chambre (num_sejour, num_chambre, date_entree_chambre) VALUES ({idsejour},{sejour.idChambre},'{sejour.dateEntree}');"
        self.curseurBDD.execute(instructionBDD2)
        self.conn.commit()
        
        #service
        instructionBDD3 = f"INSERT INTO service_sejour (date_entree_service, sejour_id, service_id) VALUES ('{sejour.dateEntree}', {idsejour}, {sejour.service});"
        self.curseurBDD.execute(instructionBDD3)
        self.conn.commit()
        
      

    def afficher_liste_sejour(self):
        # methode pour afficher tous les sejour
        instructionBDD = f"SELECT sejour.id_sejour, nom, prenom, date_entree_sejour, date_sortie_sejour, nom_service, num_chambre, num_lit, probleme FROM ((Patient INNER JOIN Sejour ON patient.id_patient = sejour.num_patient INNER JOIN lit ON sejour.num_lit=lit.id_lit)INNER JOIN sejour_chambre ON sejour.id_sejour=sejour_chambre.num_sejour INNER JOIN chambre ON sejour_chambre.num_chambre=chambre.id_chambre) INNER JOIN service_sejour ON sejour.id_sejour=service_sejour.num_sejour INNER JOIN service ON service_sejour.num_service=service.id_service"
        self.curseurBDD.execute(instructionBDD)
        resultat = self.curseurBDD.fetchall()
        
        print(resultat)
        
        retour = []
        for sejour in resultat:
            retour.append({"id_sejour":sejour[0], "nom": sejour[1], "prenom": sejour[2], "date_entree_sejour": sejour[3], "date_sortie_sejour": sejour[4], "nom_service": sejour[5], "num_chambre":sejour[6], "num_lit":sejour[7], "probleme": sejour[8]})
        return retour
    
    def infoSejour(self, id):
        instructionBDD = f"SELECT sejour.id_sejour, nom, prenom, date_entree_sejour, date_sortie_sejour, service.id_service, chambre.id_chambre, lit.id_lit, probleme FROM ((Patient INNER JOIN Sejour ON patient.id_patient = sejour.num_patient INNER JOIN lit ON sejour.num_lit=lit.id_lit)INNER JOIN sejour_chambre ON sejour.id_sejour=sejour_chambre.num_sejour INNER JOIN chambre ON sejour_chambre.num_chambre=chambre.id_chambre) INNER JOIN service_sejour ON sejour.id_sejour=service_sejour.num_sejour INNER JOIN service ON service_sejour.num_service=service.id_service WHERE sejour.id_sejour={id}"
        self.curseurBDD.execute(instructionBDD)
        sejour = self.curseurBDD.fetchone()
        return {"id_sejour":sejour[0], "nom": sejour[1], "prenom": sejour[2], "date_entree_sejour": sejour[3].strftime("%Y-%m-%d %H:%M:%S"), "date_sortie_sejour": sejour[4].strftime("%Y-%m-%d %H:%M:%S"), "service": sejour[5], "chambre":sejour[6], "lit":sejour[7], "probleme": sejour[8]}

    def modif_sejour(self, sejour, id):
        instructionBDD = f"UPDATE Sejour SET lit={sejour.idLit}, date_entree_sejour='{sejour.dateEntree}', date_sortie_sejour='{sejour.dateSortie}', probleme='{sejour.probleme}' WHERE id_sejour={id}"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()
        
        instructionBDD2 = f"UPDATE sejour_chambre SET num_chambre={sejour.idChambre} WHERE num_sejour={id}"
        self.curseurBDD.execute(instructionBDD2)
        self.conn.commit()
                
        instructionBDD3 = f"UPDATE service_sejour SET num_service={sejour.service} WHERE num_sejour={id}"
        self.curseurBDD.execute(instructionBDD3)
        self.conn.commit()