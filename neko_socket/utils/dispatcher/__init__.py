from typing import Callable


class Dispatcher:


    def __init__(self) -> None:
        self.__handlers = {}

    def bind_event(func: Callable):
        def wrapper_args(self, name: str, id: int):
            
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return wrapper_args