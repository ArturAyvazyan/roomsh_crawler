import redis
from config_handler import redis_settings

from src.models.models import ShopModel
from src.clients.base_client import BaseClient


class RedisClient(BaseClient):
    def __init__(self):
        self.host = redis_settings["HOST"]
        self.port = redis_settings["PORT"]
        self.server = redis.Redis(
            host=redis_settings["HOST"],
            port=redis_settings["PORT"],
            decode_responses=True,
        )

    def add_shop(self, shop: ShopModel):
        ...

    def update_shop(self, shop: ShopModel):
        ...

    def get_shop(self, shop: str) -> ShopModel:
        shop = self.server.get(shop)
        return ShopModel.parse_obj(shop)

    def get_all_shops(self) -> dict[str: ShopModel]:
        all_shops = self.server.scan()
        result = dict()
        for shop in all_shops:
            result.update({shop: ShopModel.parse_obj(all_shops[shop])})
        return result

    def clear_all(self):
        self.server.flushall()

    def get_diff(self, shop: ShopModel):
        ...  # FIXME: скорее всего нужно бы реализовать в основном проекте
