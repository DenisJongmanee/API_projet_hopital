from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from classes.patient import Patient
from manage.manage_patient import Manage_patient
from classes.personnel import Personnel
from manage.manage_personnel import Manage_personnel
from classes.sejour import Sejour
from manage.manage_sejour import Manage_sejour
from classes.service import Service
from manage.manage_service import Manage_service
from classes.chambre import Chambre
from manage.manage_chambre import Manage_chambre
from manage.manage_lit import Manage_lit
from manage.manage_vaccin import Manage_vaccin
from manage.manage_rendez_vous import Manage_rendez_vous
from classes.rendez_vous import Rendez_vous
from manage.manage_role import Manage_role

main_API = Flask(__name__)
CORS(main_API)

######Routes User


@main_API.route('/api/user/<email>', methods={'GET'})
def consulter(email):
    try:

        BaseDD = Manage_personnel()
        user = BaseDD.get_user(email)
        
        return jsonify(user)
    except:
        abort(500)
        
@main_API.route('/api/user', methods={'POST'})
def inscription():
    message = request.get_json(force=True)
    BaseDD = Manage_personnel()
    if "nom" in message and "prenom" in message and "date" in message and "service" in message and "email" in message and "password" in message :
        personnel = Personnel(message["nom"], message["prenom"], message["date"], message["email"], 1, message["service"], message["password"])
        try :
            print("testest")
            BaseDD.ajouter_personnel(personnel)
            return "Ok"
        except:
            abort(500)
    else:
        abort(406)

######Routes Patient

@main_API.route('/api/patient/<patient>', methods={'GET'})
def getPatient(patient):
     try:
         BaseDD = Manage_patient()
         dictionnaire_patient = BaseDD.afficher_donnees_patient(patient)
        
         return jsonify(dictionnaire_patient)
     except:
         abort(500)


@main_API.route('/api/patient', methods={'GET'})
def listePatient():
    try:
        BaseDD = Manage_patient()
        dictionnaire_patient = BaseDD.afficher_liste_patient()
        return jsonify(dictionnaire_patient)
    except:
        abort(500)
        
        
@main_API.route('/api/patient_sejour', methods={'GET'})
def listePatientSejour():
    try:
        BaseDD = Manage_patient()
        dictionnaire_patient = BaseDD.afficher_liste_patient_sejour()
        return jsonify(dictionnaire_patient)
    except:
        abort(500)
        
        
@main_API.route('/api/patient', methods={'POST'})
def ajoutPatient():
    message = request.get_json(force=True)
    BaseDD = Manage_patient()
    if "nom" in message and "prenom" in message and "date" in message:
        patient = Patient(message["nom"], message["prenom"], message["date"])
        try :
            BaseDD.ajouter_patient(patient)
            return "Ok"
        except:
            abort(500)
    else:
        abort(406)
        
        
@main_API.route('/api/patient', methods={'PUT'})
def modificationPatient() :
    message = request.get_json(force=True)
    BaseDD = Manage_patient()
    if "id" in message and "nom" in message and "prenom" in message and "date" in message:
        patient = Patient(message["nom"], message["prenom"], message["date"])
        try :
            BaseDD.modifier_patient(patient, message['id'])
            return "Ok"
        except:
            abort(500)
    else:
        abort(406)
        
        
# @main_API.route('/api/SuppressionPatient', methods={'DELETE'})
# def suppressionPatient():
#     message = request.get_json(force=True)
#     BaseDD = Manage_patient()
#     if "patient" in message :
#         try:
#             BaseDD.supprimer_patient(message["patient"])
#             return "Ok"
#         except:
#             abort(500)
#     else:
#         abort(406)


######Routes Personnel Soignant

@main_API.route('/api/personnel_soignant', methods={'GET'})
def listePersonnel():
    try:
        BaseDD = Manage_personnel()
        dictionnaire_personnel = BaseDD.afficher_liste_personnel()
        return jsonify(dictionnaire_personnel)
    except:
        abort(500)
        
        
@main_API.route('/api/personnel_soignant', methods={'POST'})
def ajoutPersonnel():
    message = request.get_json(force=True)
    BaseDD = Manage_personnel()
    if "nom" in message and "prenom" in message and "date" in message and "service" in message:
        personnel = Personnel(message["nom"], message["prenom"], message["date"], message["service"])
        try :
            BaseDD.ajouter_personnel(personnel)
            return "Ok"
        except:
            abort(500)
    else:
        abort(406)
        
        
