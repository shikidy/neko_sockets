from typing import List, Union


class DataEncoder:
    @staticmethod
    def encode(*data: List[Union[str, int, float]], int_bytes: int = 3) -> bytes:
        result: bytes = bytes()
        lenghts: List[int] = []
        for el in  data:
            converted = bytes()
            if isinstance(el, (int, float)):
                el = str(el)
            converted = el.encode("utf-8")
            lenghts.append(len(converted))
            result += converted
        final_result: bytes = len(lenghts).to_bytes(int_bytes, "big")
        for lenght in lenghts:
            final_result += lenght.to_bytes(int_bytes, "big")
        final_result += result
        return final_result
    
    @staticmethod
    def decode(data: bytes, int_bytes: int = 3) -> List[Union[str]]:
        result = []
        lenghts = []
        items_amount = int.from_bytes(data[:int_bytes], "big")
        for i in range(int_bytes, items_amount*int_bytes+int_bytes, int_bytes):
            lenghts.append(
                int.from_bytes(data[i:i+int_bytes], "big")
            )
        data_sector = data[i+int_bytes:]
        offset = 0
        for lenght in lenghts:
            parsed_data: bytes = data_sector[offset:lenght+offset]
            result.append(
                parsed_data.decode("utf-8")
            )
            offset = offset + lenght
        return result
    


