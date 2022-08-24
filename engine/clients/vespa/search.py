from typing import List, Tuple

from engine.base_client.search import BaseSearcher


class VespaSearcher(BaseSearcher):
    search_params = {}
    client = None

    @classmethod
    def init_client(cls, host, distance, connection_params: dict, search_params: dict):
        cls.client = ...
        cls.search_params = search_params

    @classmethod
    def search_one(cls, vector, meta_conditions, top) -> List[Tuple[int, float]]:
        raise NotImplementedError()
