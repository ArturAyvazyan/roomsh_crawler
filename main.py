import uvicorn
from config_handler import server_settings
from fastapi import FastAPI

app = FastAPI()


def run():
    uvicorn.run(
        "src.routers.shop_router:app",
        host=server_settings["HOST"],
        port=server_settings["PORT"],
        reload=True,
        log_level="trace"
    )


if __name__ == '__main__':
    run()
