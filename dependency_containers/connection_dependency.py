from src.clients.rabbit_client import RabbitClient
from src.clients.redis_client import RedisClient


class SimpleConnectionDependencyContainer:  # Actually it's super simple
    redis_client = RedisClient().connect()
    rabbit_client = RabbitClient().connect()
