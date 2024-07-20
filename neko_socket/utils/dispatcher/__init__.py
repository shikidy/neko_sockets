from typing import Callable, List

from .handler import Handler


class Dispatcher:


    def __init__(self) -> None:
        self.__handlers = {}

    def add_event(self, callback: Callable, name: str, id: int):
        handler: Handler = self.__handlers.get(id, None)
        if handler:
            raise ValueError(f"Id {id} already registered! Used for {handler.callback.__name__} func")

        self.__handlers[id] = Handler(name, id, callback)

    def bind_event(self, name: str, id: int):
        def wrapper_args(func: Callable):
            self.add_event(func, name, id)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return wrapper_args
    
    def execute_event(self, id: int, data: List[str]): 
        handler: Handler = self.__handlers.get(id, None)
        if not handler:
            raise ValueError(f"Can not find handler with id {id}")
        handler.execute(*data)
        