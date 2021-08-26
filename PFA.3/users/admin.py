from django.contrib import admin
from .models import Personne,Patient,Docteur,Analyste,Pharmacien,Radiologue,Dossier
from django.apps import apps
# Register your models here.
admin.site.register(Personne)
admin.site.register(Patient)
admin.site.register(Docteur)
admin.site.register(Analyste)
admin.site.register(Pharmacien)
admin.site.register(Radiologue)
app = apps.get_app_config('graphql_auth')

for model_name, model in app.models.items():
    admin.site.register(model)



