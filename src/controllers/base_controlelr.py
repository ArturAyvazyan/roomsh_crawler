from abc import ABCMeta, abstractmethod
from config_handler import websites_to_crawl
from src.models.shop_models import ShopModel


class BaseActionController(metaclass=ABCMeta):
    def __init__(self):
        self.websites = websites_to_crawl.values()

    @abstractmethod
    def start(self):
        ...

    @abstractmethod
    def crawl(self, website):
        ...

    @abstractmethod
    async def scrape(self, websites):
        ...

    @abstractmethod
    async def sleep(self, timeout: int):
        ...


class BaseDataController(metaclass=ABCMeta):
    @abstractmethod
    async def get_shop(self, shop: str) -> ShopModel:
        ...

    @abstractmethod
    async def update_shop(self, shop: ShopModel):
        ...

    @abstractmethod
    async def add_shop(self, shop: ShopModel):
        ...

    @abstractmethod
    async def get_shops(self) -> dict[str: ShopModel]:
        ...

    @abstractmethod
    async def clear_all(self):
        ...

    @abstractmethod
    async def get_diff(self, shop: ShopModel):
        ...
