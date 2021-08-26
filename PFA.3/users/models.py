from django.db import models
from django.contrib.auth.models import AbstractUser
from aboutPatient.models import Dossier, Consultation, Radio, Analyse, Chambre,Prescription

# Create your models here.
# def get_profile_iage_filepath(self, filename):
#     return f'profile_image/{self.pk}/{"profile_image.png}'

class Personne(AbstractUser):
    email = models.EmailField(blank=False, max_length=254, verbose_name="email",unique=True)
    #first_name = models.CharField(max_length=30)
    #last_name = models.CharField(max_length=30)
    adresse = models.CharField(max_length=254)
    telephone = models.CharField(max_length=20)

    #profile_image = models.ImageField(max_length=255, upload_to= , null = True, blank = True, default=)
    dateDeNaissance = models.DateField(default="2020-01-01") 
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    
    
    
        



class Patient (Personne):
   pass
    
    
    

class Docteur (Personne):
    specialite = models.CharField(max_length=100)

class Analyste (Personne):
    pass

class Radiologue (Personne):
    pass

class Pharmacien (Personne):
    pass
#----------------------------------------------------------------------------------------------------------------









 
