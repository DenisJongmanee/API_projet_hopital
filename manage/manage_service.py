import mysql.connector
from classes.service import Service

class Manage_service:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost",user="root",password="", database="gestion_Patients")
        # connexion à la base de donnée
        self.curseurBDD = self.conn.cursor()

    def ajouter_service(self, service):
        # int id_sejour /str nom et zone géographique
        # methode pour ajouter un service

        instructionBDD = f"INSERT INTO Service (nom_service, zone_geographique) " \
                         f"VALUES ('{service.nom}', '{service.zone}';)"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()

    def supprimer_service(self, service):
        # methode pour supprimer un service de la bdd en prenant en compte son id
        instructionBDD = f"DELETE * FROM service Where id = {service}"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()
        #si on veut aller plus loin, on peut garder les données pour les insérer dans une base de donnée dite "archive"

    def modifier_service(self, service, nom, zone):
        # int id_sejour /str nom et zone géographique
        # methode pour modifier un service
        instructionBDD = f"UPDATE service set nom = '{nom}', zone = '{zone}' where id = {service};"
        self.curseurBDD.execute(instructionBDD)
        self.conn.commit()

    def afficher_liste_service(self):
        # methode pour afficher tous les service
        instructionBDD = "SELECT id, nom_service, zone_geographique FROM Service"
        self.curseurBDD.execute(instructionBDD)
        resultat = self.curseurBDD.fetchall()
        print(resultat)
        retour = []
        for service in resultat:
            retour.append({"id_service":service[0], "nom_service": service[1], "zone_geographique": service[2]})
        return retour