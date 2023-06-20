from django.contrib import admin
from django.apps import apps

app = apps.get_app_config('main')

model_admins = {}

for model_name, model in app.models.items():

    if model_name in model_admins.keys():
        admin.site.register(model, model_admins[model_name])
    else:
        admin.site.register(model)
