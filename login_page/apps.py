from django.apps import AppConfig


class LoginPageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'login_page'

    def ready(self):
        import login_page.signals