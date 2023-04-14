from abc import ABCMeta, abstractmethod


class BaseClient(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        self.timeout = 2.5
        self.host = ...
        self.port = ...
        self.server = ...

    @abstractmethod
    def connect(self):
        ...

    @abstractmethod
    def disconnect(self):
        ...

    @abstractmethod
    def restart(self):
        ...
