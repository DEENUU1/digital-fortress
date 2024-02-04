from django.apps import AppConfig


class ScenarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scenario'

    def ready(self):
        import scenario.signals
        print("Scenario Signals Connected")
