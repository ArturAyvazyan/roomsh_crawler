import setuptools
import tomllib
from setuptools import setup


with open("CONFIG.toml", "rb") as f:
    data = tomllib.load(f)
    base_settings = data["base_settings"]
    requirements_settings = base_settings["REQUIREMENTS"]

CONFIG_PATH = f"/requirements/{requirements_settings}"

setup(
    name="roomsh_crawler",
    version="0.1",
    description="specific crawler for Roomsh project",
    author="PullYa",
    author_email="arcanwork@gmail.com",
    packages=setuptools.find_packages(where=CONFIG_PATH),
    install_requires=[
        "fastapi == 0.95.0",
        "uvicorn == 0.21.1",
        "redis == 4.5.4"
        "requests == 2.28",
        "pydantic == 1.10.7",
        "pika == 1.3.2",
        "PyYAML == 6.0",
        'importlib-metadata; python_version == "3.11"',
    ],
    entry_points={
        "console_scripts": ["roomsh_crawler = src.routers.shop_router:app"]
    },
)
