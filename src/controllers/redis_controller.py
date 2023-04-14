from src.models.shop_models import ShopModel
from src.controllers.base_controlelr import BaseDataController
from src.repositories.redis_repository import RedisRepository


class RedisController(BaseDataController):
    def __init__(self):
        self.repository = RedisRepository()

    async def get_shop(self, shop: str) -> ShopModel:
        return await self.repository.get_shop(shop=shop)

    async def update_shop(self, **shop_kwargs):
        shop = ShopModel.parse_obj(shop_kwargs)
        shop_old_data = self.get_shop(shop.name)
        if shop != shop_old_data:
            raise ...

        return await self.repository.update_shop(shop=shop)

    async def add_shop(self, **shop_kwargs):
        shop = ShopModel.parse_obj(shop_kwargs)
        return await self.repository.add_shop(shop=shop)

    async def get_shops(self) -> dict[str: ShopModel]:
        return await self.repository.get_shops()

    async def clear_all(self):
        return await self.repository.clear_all()

    async def get_diff(self, shop: ShopModel):
        # FIXME: скорее всего нужно бы реализовать в основном проекте
        return await self.repository.get_diff(shop=shop)
