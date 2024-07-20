from typing import Callable


class Handler:

    
    def __init__(self, name: str, id: int, callback: Callable) -> None:

        if not isinstance(id, int):
            raise TypeError(f"Id must be int, not {type(id)}")
        if not isinstance(name, str):
            raise TypeError(f"Name must be str, not {type(str)}")
        if not isinstance(callback, Callable):
            raise TypeError(f"callback must be callable, not {type(callback)}")
        
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
    
    def execute(self, *args, **kwrags):
        self.__callback(*args, **kwrags)