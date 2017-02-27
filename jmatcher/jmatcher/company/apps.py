from django.apps import AppConfig


class CompanyConfig(AppConfig):
    name = 'jmatcher.company'
    verbose_name = "company"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
