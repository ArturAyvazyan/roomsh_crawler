from abc import ABCMeta, abstractmethod


class BaseClient(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        self.timeout = 2.5
        self.host = ...
        self.port = ...

    @abstractmethod
    def connect(self, *args):
        ...

    @abstractmethod
    def disconnect(self, *args):
        ...

    @abstractmethod
    def restart(self):
        ...
