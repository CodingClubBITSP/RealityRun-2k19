from django.apps import AppConfig


class SportzillaConfig(AppConfig):
    name = 'sportzilla'

    def ready(self):
        import sportzilla.signals
