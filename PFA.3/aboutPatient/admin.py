from django.contrib import admin
from .models import Consultation,Dossier,Analyse,Radio,Prescription,Chambre
# Register your models here.
admin.site.register(Consultation)
admin.site.register(Dossier)
admin.site.register(Analyse)
admin.site.register(Radio)
admin.site.register(Prescription)
admin.site.register(Chambre)