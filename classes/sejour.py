class Sejour:
    def __init__(self, patient, service, dateEntree, dateSortie, probleme, idLit, idChambre):
        self.patient = patient
        self.service = service
        self.dateEntree = dateEntree
        self.dateSortie = dateSortie
        self.probleme = probleme
        self.idLit = idLit
        self.idChambre = idChambre
#str probleme/date date entree et sortie / int patient, servicen idLit et id Chambre