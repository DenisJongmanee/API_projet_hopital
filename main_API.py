from flask import Flask, jsonify, request, abort
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

main_API = Flask(__name__)

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
        personnel = Personnel(message["nom"], message["prenom"], message["date"], message["service"], message["email"], message["password"])
        try :
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
    print("test");
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
 
        
        
        
if __name__ == '__main__':
    main_API.run()

