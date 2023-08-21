from django.apps import AppConfig
from taskman import signals


class TaskmanConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    
    name = 'taskman'


    