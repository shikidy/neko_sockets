import socket

from .client import Client

class NekoSocket():


    def __init__(self, host: str, port: int, custom_socket: socket = None, timeout: int = 1) -> None:
        self.__host = host
        self.__port = port
        self.__socket = custom_socket if custom_socket else socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__socket.timeout = 1

    def serve(self):
        self.__socket.bind((self.__host, self.__port))

        while 1:
            accepted_con, ip = self.__socket.accept()
            Client(accepted_con, ip).start_listen()




        