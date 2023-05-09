from src.controllers.shop_controller import ShopController
from src.controllers.telegram_controller import TelegramController
from src.controllers.web_controller import WebController


class SimpleDependencyContainer:  # Actually it's super simple
    web_controller = WebController()
    telegram_controller = TelegramController()
    shop_controller = ShopController()
