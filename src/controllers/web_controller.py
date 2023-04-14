import asyncio
import requests

from src.controllers.base_controlelr import BaseActionController


class WebController(BaseActionController):
    def __init__(self):
        super().__init__()

    async def start(self):
        while True:
            tasks = list()
            for website in self.websites:
                session = requests.session()
                session.get(website)

                task = asyncio.create_task(self.crawl(website=website))
                tasks.append(task)

            await asyncio.gather(*tasks)

    async def crawl(self, website):
        ...

    async def scrape(self, websites):
        ...

    async def sleep(self, timeout: int):
        ...
