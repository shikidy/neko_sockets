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
        # 12 cuz prefix = 8 + (symb count)
        # print(len(result))
        # return result
        return zlib.compress(result) if len(result) > 12 else result


res = DataZipper.zip(1, "Hello World!", "SecondMessage!", "Heeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeewqceqwceqcweqwcecqwcekceqwkceolqw.eqwjekvqwjevkqwjekqwjekqwvjeqwk,vejqwviejqwv,eiuhjv2u3vh12u3vh123vqwhejqwhevqwuhev123h12v8k3h123j1h23k812vkh3v12j3vuh1mllo World", 201, 408)
# print(len(res))
# print(res)