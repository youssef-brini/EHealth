from django.db import models

class Dossier (models.Model):
    patient = models.OneToOneField("users.Patient",null=True,on_delete=models.CASCADE,related_name="dossier_patient") 

class Prescription (models.Model):
    docteur = models.ForeignKey("users.Docteur",null=True, on_delete=models.CASCADE, related_name='idDocteurPrescription')
    patient = models.ForeignKey("users.Patient",null=True, on_delete=models.CASCADE, related_name='idPatientPrescription')
    medicament = models.TextField()
    dateDeCreation = models.DateField(auto_now_add=True)

class Chambre (models.Model):
    patient = models.ForeignKey("users.Patient", on_delete=models.CASCADE, related_name='idPatientChambre',null=True)
    docteur = models.ForeignKey("users.Docteur", on_delete=models.CASCADE, related_name='idDocteurChambre',null=True)
    dateDeSejour = models.DateField(null=True)
    dateDeFinSejour =models.DateField(null=True)

class Consultation (models.Model):
    prescription = models.OneToOneField(Prescription, on_delete=models.SET_NULL, related_name='prescription',null=True)
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE, related_name='consultation',null=True)
    docteur = models.ForeignKey("users.Docteur", on_delete=models.SET_NULL, related_name='docteur',null=True)
    chambre = models.OneToOneField(Chambre, on_delete=models.SET_NULL,null=True,related_name='chambre')
    
    comptRendu = models.TextField()


class Radio (models.Model):
    
    patient = models.ForeignKey("users.Patient", on_delete=models.CASCADE, related_name='idPatientRadio', null=True)
    docteur = models.ForeignKey("users.Docteur", on_delete=models.CASCADE, related_name='idDocteurRadio',null=True)
   
    dateOperation = models.DateField(auto_now_add=True)
    description = models.TextField()
    resultat = models.TextField()
    validation = models.BooleanField(default=False)

class Analyse (models.Model):
    patient = models.ForeignKey("users.Patient", on_delete=models.CASCADE, related_name='idPatientAnalyse', null=True)
    docteur = models.ForeignKey("users.Docteur", on_delete=models.CASCADE, related_name='idDocteurAnalyse', null=True)
    
    dateOperation = models.DateField(auto_now_add=True)
    description = models.TextField()
    resultat = models.TextField()
    validation = models.BooleanField(default=False)