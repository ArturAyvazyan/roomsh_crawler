import asyncio

import uvicorn
from fastapi import FastAPI

from config_handler import server_settings
from src.routers.shop_router import shop_router
from src.events.encrust_data import EncrustData


app = FastAPI()
app.include_router(shop_router)


async def run():
    config = uvicorn.Config(
        "main:app",
        host=server_settings["HOST"],
        port=server_settings["PORT"],
        reload=True,
        log_level="trace",
    )
    server = uvicorn.Server(config)
    await server.serve()


@app.on_event("startup")
async def start():
    data_encruster = EncrustData()
    asyncio.create_task(data_encruster.start())


if __name__ == "__main__":
    asyncio.run(run())
