import graphene
from graphql_auth.schema import UserQuery, MeQuery
from graphene_django import DjangoObjectType
from graphql_auth import mutations
from graphql_jwt.shortcuts import get_token
import graphql_jwt
from .models import Patient,Docteur,Analyste,Pharmacien,Radiologue
#from aboutPatient.models import Dossier,Prescription,Chambre,Consultation

class PatientsType(DjangoObjectType):
    class Meta:
        model = Patient
        fields = ("id","email", "username","password","adresse","telephone","dateDeNaissance","dossier_patient")

class PatientMutation(graphene.Mutation):
    patient = graphene.Field(PatientsType)
    token = graphene.String()
    class Arguments:
        
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        #first_name = graphene.String()
        #last_name = graphene.String()
        adresse = graphene.String()
        telephone = graphene.String()
       


    def mutate(self, info, username, password, email,adresse,telephone):
        patient = Patient.objects.create(email=email,username = username)
       
        #patient.first_name = first_name
        #patient.last_name = last_name
        patient.adresse = adresse
        patient.telephone = telephone 
        patient.set_password(password)
        
        patient.save()
        token = get_token(patient)
        return PatientMutation(patient=patient, token=token)

class UpdatePatient(graphene.Mutation):
    class Arguments:
        
        username = graphene.String()
        password = graphene.String()
        email = graphene.String(required=True)
        #first_name = graphene.String()
        #last_name = graphene.String()
        adresse = graphene.String()
        telephone = graphene.String()

    patient = graphene.Field(PatientsType)
    def mutate(self, info,email,username=None,password =None,first_name =None,last_name=None,adresse=None,telephone=None):
        patient = Patient.objects.get(email=email)
        patient.username = username if username is not None else patient.username
        #patient.first_name = first_name if first_name is not None else patient.first_name
        #patient.last_name = last_name if last_name is not None else patient.last_name
        patient.adresse = adresse if adresse is not None else patient.adresse
        patient.telephone = telephone if telephone is not None else patient.telephone
        if password is not None:
            patient.set_password(password)
        else:
            patient.set_password(patient.password)
        patient.save()

        return UpdatePatient(patient=patient)




