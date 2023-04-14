from src.models.shop_models import ShopModel
from dependency_container import SimpleDependencyContainer


class RedisRepository:
    def __init__(self):
        self.server = SimpleDependencyContainer.redis_client.connect()

    async def get_shop(self, shop: str) -> ShopModel:
        shop = self.server.get(shop)
        return ShopModel.parse_obj(shop)

    async def update_shop(self, shop: ShopModel):
        ...

    async def add_shop(self, shop: ShopModel):
        ...

    async def get_shops(self) -> dict[str: ShopModel]:
        all_shops = self.server.scan()
        result = dict()
        for shop in all_shops:
            result.update({shop: ShopModel.parse_obj(all_shops[shop])})
        return result

    async def clear_all(self):
        self.server.flushall()

    async def get_diff(self, shop: ShopModel):
        ...
