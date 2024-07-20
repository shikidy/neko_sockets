import time
import socket
import logging
import pytest
from threading import Thread

from neko_socket import NekoSocket, DataEncoder


class TestServerConnections:

    def setup_method(self):
        self.server = NekoSocket("localhost", 10205, buffer_size=1024, max_buffer=4096)
        self.server.thread_serve()

    def teardown_method(self):
        self.server.close()

    @pytest.mark.skip
    def test_send_and_recieve_data(self):
        gotted_data = None
        test_data = ("1", "MyNameIs", "python")

        @self.server.dispatcher.bind_event("testevent", 1)
        def local_event(*data):
            nonlocal gotted_data
            gotted_data = data

        encoded = DataEncoder.encode(*test_data)
        client = socket.socket()
        client.connect(('localhost', 10205))
        client.send(encoded)

        timeout = 9
        while timeout and not gotted_data:
            time.sleep(1)
            timeout -= 1

        assert gotted_data == test_data[1:], "Sended and recieved data should be the same"



