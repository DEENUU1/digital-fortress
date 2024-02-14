from celery import shared_task
from scenario.ai.run import run_ai_client


@shared_task()
def run_ai_client_task(user_id: int, model: str, scenario_id: int, user_input: str = ""):
    return run_ai_client(user_id, model, scenario_id, user_input)
