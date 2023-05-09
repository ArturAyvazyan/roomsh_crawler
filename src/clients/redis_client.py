import redis
from config_handler import redis_settings

from src.clients.base_client import BaseClient


class RedisClient(BaseClient):  # TODO: aioredis
    def __init__(self):
        super().__init__()
        self.host = redis_settings["HOST"]
        self.port = redis_settings["PORT"]

    def connect(self):
        return redis.Redis(
            host=self.host,
            port=self.port,
            decode_responses=True,
        )

    def disconnect(self):
        ...

    def restart(self):
        ...
