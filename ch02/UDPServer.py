# -*- coding: UTF-8 -*-
"""
@Script of Server in UDP
@File : UDPServer.py
@Time : 2021/12/16 9:48
@copyright : Je Zhang
@author : Je Zhang
"""

from socket import *

__SERVER_PORT__ = 12000

__BUF_SIZE__ = 2048


class UDPServer:
    def __init__(self):
        self.server_socket = socket(AF_INET, SOCK_DGRAM)  # 服务器socket，服务器不会主动关闭

    def start_server(self, port: int):
        self.server_socket.bind(('', port))  # 将服务器socket与端口绑定
        print('server is ready to receive')
        while True:
            message, client_address = self.server_socket.recvfrom(__BUF_SIZE__)  # 从客户端监听信息
            modified_message = message.decode().upper()  # 将信息转为大写
            self.server_socket.sendto(modified_message.encode(), client_address)  # 向客户端发回该信息


if __name__ == '__main__':
    UDPServer().start_server(__SERVER_PORT__)
