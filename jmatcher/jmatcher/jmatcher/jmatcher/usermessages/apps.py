from django.apps import AppConfig


class UserMessagesConfig(AppConfig):
    name = 'jmatcher.usermessages'


    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
