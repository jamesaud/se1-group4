from django.apps import AppConfig


class ShipmentsConfig(AppConfig):
    name = '{{YOURPROJECTNAME}}.django-starter-app'
    verbose_name = "django-starter-app"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
