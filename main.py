import asyncio

from fastapi import FastAPI

from src.routers.shop_router import shop_router
from src.events.main_server import MainServer
from src.events.encrust_data import EncrustData


app = FastAPI()
app.include_router(shop_router)


@app.on_event("startup")
async def start():
    data_encruster = EncrustData()
    asyncio.create_task(data_encruster.start())


if __name__ == "__main__":
    main_server = MainServer()
    asyncio.run(main_server.start())
