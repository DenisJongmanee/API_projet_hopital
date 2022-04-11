import mysql.connector


class Manage_lit:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost",user="root",password="", database="gestion_Patients")
        # connexion à la base de donnée
        self.curseurBDD = self.conn.cursor()

    def afficher_liste_lit(self):
        # methode pour afficher toutes les chambres
        instructionBDD = "SELECT * FROM Lit"
        self.curseurBDD.execute(instructionBDD)

        lits = self.curseurBDD.fetchall()
        
        retour = []
        print(lits)
        for lit in lits:
            retour.append({"id":lit[0], "num_lit":lit[1]})
        return retour;