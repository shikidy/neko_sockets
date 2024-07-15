import zlib
from typing import List, Union


class DataZipper:
    data_split =b'\x00'

    @staticmethod
    def zip(method_id: int, *data: List[Union[str, int]], int_bytes: int = 3, method_id_bytes: int = 3, compress_level: int = 1) -> bytes:
        result: bytes = method_id.to_bytes(method_id_bytes, "big")

        for el in data:
            if isinstance(el, str):
                result +=  DataZipper.data_split + el.encode("utf-8")
            elif isinstance(el, int):
                #TODO OverflowError
                result +=  DataZipper.data_split + el.to_bytes(int_bytes, "big")
            else:
                raise TypeError(f"Can not read {type(el)} type!")
        return zlib.compress(result) if len(result) > 12 else result