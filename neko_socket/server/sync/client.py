import logging
from threading import Thread

import socket

from neko_socket import Dispatcher, DataEncoder


logger = logging.getLogger(__name__)

class Client:

    def __init__(self, conn: socket.socket, ip: socket._RetAddress, dispatcher: Dispatcher) -> None:
        self.__conn = conn
        self.__ip = ip
        self.__dp = dispatcher

    @property
    def conn(self):
        return self.__conn
    
    @property
    def ip(self):
        return self.__ip
    
    def kill(self):
        self.conn.close()

    def thread_worker(self, data: bytes):
        try:
            decoded_data = DataEncoder.decode(data)
            if len(decoded_data) < 0:
                #FIXME отлов нулевой даты. Нам хотя б айди ивента
                return
            # id, arg1, arg2 ...
            self.__dp.execute_event(decoded_data[0], decoded_data[1:])
        except ValueError as err:
            logger.exception(err)
        
        except Exception as err:
            logger.exception(f"Unexpected err: {err}")
        

    def execute_with_new_thread(self, data: bytes):
        Thread(
            target=self.thread_worker,
            args=(data,)
        ).start()

    def listen(self, buffer_bytes: int=1024, max_buffer_size: int=1024):
        buffer = bytes()
        while 1:
            readed_bytes =  self.__conn.recv(buffer_bytes)
            if len(readed_bytes) == 0:
                logger.debug(f"{self.ip} connection was closed")
                # Connection was closed
                break
            
            if len(buffer) + len(readed_bytes) > max_buffer_size:
                logger.debug(f"{self.ip} sended more bytes that allowed")
                self.kill()
                continue

            buffer += readed_bytes

            if len(readed_bytes) < buffer_bytes:
                self.execute_with_new_thread(buffer)
                break



            
            

