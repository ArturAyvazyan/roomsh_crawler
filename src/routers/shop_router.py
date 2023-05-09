from fastapi import APIRouter, Body
from dependency_containers.controller_dependency import SimpleDependencyContainer
from src.models.shop_models import ShopModel, Product, ShopInformation

shop_controller = SimpleDependencyContainer.shop_controller

shop_router = APIRouter(
    prefix="/shops",
    tags=["shops"],
    responses={404: {"description": "Not found"}},
)


@shop_router.post("/get_shops")
def get_shops() -> dict:
    return shop_controller.get_shops()


@shop_router.post("/get_shop")
def get_shop(shop: str = Body(embed=True)) -> ShopModel:
    return shop_controller.get_shop(shop=shop)


@shop_router.post("/get_shops_product")
def get_shops_product(shop: str = Body(embed=True)) -> Product:
    shop = shop_controller.get_shop(shop=shop)
    product = shop["product"]
    return Product.parse_obj(product)


@shop_router.post("/get_shops_info")
def get_shops_info(shop: str = Body(embed=True)) -> ShopInformation:
    shop = shop_controller.get_shop(shop=shop)
    shop_info = shop["shop_info"]
    return ShopInformation.parse_obj(shop_info)
