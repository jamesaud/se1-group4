from django.apps import AppConfig


class PostsConfig(AppConfig):
    name = 'jmatcher.posts'

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
