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
        return retour


    def afficher_liste_lit_cs(self):
        # methode pour afficher toutes les chambres
        instructionBDD = "SELECT numero_lit, numero_chambre FROM chambre INNER JOIN sejour_chambre ON chambre.id_chambre=sejour_chambre.num_chambre INNER JOIN sejour ON sejour_chambre.num_sejour=sejour.id_sejour RIGHT JOIN lit ON sejour.num_lit=lit.id_lit WHERE Sejour.date_entree_sejour<now() AND Sejour.date_sortie_sejour>Now();"
        self.curseurBDD.execute(instructionBDD)
        resultat = self.curseurBDD.fetchall()
        
        instructionBDD2 = "SELECT numero_lit FROM Lit"
        self.curseurBDD.execute(instructionBDD2)
        resultat2 = self.curseurBDD.fetchall()
        
        retour = []
        lits = [] 
        for lit in resultat2:
            lit_utilise = False
            for lit_sejour in resultat:
                if lit_sejour[0] == lit[0]:
                    lit_utilise = True
                    numero_chambre = lit_sejour[1]
            if lit_utilise:
                lits.append({"NumeroLit":lit[0], "NumeroChambre":numero_chambre, "Occupation": True})
            else:
                lits.append({"NumeroLit":lit[0], "NumeroChambre":0, "Occupation": False})
        print(lits)
        retour = {"ListLits": lits}
        return retour