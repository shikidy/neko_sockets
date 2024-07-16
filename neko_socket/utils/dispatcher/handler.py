from typing import Callable


class Handler:

    
    def __init__(self, name: str, id: int, callback: Callable) -> None:
        self.__name = name
        self.__id = id
        self.__callback = callback

    @property
    def name(self):
        return self.__name
    
    @property
    def id(self):
        return self.__id
    
    @property
    def callback(self):
        return self.__callback