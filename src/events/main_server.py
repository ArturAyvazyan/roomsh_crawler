import uvicorn
from config_handler import server_settings


class MainServer:
    def __init__(self):
        self.host = server_settings["HOST"]
        self.port = server_settings["PORT"]

    async def start(self):
        config = uvicorn.Config(
            "main:app",
            host=self.host,
            port=self.port,
            reload=True,
            log_level="trace",
        )
        server = uvicorn.Server(config)
        await server.serve()
