from core.repository.base_repository import CRUDRepository
from ..models import Scenario


class ScenarioRepository(CRUDRepository):
    def __init__(self):
        super().__init__(Scenario)