@main_API.route('/api/personnel_soignant', methods={'PUT'})
def modificationPersonnel() :
    message = request.get_json(force=True)
    BaseDD = Manage_personnel()
    if "personnel" in message and "nom" in message and "prenom" in message and "date" in message and "service" in message:
        personnel = Personnel(message["nom"], message["prenom"], message["date"], message["service"])
        try :
            BaseDD.modifier_personnel(personnel, message["personne"])
            return "Ok"
        except:
            abort(500)
    else:
        abort(406)
        
        
#@main_API.route('/api/personnel_soignant', methods={'DELETE'})
# def suppressionPersonnel():
#     message = request.get_json(force=True)
#     BaseDD = Manage_personnel()
#     if "personnel" in message :
#         try:
#             BaseDD.supprimer_personnel(message["personnel"])
#             return "Ok"
#         except:
#             abort(500)
#     else:
#         abort(406)


######Routes Service

@main_API.route('/api/service', methods={'GET'})
def listeService():
    try:
        BaseDD = Manage_service()
        dictionnaire_service = BaseDD.afficher_liste_service()
        return jsonify(dictionnaire_service)
    except:
        abort(500)


# @main_API.route('/api/service', methods={'POST'})
# def ajoutService():
#     message = request.get_json(force=True)
#     BaseDD = Manage_service()
#     if "nom" in message and "zone" in message:
#         service = Service(message["nom"], message["zone"])
#         try :
#             BaseDD.ajouter_service(service)
#             return "Ok"
#         except:
#             abort(500)
#     else:
#         abort(406)
        
        
# @main_API.route('/api/service', methods={'PUT'})
# def modificationService() :
#     message = request.get_json(force=True)
#     BaseDD = Manage_service()
#     if "service" in message and "nom" in message and "zone" in message:
#         service = Service(message["nom"], message["zone"])
#         try :
#             BaseDD.modifier_service(service)
#             return "Ok"
#         except:
#             abort(500)
#     else:
#         abort(406)


#@main_API.route('/api/service', methods={'DELETE'})
# def suppressionService():
#     message = request.get_json(force=True)
#     BaseDD = Manage_service()
#     if "service" in message :
#         try:
#             BaseDD.supprimer_service(message["service"])
#             return "Ok"
#         except:
#             abort(500)
#     else:
#         abort(406)



######Routes Sejour

@main_API.route('/api/sejour', methods={'POST'})
def ajoutSejour():
    message = request.get_json(force=True)
    BaseDD = Manage_sejour()
    #sejour, patient, service, dateEntree, dateSortie, probleme, idLit, idChambre
    if "patient" in message and "service" in message and "dateEntree" in message and "dateSortie" in message and "probleme" in message and "idLit" in message and "idChambre" in message:
        sejour = Sejour(message["patient"], message["service"], message["dateEntree"], message["dateSortie"], message["probleme"], message["idLit"], message["idChambre"])
        try :
            BaseDD.ajouter_sejour(sejour)
            return "Ok"
        except:
            abort(500)
    else:
        abort(406)


@main_API.route('/api/sejour', methods={'GET'})
def listeSejour():
    try:
        BaseDD = Manage_sejour()
        dictionnaire_sejour = BaseDD.afficher_liste_sejour()
        return jsonify(dictionnaire_sejour)
    except:
        abort(500)

@main_API.route('/api/sejour/<sejour>', methods={'GET'})
def getSejour(sejour):
     try:
         BaseDD = Manage_sejour()
         dictionnaire_patient = BaseDD.infoSejour(sejour)
        
         return jsonify(dictionnaire_patient)
     except:
         abort(500)

        
@main_API.route('/api/sejour', methods={'PUT'})
def modificationSejour() :
    message = request.get_json(force=True)
    BaseDD = Manage_sejour()
    if "service" in message and "dateEntree" in message and "dateSortie" in message and "probleme" in message and "idLit" in message and "idChambre" in message and "id" in message:
        sejour = Sejour("", message["service"], message["dateEntree"], message["dateSortie"], message["probleme"], message["idLit"], message["idChambre"])
        try :
            BaseDD.modif_sejour(sejour, message['id'])
            return "Ok"
        except:
            abort(500)
    else:
        abort(406)


######Routes Chambre

@main_API.route('/api/chambre', methods={'GET'})
def listeChambre():
    try:
        BaseDD = Manage_chambre()
        dictionnaire_chambre = BaseDD.afficher_liste_chambre()
        return jsonify(dictionnaire_chambre)
    except:
        abort(500)
        
# ######Routes Lit

@main_API.route('/api/lit', methods={'GET'})
def listeLit():
    try:
        BaseDD = Manage_lit()
        dictionnaire_chambre = BaseDD.afficher_liste_lit()
        return jsonify(dictionnaire_chambre)
    except:
        abort(500)



