import graphene

from graphene_django import DjangoObjectType, DjangoListField 
from .models import  Dossier,Prescription,Chambre,Consultation,Radio,Analyse
from users.models import Patient,Docteur

class DossierType(DjangoObjectType): 
    class Meta:
        model = Dossier
        fields = "__all__"

class CreateDossier(graphene.Mutation):
    dossier = graphene.Field(DossierType)
    class Arguments:
        patient = graphene.String()
        

    def mutate(root, info, patient=None):
        dossier = Dossier.objects.create()
        dossier.patient=Patient.objects.get(email=patient)
        
        dossier.save()
        return CreateDossier(dossier=dossier)


class DeleteDossier(graphene.Mutation):
    
    class Arguments:
        id = graphene.ID()

    dossier = graphene.Field(DossierType)

    
    def mutate(root, info, id):
        dossier = Dossier.objects.get(pk=id)
        dossier.delete()

        return None 
#-------------------------------------------------------------------------------------------------------------------------#
class PrescriptionType(DjangoObjectType): 
    class Meta:
        model = Prescription
        fields = "__all__"

    

class CreatePrescription(graphene.Mutation):
    prescription = graphene.Field(PrescriptionType)
    class Arguments:
        
        patient = graphene.String()
        docteur = graphene.String()
        medicament = graphene.String()
        
        

    def mutate(root, info,docteur,patient, medicament ):
        prescription= Prescription.objects.create()
        prescription.docteur=Docteur.objects.get(email=docteur)
        prescription.patient=Patient.objects.get(email=patient)
        prescription.medicament=medicament
        
        
        prescription.save()
        return CreatePrescription(prescription=prescription)


