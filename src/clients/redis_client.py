import redis
from config_handler import redis_settings

r = redis.Redis(host=redis_settings.HOST, port=redis_settings.PORT, decode_responses=True)
