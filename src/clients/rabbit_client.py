import pika

from src.clients.base_client import BaseClient


class RabbitClient(BaseClient):  # TODO: aioredis
    def __init__(self):
        super().__init__()
        self.connection = pika.SelectConnection(on_open_callback=self.on_open, on_close_callback=self.on_close)

    def connect(self):
        self.connection.ioloop.start()
        return self.connection

    def disconnect(self):
        self.connection.ioloop.stop()
        self.connection.close()

    def on_open(self):
        # Invoked when the connection is open
        pass

    def on_close(self):
        # Invoked when the connection is closed
        self.connection.ioloop.stop()

    def restart(self):
        ...
