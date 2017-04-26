from django.apps import AppConfig


class ChatRoomConfig(AppConfig):
    name = 'jmatcher.chatRoom'

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
