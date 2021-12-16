# -*- coding: UTF-8 -*-
"""
@Script of UDPClient
@File : UDPClient.py
@Time : 2021/12/16 9:19
@copyright : Je Zhang
@author : Je Zhang
"""

from socket import *

__HOST_NAME__ = "127.0.0.1"  # 服务器名称
__SERVER_PORT__ = 12000  # 服务器端口号

__BUF_SIZE__ = 2048  # 客户端接收窗口的最大大小


class UDPClient:
    def __init__(self):
        self.clientSocket = None  # 以后实际创建的客户端socket，每次start都会创建一个

    def start_client(self):
        # 这里声明了其使用IPv4(AF_INET)，为UDP(SOCK_DGRAM)
        self.clientSocket = socket(AF_INET, SOCK_DGRAM)  # 创建实际的客户端socket
        print('Input lowercase sentence:')
        message = input()  # 接收玩家输入
        self.clientSocket.sendto(message.encode(), (__HOST_NAME__, __SERVER_PORT__))  # 向服务器发送信息，要求是bytes
        modified_message, server_address = self.clientSocket.recvfrom(__BUF_SIZE__)  # 从服务器接收信息
        print(modified_message.decode())  # 将从服务器收到的bytes转换为string
        self.clientSocket.close()


if __name__ == '__main__':
    print('hi client start')
    UDPClient().start_client()
