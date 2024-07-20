import socket
from threading import Thread
from typing import List
import logging

from .client import Client
from neko_socket import Dispatcher


class NekoSocket():


    def __init__(self, host: str, port: int, custom_socket: socket = None, buffer_size: int = 1024, max_buffer: int = 4096) -> None:
        self.__host = host
        self.__port = port
        self.__socket = custom_socket if custom_socket else socket.socket()
        self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.dispatcher = Dispatcher()
        self.is_listen = True
        self.__clients: List[Client] = []
        self.__buffer_size = buffer_size
        self.__max_buffer = max_buffer
        self.__listening_thread = None

    def thread_serve(self):
        self.__listening_thread = Thread(target=self.serve)
        self.__listening_thread.start()


    def serve(self):
        self.__socket.bind((self.__host, self.__port))
        self.__socket.listen(5)

        while self.is_listen:
            try:
                accepted_con, ip = self.__socket.accept()
            except:
                break
            client = Client(accepted_con, ip, self.dispatcher)
            client.start_listen(self.__buffer_size, self.__max_buffer)
            self.__clients.append(client)

        for client in self.__clients:
            client.kill()


    def close(self):
        self.is_listen = False
        self.__socket.close()
        self.__listening_thread.join()



        