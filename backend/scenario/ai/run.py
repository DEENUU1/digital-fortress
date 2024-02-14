from scenario.repository.scenario import ScenarioRepository
from user.repository.user import UserAccountRepository
from user.services.user import UserAccountService
from .client import AIClient


def _process_full_path(scenario_id: int) -> str:
    full_path = ScenarioRepository().get_full_path(scenario_id=scenario_id)

    result = []

    for data in full_path:
        text = ""
        if data.user_details:
            text += f"User details: {data.user_details}"
            text += "\n"
        if data.response:
            text += f"AI Response: {data.response}"
            text += "\n"

        result.append(text)

    return "\n".join(result)


def run_ai_client(user_id: int, model: str, scenario_id: int, user_input: str = ""):
    try:
        __user = UserAccountService(UserAccountRepository()).get(user_id)
        full_path = _process_full_path(scenario_id)

        client = AIClient(openai_key=__user.openai_key, model=model)

        return client.run(user_input=user_input, scenarios=full_path)

    except Exception as e:
        print(e)
