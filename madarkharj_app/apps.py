from django.apps import AppConfig


class MadarkharjAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'madarkharj_app'
    
    def ready(self):
        import madarkharj_app.signals
        
        
