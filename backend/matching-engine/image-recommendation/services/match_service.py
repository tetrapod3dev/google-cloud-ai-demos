from typing import Any, List

from google.cloud.aiplatform.matching_engine import matching_engine_index_endpoint

class MatchService:
    def __init__(self, index_endpoint_id: str, deployed_index_id: str, name: str) -> None:
        self.index_endpoint = matching_engine_index_endpoint.MatchingEngineIndexEndpoint(index_endpoint_id)
        self.deployed_index_id = deployed_index_id

    def convert_to_embeddings(self, image):
        pass

    def match(self, image, num_neighbors: int) -> List[Any]:

        embeddings = self.convert_to_embeddings(image)
        
        response = self.index_endpoint.match(
            deployed_index_id=self.deployed_index_id,
            queries=[embeddings],
            num_neighbors=num_neighbors,
            filter=[matching_engine_index_endpoint.Namespace("class", ["even"])],
        )

        response