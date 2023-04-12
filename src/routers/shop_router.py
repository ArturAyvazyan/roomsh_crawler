from fastapi import FastAPI, APIRouter

app = FastAPI()

shop_router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


@shop_router.get("/ping")
def pong():
    return {"ping": "pong!"}