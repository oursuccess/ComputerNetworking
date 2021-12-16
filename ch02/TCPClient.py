# -*- coding: UTF-8 -*-
"""
@Script of TCPClient, get input from player, and print the message from server
@File : TCPClient.py
@Time : 2021/12/16 10:01
@copyright : Je Zhang
@author : Je Zhang
"""
import string
from socket import *

__SERVER_ADDRESS__ = "127.0.0.1"
__SERVER_PORT__ = 11998

__BUF_SIZE__ = 2048


class TCPClient:
    def __init__(self):
        self.socket = None  # 客户端的socket

    def start_client(self, server: str, port: int):
        self.socket = socket(AF_INET, SOCK_STREAM)  # 创建一个TCP的socket
        self.socket.connect((server, port))  # 试图和指定服务器的指定端口建立连接
        print('please input lower case string, and I will encode them to upper case string')
        print('input . to stop')
        input_str = input()
        while input_str != '.':
            self.socket.send(input_str.encode())
            received_bytes = self.socket.recv(__BUF_SIZE__)
            print(('the target string is : %s', received_bytes.decode()))
            input_str = input()
        self.socket.shutdown(SHUT_RDWR)  # 关闭连接
        self.socket.close()
        print('connection has closed, you can leave now!')


if __name__ == "__main__":
    TCPClient().start_client(__SERVER_ADDRESS__, __SERVER_PORT__)
