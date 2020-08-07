from django.apps import AppConfig


class SocialAppsConfig(AppConfig):
    name = 'Social_Apps'

    def ready(self):
        import Social_Apps.signals
