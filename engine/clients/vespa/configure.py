from vespa.deployment import VespaCloud, VespaDocker

from engine.base_client.configure import BaseConfigurator


class VespaConfigurator(BaseConfigurator):
    def __init__(self, host, collection_params: dict, connection_params: dict):
        super().__init__(host, collection_params, connection_params)
        self.client = ...

    def clean(self):
        raise NotImplementedError()

    def recreate(
            self,
            distance,
            vector_size,
            collection_params,
    ):
        self.clean()
        raise NotImplementedError()


if __name__ == '__main__':
    pass
