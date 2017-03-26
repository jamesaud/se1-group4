from django.apps import AppConfig


class StudentConfig(AppConfig):
    name = 'jmatcher.students'

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
