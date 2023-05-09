
from src.controllers.base_controller import BaseActionController


class TelegramController(BaseActionController):

    def __init__(self):
        super().__init__()

    async def start(self):
        ...

    async def crawl(self, website):
        ...

    async def scrape(self, websites):
        ...

    async def sleep(self, timeout: int):
        ...