class DeletePatient(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
    patient = graphene.Field(PatientsType)
    def mutate(self, info,  email):
        patient = Patient.objects.get(email=email)
        patient.delete()
        return

#-----------------------------------------------------------------------------------------------------------------------------------

class DocteursType(DjangoObjectType):
    class Meta:
        model = Docteur
        fields = ("id","email", "username","password","adresse","telephone","dateDeNaissance","specialite")

class DocteurMutation(graphene.Mutation):
    docteur = graphene.Field(DocteursType)
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        #first_name = graphene.String()
        #last_name = graphene.String()
        adresse = graphene.String()
        telephone = graphene.String()
        specialite = graphene.String()

    def mutate(self, info, username, password, email,adresse,telephone,specialite):
        docteur = Docteur.objects.create(email=email,username = username)
        docteur.specialite = specialite
        #docteur.first_name = first_name
        #docteur.last_name = last_name
        docteur.adresse = adresse
        docteur.telephone = telephone 
        docteur.set_password(password)
        docteur.save()

        return DocteurMutation(docteur=docteur)


    
#-----------------------------------------------------------------------------------------------------------------------------------
class AnalystesType(DjangoObjectType):
    class Meta:
        model = Analyste
        fields = ("id","email", "username","password","adresse","telephone","dateDeNaissance")

class AnalysteMutation(graphene.Mutation):
    analyste = graphene.Field(AnalystesType)
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
       # first_name = graphene.String()
        #last_name = graphene.String()
        adresse = graphene.String()
        telephone = graphene.String()
        

    def mutate(self, info, username, password, email,adresse,telephone):
        analyste = Analyste.objects.create(email=email,username = username)
        
        #analyste.first_name = first_name
        #analyste.last_name = last_name
        analyste.adresse = adresse
        analyste.telephone = telephone 
        analyste.set_password(password)
        analyste.save()

        return AnalysteMutation(analyste=analyste)


#-----------------------------------------------------------------------------------------------------------------------------------
class PharmaciensType(DjangoObjectType):
    class Meta:
        model = Pharmacien
        fields = ("id","email", "username","password","adresse","telephone","dateDeNaissance")

class PharmacienMutation(graphene.Mutation):
    pharmacien = graphene.Field(PharmaciensType)
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        #first_name = graphene.String()
        #last_name = graphene.String()
        adresse = graphene.String()
        telephone = graphene.String()
        

    def mutate(self, info, username, password, email,adresse,telephone):
        pharmacien = Pharmacien.objects.create(email=email,username = username)
        
        #pharmacien.first_name = first_name
        #pharmacien.last_name = last_name
        pharmacien.adresse = adresse
        pharmacien.telephone = telephone 
        pharmacien.set_password(password)
        pharmacien.save()

        return PharmacienMutation(pharmacien=pharmacien)


#-----------------------------------------------------------------------------------------------------------------------------------
class RadiologuesType(DjangoObjectType):
    class Meta:
        model = Radiologue
        fields = ("id","email", "username","password","adresse","telephone","dateDeNaissance")

class RadiologueMutation(graphene.Mutation):
    radiologue = graphene.Field(RadiologuesType)
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        #first_name = graphene.String()
        #last_name = graphene.String()
        adresse = graphene.String()
        telephone = graphene.String()
        

    def mutate(self, info, username, password, email,adresse,telephone):
        radiologue = Radiologue.objects.create(email=email,username = username)
        
        #radiologue.first_name = first_name
        #radiologue.last_name = last_name
        radiologue.adresse = adresse
        radiologue.telephone = telephone 
        radiologue.set_password(password)
        radiologue.save()

        return RadiologueMutation(radiologue=radiologue)


#-----------------------------------------------------------------------------------------------------------------------------------
class Mutation(graphene.ObjectType):
    add_patient = PatientMutation.Field()
    update_patient = UpdatePatient.Field()
    delete_patient = DeletePatient.Field()
    add_docteur = DocteurMutation.Field()
    add_analyste = AnalysteMutation.Field()
    add_pharmacien = PharmacienMutation.Field()
    add_radiologue = RadiologueMutation.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    

class Query(graphene.ObjectType):
    all_patients = graphene.List(PatientsType)
    patient_by_email = graphene.Field(PatientsType,email = graphene.String())
    all_docteurs = graphene.List(DocteursType)
    docteur_by_email = graphene.Field(DocteursType,email = graphene.String())
    all_analystes = graphene.List(AnalystesType)
    analyste_by_email = graphene.Field(AnalystesType,email = graphene.String())
    all_pharmaciens = graphene.List(PharmaciensType)
    pharmacien_by_email = graphene.Field(PharmaciensType,email = graphene.String())
    all_radiologues = graphene.List(RadiologuesType)
    radiologue_by_email = graphene.Field(RadiologuesType,email = graphene.String())
    
    def resolve_all_patients(root, info):
        
        return Patient.objects.all()

    def resolve_patient_by_email (root, info, email):
        try:
            return Patient.objects.get(email = email)
        except:
            return None
    def resolve_all_docteurs(root, info):
        return Docteur.objects.all()
    def resolve_docteur_by_email (root, info, email):
        try:
            return Docteur.objects.get(email = email)
        except:
            return None
    def resolve_all_analystes(root, info):
        return Analyste.objects.all()
    def resolve_analyste_by_email (root, info, email):
        try:
            return Analyste.objects.get(email = email)
        except:
            return None
    def resolve_all_pharmaciens(root, info):
        return Pharmacien.objects.all()
    
    def resolve_pharmacien_by_email (root, info, email):
        try:
            return Pharmacien.objects.get(email = email)
        except:
            return None
    def resolve_all_radiologues(root, info):
        return Radiologue.objects.all()

    def resolve_radiologue_by_email (root, info, email):
        try:
            return Radiologue.objects.get(email = email)
        except:
            return None

schema = graphene.Schema(query=Query, mutation=Mutation)
