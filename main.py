import asyncio

import uvicorn
from fastapi import FastAPI

from config_handler import server_settings
from src.routers.shop_router import shop_router
from src.events.crawler import Crawler


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
    asyncio.create_task(Crawler.start())


if __name__ == "__main__":
    asyncio.run(run())