class DeletePrescription(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    prescription = graphene.Field(PrescriptionType)

    
    def mutate(root, info, id):
        prescription = Prescription.objects.get(pk=id)
        prescription.delete()

        return None 
#--------------------------------------------------------------------------------------------------------------------------
class ChambreType(DjangoObjectType): 
    class Meta:
        model = Chambre
        fields = "__all__"


class CreateChambre(graphene.Mutation):
    class Arguments:
        patient = graphene.String()
        docteur = graphene.String()
        dateDeSejour = graphene.Date()
        dateDeFinSejour = graphene.Date()
        

    chambre = graphene.Field(ChambreType)

    @staticmethod
    def mutate(root, info,patient,docteur,dateDeSejour,dateDeFinSejour ):
        chambre = Chambre.objects.create() 
        chambre.patient=Patient.objects.get(email=patient)
        chambre.docteur=Docteur.objects.get(email=docteur)
        chambre.dateDeSejour=dateDeSejour
        chambre.dateDeFinSejour=dateDeFinSejour
        
        chambre.save()
        return CreateChambre(chambre=chambre)

class DeleteChambre(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    chambre = graphene.Field(ChambreType)

    
    def mutate(root, info, id):
        chambre = Chambre.objects.get(pk=id)
        chambre.delete()

        return None
 
#-----------------------------------------------------------------------------------------------------------------
class ConsultationType(DjangoObjectType): 
    class Meta:
        model = Consultation
        fields = "__all__"


class CreateConsultation(graphene.Mutation):
    class Arguments:
        
        prescription = graphene.ID()
        dossier = graphene.ID()
        docteur = graphene.String()
        chambre = graphene.ID()
        comptRendu = graphene.String() 

    consultation = graphene.Field(ConsultationType)

    def mutate(root, info,prescription,dossier,docteur,chambre,comptRendu ):
        consultation = Consultation.objects.create()

        consultation.prescription=Prescription.objects.get(pk=prescription)
        consultation.dossier=Dossier.objects.get(pk=dossier)
        consultation.docteur=Docteur.objects.get(email=docteur)
        consultation.chambre=Chambre.objects.get(pk=chambre)
        consultation.comptRendu=comptRendu
        
        consultation.save()
        return CreateConsultation(consultation=consultation)

class DeleteConsultation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    consultation = graphene.Field(ConsultationType)

    @staticmethod
    def mutate(root, info, id):
        consultation = Consultation.objects.get(pk=id)
        consultation.delete()

        return None 

#-----------------------------------------------------------------------------------------------------------------
class RadioType(DjangoObjectType): 
    class Meta:
        model = Radio
        fields = "__all__"


class CreateRadio(graphene.Mutation):
    class Arguments:
        
        patient = graphene.String()
        
        docteur = graphene.String()
        description = graphene.String() 
        resultat  = graphene.String() 
        validation  = graphene.Boolean() 

    radio = graphene.Field(RadioType)

    def mutate(root, info,patient,docteur,description,resultat,validation ):
        radio = Radio.objects.create()

        radio.patient=Patient.objects.get(email=patient)
      
        radio.docteur=Docteur.objects.get(email=docteur)
        
        radio.description=description
        radio.resultat=resultat
        radio.validation = validation
        
        radio.save()
        return CreateRadio(radio=radio)

class DeleteRadio(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    radio = graphene.Field(RadioType)

    @staticmethod
    def mutate(root, info, id):
        radio = Radio.objects.get(pk=id)
        radio.delete()

        return None 

#-----------------------------------------------------------------------------------------------------------------
class AnalyseType(DjangoObjectType): 
    class Meta:
        model = Analyse
        fields = "__all__"


class CreateAnalyse(graphene.Mutation):
    class Arguments:
        
        patient = graphene.String()
      
        docteur = graphene.String()
        description = graphene.String() 
        resultat  = graphene.String() 
        validation  = graphene.Boolean() 

    analyse = graphene.Field(AnalyseType)

    def mutate(root, info,patient,docteur,description,resultat,validation ):
        analyse = Analyse.objects.create()

        analyse.patient=Patient.objects.get(email=patient)
    
        analyse.docteur=Docteur.objects.get(email=docteur)
        
        analyse.description=description
        analyse.resultat=resultat
        analyse.validation = validation
        
        analyse.save()
        return CreateAnalyse(analyse=analyse)

class DeleteAnalyse(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    analyse = graphene.Field(AnalyseType)

    @staticmethod
    def mutate(root, info, id):
        analyse = Analyse.objects.get(pk=id)
        analyse.delete()

        return None 



class Mutation(graphene.ObjectType):
    create_dossier = CreateDossier.Field()
    delete_dossier = DeleteDossier.Field()
    create_prescription = CreatePrescription.Field()
    delete_prescription = DeletePrescription.Field()
    create_chambre = CreateChambre.Field()
    delete_chambre = DeleteChambre.Field()
    create_consultation = CreateConsultation.Field()
    delete_consultation = DeleteConsultation.Field()
    create_radio = CreateRadio.Field()
    delete_radio = DeleteRadio.Field()
    create_analyse = CreateAnalyse.Field()
    delete_analyse = DeleteAnalyse.Field()
    """
    update_prescription = UpdatePrescription.Field()
    update_chambre = UpdateChambre.Field()
    update_consultation = UpdateConsultation.Field()
    delete_consultation = DeleteConsultation.Field()
 """

class Query(graphene.ObjectType):
    
    all_dossiers = graphene.List(DossierType)
    dossier = graphene.Field(DossierType, id=graphene.Int())

    def resolve_all_dossiers(self, info, **kwargs):
        return Dossier.objects.all()

    def resolve_dossier(self, info, id):
        return Dossier.objects.get(pk=id)

    all_prescriptions = graphene.List(PrescriptionType)
    prescription = graphene.Field(PrescriptionType, id=graphene.Int())

    def resolve_all_prescriptions(self, info, **kwargs):
        return Prescription.objects.all()

    def resolve_prescription(self, info, id):
        return Prescription.objects.get(pk=id)


    all_chambres = graphene.List(ChambreType)
    chambre = graphene.Field(ChambreType, id=graphene.Int())

    def resolve_all_chambres(self, info, **kwargs):
        return Chambre.objects.all()

    def resolve_chambre(self, info, id):
        return Chambre.objects.get(pk=id)

    all_consultations = graphene.List(ConsultationType)
    consultation = graphene.Field(ConsultationType, id=graphene.Int())

    def resolve_all_consultations(self, info, **kwargs):
        return Consultation.objects.all()

    def resolve_consultation(self, info, id):
        return Consultation.objects.get(pk=id)


schema = graphene.Schema(query=Query, mutation=Mutation)














"""
class UpdatePrescription(graphene.Mutation):
    class Arguments:
        prescription_data = PrescriptionInput(required=True)

    prescription = graphene.Field(PrescriptionType)

    @staticmethod
    def mutate(root, info, prescription_data=None):

        prescription_instance = Prescription.objects.get(pk=prescription_data.id)

        if prescription_instance:
            prescription_instance.idDocteur = prescription_data.idDocteur
            prescription_instance.idPatient = prescription_data.idPatient
            prescription_instance.medicament = prescription_data.medicament
            prescription_instance.dateDeCreation = prescription_data.dateDeCreation
            prescription_instance.save()

            return UpdatePrescription(prescription=prescription_instance)
        return UpdatePrescription(prescription=None)


        
class UpdateChambre(graphene.Mutation):
    class Arguments:
        chambre_data = ChambreInput(required=True)

    chambre = graphene.Field(ChambreType)

    @staticmethod
    def mutate(root, info, chambre_data=None):

        chambre_instance = Chambre.objects.get(pk=chambre_data.id)

        if chambre_instance:
            chambre_instance.idPatient= chambre_data.idPatient
            chambre_instance.idDocteur = chambre_data.idDocteur
            chambre_instance.dateDeSejour = chambre_data.dateDeSejour
            chambre_instance.dateDeFinSejour = chambre_data.dateDeFinSejour
            chambre_instance.save()

            return UpdateChambre(chambre=chambre_instance)
        return UpdateChambre(chambre=None)

class UpdateConsultation(graphene.Mutation):
    class Arguments:
        consultation_data = ConsultationInput(required=True)

    consultation = graphene.Field(ConsultationType)

    @staticmethod
    def mutate(root, info, consultation_data=None):

        consultation_instance = Consultation.objects.get(pk=consultation_data.id)

        if consultation_instance:
            consultation_instance.idPrescription= consultation_data.idPrescription
            consultation_instance.idDossier = consultation_data.idDossier
            consultation_instance.idDocteur = consultation_data.idDocteur
            consultation_instance.idChambre = consultation_data.idChambre
            consultation_instance.comptRendu = consultation_data.comptRendu
            consultation_instance.save()

            return UpdateConsultation(consultation=consultation_instance)
        return UpdateConsultation(consultation=None)
"""