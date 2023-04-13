import asyncio
import requests


WEBSITES_TO_CRAWL = {
    "fungiline": "https://fungiline.com/",
    "amanita_club": "https://amanita.club/",
    "grib_spb": "https://grybspb.ru/",
}

keywords = ["магазин", "продукция", "каталог"]


class Crawler:
    @staticmethod
    async def start():
        tasks = list()
        for website in WEBSITES_TO_CRAWL.values():
            session = requests.session()
            session.get(website)

            task = asyncio.create_task(Crawler.crawl(website=website))
            tasks.append(task)

        await asyncio.gather(*tasks)

    @staticmethod
    async def crawl(website: str = None):  # TODO this
        print('vicious')
        await asyncio.sleep(5)
        print('ferocious')


class Scraper:
    @staticmethod
    async def scrape(page):  # TODO this
        print(f"{page = }")
        await asyncio.sleep(25)
        print("outside")
        # TODO: Get all pages of site
        # TODO: run task to check if there is prices
