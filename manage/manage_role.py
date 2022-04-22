import mysql.connector

class Manage_role:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost",user="root",password="", database="gestion_Patients")
        # connexion à la base de donnée
        self.curseurBDD = self.conn.cursor()

    def afficher_liste_role_cs(self):
        # methode pour afficher tous les service

        instructionBDD = "SELECT id_role, nom_role FROM Role"
        self.curseurBDD.execute(instructionBDD)
        resultat = self.curseurBDD.fetchall()
        print(resultat)
        roles = []
        for role in resultat:
            roles.append({"IdRole":role[0], "NomRole": role[1]})
        retour = {"ListRoles": roles}
        return retour