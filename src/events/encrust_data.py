import asyncio
from dependency_container import SimpleDependencyContainer


class EncrustData:
    def __init__(self):
        self.web_controller = SimpleDependencyContainer.web_controller
        self.telegram_controller = SimpleDependencyContainer.telegram_controller

    async def start(self):
        while True:
            web_tasks = asyncio.create_task(self.web_controller.start())
            telegram_tasks = asyncio.create_task(self.telegram_controller.start())

            await asyncio.gather(*(web_tasks, telegram_tasks))
            await asyncio.sleep(225)  # TODO: think about timing of this(maybe even put inside settings)
