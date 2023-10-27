from typing import List, Optional

import psycopg2
from psycopg2.extras import RealDictCursor

from engine.base_client.upload import BaseUploader
from engine.clients.pgvector.config import get_db_config


class PgVectorUploader(BaseUploader):
    client = None
    upload_params = {}

    @classmethod
    def init_client(cls, host, distance, connection_params, upload_params):
        cls.conn = psycopg2.connect(**get_db_config())
        cls.cur = cls.conn.cursor(cursor_factory=RealDictCursor)
        cls.upload_params = upload_params

    @classmethod
    def upload_batch(
        cls, ids: List[int], vectors: List[list], metadata: Optional[List[dict]]
    ):
        INSERT_EMBEDDING_QUERY = """
        INSERT INTO items (id, embedding) VALUES (%s, %s)
        """
        cls.cur.executemany(
            INSERT_EMBEDDING_QUERY, [(id, vector) for id, vector in zip(ids, vectors)]
        )
        cls.conn.commit()
