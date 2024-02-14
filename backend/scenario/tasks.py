from celery import shared_task
from scenario.ai.run import run_ai_client
from scenario.models import Scenario


@shared_task()
def run_ai_client_task(user_id: int, model: str, scenario_id: int, user_input: str = "") -> None:
    response = run_ai_client(user_id, model, scenario_id, user_input)

    # Update scenario object with generated response
    scenario_obj = Scenario.objects.get(id=scenario_id)
    scenario_obj.response = response
    scenario_obj.save()
