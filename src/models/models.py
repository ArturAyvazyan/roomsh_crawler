from typing import Union
from pydantic import BaseModel, validator
from src.models.enums import LegalForms, Cities, ShroomType


class SpotAddress(BaseModel):
    city: list[Cities]
    index: str
    street: str
    house: str


class ShopInformation(BaseModel):
    city: list[Cities]
    real_spot: bool
    legal_form: LegalForms
    inn: str
    ogrn: str
    main_email: Union[str, None] = None
    additional_email: Union[str, None] = None
    contact_phone: Union[str, None] = None

    @validator("inn")
    def _inn(cls, v):
        # 7743013902
        return v.inn

    @validator("ogrn")
    def _ogrn(cls, v):
        # 1053600591197
        # 484833211
        return v.ogrn


class Product(BaseModel):
    name: str
    shroom_type: ShroomType
    category_type: str
    amount: int
    weight: int
    price: int


class ShopModel(Product, ShopInformation, SpotAddress):
    name: str
