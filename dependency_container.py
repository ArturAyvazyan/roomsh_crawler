from src.clients.redis_client import RedisClient
from src.controllers.telegram_controller import TelegramController
from src.controllers.web_controller import WebController


class SimpleDependencyContainer:  # Actually it's super simple
    redis_client = RedisClient().connect()
    web_controller = WebController()
    telegram_controller = TelegramController()
