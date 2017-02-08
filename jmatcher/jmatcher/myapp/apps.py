from django.apps import AppConfig


class MyappConfig(AppConfig):
    name = 'jmatcher.myapp'
    verbose_name = "Myapps"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