@main_API.route('/api/vaccin', methods={'GET'})
def listeVaccin():
    try:
        BaseDD = Manage_vaccin()
        dictionnaire_vaccin = BaseDD.afficher_liste_vaccin()
        return jsonify(dictionnaire_vaccin)
    except:
        abort(500)



@main_API.route('/api/rendez_vous', methods={'GET'})
def listeRendez_vous():
    try:
        BaseDD = Manage_rendez_vous()
        dictionnaire_rendez_vous = BaseDD.afficher_liste_rendez_vous()
        return jsonify(dictionnaire_rendez_vous)
    except:
        abort(500) 

@main_API.route('/api/rendez_vous', methods={'POST'})
def ajout_rendez_vous():
    message = request.get_json(force=True)
    BaseDD = Manage_rendez_vous()
    message = message["rendez_vous"]
    if "nom" in message and "prenom" in message and "dateNaissance" in message and "numSecuriteSociale" in message and "dateRes" in message and "nomVaccin" in message and "nbrDoses" in message:
        rendez_vous = Rendez_vous(message["nom"], message["prenom"], message["dateNaissance"], message["numSecuriteSociale"], message["dateRes"], message["nomVaccin"], message["nbrDoses"])
        try :
            BaseDD.ajouter_rendez_vous(rendez_vous)
            return "Ok"
        except:
            abort(500)
    else:
        abort(406)


#partie c#
@main_API.route('/api/cs/service', methods={'GET'})
def listeServiceCS():
    try:
        BaseDD = Manage_service()
        dictionnaire_service = BaseDD.afficher_liste_service_cs()
        return jsonify(dictionnaire_service)
    except:
        abort(500)

@main_API.route('/api/cs/lit', methods={'GET'})
def listeLitCS():
    try:
        BaseDD = Manage_lit()
        dictionnaire_chambre = BaseDD.afficher_liste_lit_cs()
        return jsonify(dictionnaire_chambre)
    except:
        abort(500)

@main_API.route('/api/cs/vaccin', methods={'GET'})
def listeVaccinCS():
    try:
        BaseDD = Manage_vaccin()
        dictionnaire_vaccin = BaseDD.afficher_liste_vaccin_cs()
        return jsonify(dictionnaire_vaccin)
    except:
        abort(500)


@main_API.route('/api/cs/role', methods={'GET'})
def listeRole():
    try:
        BaseDD = Manage_role()
        dictionnaire_role = BaseDD.afficher_liste_role_cs()
        return jsonify(dictionnaire_role)
    except:
        abort(500)

@main_API.route('/api/cs/compte', methods={'GET'})
def listeCompte():
    try:
        BaseDD = Manage_personnel()
        dictionnaire_compte = BaseDD.afficher_liste_compte_cs()
        return jsonify(dictionnaire_compte)
    except:
        abort(500)

@main_API.route('/api/cs/compte', methods={'POST'})
def inscriptionCS():
    message = request.get_json(force=True)
    BaseDD = Manage_personnel()
    if "Nom" in message and "Prenom" in message and "DateNaissance" in message and "AdresseMail" in message and "Role" in message and "Service" in message and "MotDePasse" in message :
        personnel = Personnel(message["Nom"], message["Prenom"], message["DateNaissance"], message["AdresseMail"], message["Role"], message["Service"], message["MotDePasse"])
        try :
            id = BaseDD.ajouter_compte_cs(personnel)
            return jsonify(id)
        except:
            abort(500)
    else:
        abort(406)

@main_API.route('/api/cs/compte/<id>', methods={'DELETE'})
def suppressionCompte(id):
    BaseDD = Manage_personnel()
    try:
        BaseDD.supprimer_compte_cs(id)
        return "Ok"
    except:
        abort(500)
    else:
        abort(406)


@main_API.route('/api/cs/compte', methods={'PUT'})
def modificationCompte():
    message = request.get_json(force=True)
    BaseDD = Manage_personnel()
    print("herherhe")
    print(message)
    if "IdCompte" in message and "Nom" in message and "Prenom" in message and "DateNaissance" in message and "AdresseMail" in message and "Role" in message and "Service" in message and "MotDePasse" in message:
        personnel = Personnel(message["Nom"], message["Prenom"], message["DateNaissance"], message["AdresseMail"], message["Role"], message["Service"], message["MotDePasse"])
        try :
            BaseDD.modifier_compte_cs(personnel, message["IdCompte"])
            return "Ok"
        except:
            abort(500)
    else:
        abort(406)

if __name__ == '__main__':
    main_API.run()

