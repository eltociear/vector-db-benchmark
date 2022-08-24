from typing import List, Optional

import numpy as np

from engine.base_client.upload import BaseUploader


class RedisUploader(BaseUploader):
    client = None
    upload_params = {}

    @classmethod
    def init_client(cls, host, distance, connection_params, upload_params):
        cls.client = ...
        cls.upload_params = upload_params

    @classmethod
    def upload_batch(
        cls, ids: List[int], vectors: List[list], metadata: Optional[List[dict]]
    ):
        raise NotImplementedError()

    @classmethod
    def post_upload(cls, _distance):
        return {}

