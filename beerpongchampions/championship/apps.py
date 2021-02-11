from django.apps import AppConfig


class ChampionshipConfig(AppConfig):
    name = 'championship'

    def ready(self):
        import championship.signals