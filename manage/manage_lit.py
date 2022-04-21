import mysql.connector


class Manage_lit:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost",user="root",password="", database="gestion_Patients")
        # connexion à la base de donnée
        self.curseurBDD = self.conn.cursor()

    def afficher_liste_lit(self):
        # methode pour afficher toutes les chambres
        instructionBDD = "SELECT numero_lit, id_sejour, numero_chambre FROM chambre INNER JOIN sejour_chambre ON chambre.id_chambre=sejour_chambre.num_chambre INNER JOIN sejour ON sejour_chambre.num_sejour=sejour.id_sejour RIGHT JOIN lit ON sejour.num_lit=lit.id_lit"
        self.curseurBDD.execute(instructionBDD)
        lits = self.curseurBDD.fetchall()
        retour = []
        print(lits)
        for lit in lits:
            retour.append({"id":lit[0], "num_lit":lit[1]})
            if lit[2] == None :
                retour.append({"disponible":"oui"})
            else :
                retour.append({"disponible": "non"})

        return retour