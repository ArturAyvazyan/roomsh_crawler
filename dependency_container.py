from src.clients.redis_client import RedisClient


class SimpleDependencyContainer:  # Actually it's super simple
    redis_client = RedisClient()
