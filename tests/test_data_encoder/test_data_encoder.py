import time
import typing

import pytest

from neko_socket import DataEncoder


class TestDataEncoder:
    @pytest.mark.parametrize(
            "data_sample", [
                ["1", "some_data", "coolest data", "tewst"],
                ["3", "doo", "qwe data", "ee"]
            ]
    )
    def test_encode_decode_same_data(self, data_sample: typing.List):
        """Test decoded and encoded data must me same
        """
        bytes_result = DataEncoder.encode(*data_sample)
        assert DataEncoder.decode(bytes_result) == data_sample, "Encoded data doesnt match decoded"