from abc import ABCMeta, abstractmethod

from src.models.models import ShopModel


class BaseClient(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        self.host = ...
        self.port = ...
        self.server = ...

    @abstractmethod
    def add_shop(self, shop: ShopModel):
        ...

    @abstractmethod
    def update_shop(self, shop: ShopModel):
        ...

    @abstractmethod
    def get_shop(self, shop: str) -> ShopModel:
        ...

    @abstractmethod
    def get_all_shops(self) -> dict[str: ShopModel]:
        ...

    @abstractmethod
    def clear_all(self):
        ...

    @abstractmethod
    def get_diff(self, shop: ShopModel):
        ...
