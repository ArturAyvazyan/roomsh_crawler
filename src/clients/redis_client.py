import redis
from config_handler import redis_settings

from src.clients.base_client import BaseClient


class RedisClient(BaseClient):  # TODO: aioredis
    def __init__(self):
        super().__init__()
        self.host = redis_settings["HOST"]
        self.port = redis_settings["PORT"]

    def connect(self):
        self.server = redis.Redis(
            host=redis_settings["HOST"],
            port=redis_settings["PORT"],
            decode_responses=True,
        )
        return self.server

    def disconnect(self):
        ...

    def restart(self):
        ...
