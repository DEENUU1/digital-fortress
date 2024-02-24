from scenario.repository.scenario import ScenarioRepository
from scenario.tasks import run_ai_client_task


class ScenarioService:

    def __init__(self, repository: ScenarioRepository):
        self._repository = repository

    def create(self, data, user_id: int):
        obj = self._repository.create(data)

        run_ai_client_task(
            obj.project.slug,
            user_id,
            "gpt-3.5-turbo-16k-0613",
            obj.id,
            data.get("user_details"),
        )
        return obj

    def delete(self, user, _id: int) -> None:
        self._repository.delete(_id, user)

    def get_all(self, user, project_id: int):
        return self._repository.get_tree(project_id, user)

    def has_root(self, user, project_id: int) -> bool:
        root = self._repository.get_root(project_id, user)
        return root is not None

    def get_by_id(self, user, _id: int):
        return self._repository.get_by_id(_id, user)
