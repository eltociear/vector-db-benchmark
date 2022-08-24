from vespa.package import ApplicationPackage, Document, Field, HNSW, QueryProfile, Schema, RankProfile, FieldSet, \
    QueryProfileType, QueryTypeField

from engine.base_client.distances import Distance
from engine.clients.vespa.config import VESPA_SCHEMA_NAME, VESPA_APP_NAME


class VesaApp(ApplicationPackage):
    DISTANCE_MAPPING = {
        Distance.L2: "euclidean",
        Distance.COSINE: "angular",
        Distance.DOT: "angular",
    }

    def __init__(self, vector_size, distance, max_links_per_node, neighbors_to_explore_at_insert):
        document = Document(
            fields=[
                Field(name="context_id", type="int", indexing=["summary", "attribute"]),
                Field(
                    name="embeddings",
                    type=f"tensor<float>(x[{vector_size}])",
                    indexing=["attribute", "index"],
                    ann=HNSW(
                        distance_metric=distance,
                        max_links_per_node=max_links_per_node,
                        neighbors_to_explore_at_insert=neighbors_to_explore_at_insert,
                    ),
                )

            ]
        )
        schema = Schema(
            name=VESPA_SCHEMA_NAME,
            document=document,
            fieldsets=[FieldSet(name="default", fields=["embeddings"])],
            rank_profiles=[
                RankProfile(
                    name="semantic-similarity",
                    inherits="default",
                    first_phase="closeness(embeddings)",
                ),
            ],
        )
        super().__init__(
            name=VESPA_APP_NAME,
            schema=[schema],
            query_profile=QueryProfile(),
            query_profile_type=QueryProfileType(
                fields=[
                    QueryTypeField(
                        name="ranking.features.query(query_embedding)",
                        type=f"tensor<float>(x[{vector_size}])",
                    )
                ]
            ),
        )
