from django.apps import AppConfig


class EmployerConfig(AppConfig):
    name = 'jmatcher.employers'

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
