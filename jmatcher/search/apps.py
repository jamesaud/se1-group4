from django.apps import AppConfig


class SearchConfig(AppConfig):
    name = 'jmatcher.search'

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
