# -*- coding: UTF-8 -*-
"""
@Script of TCPServer, a simple script that encodes lower characters to upper and return to client
@File : TCPServer.py
@Time : 2021/12/16 10:22
@copyright : Je Zhang
@author : Je Zhang
"""

from socket import *

__SERVER_PORT__ = 12001

__SERVER_CAPACITY__ = 1

__BUF_SIZE__ = 2048


class TCPServer:
    def __init__(self):
        self.socket = None  # 创建一个服务器的tcpSocket
        self.connected_sockets = {}  # 记录所有已经建立链接的套接字字典 key--value: peer_address--socket

    def start_server(self, port: int, capacity: int):
        self.socket = socket(AF_INET, SOCK_STREAM)  # 创建一个socket
        self.socket.bind('localhost', port)  # 将该socket与允许连接的IP绑定
        self.socket.listen(capacity)  # 开始监听
        while True:
            connected_socket, peer_address = self.socket.accept()  # 已经建立好TCP链接的套接字
            self.connected_sockets[peer_address] = connected_socket  # 将建立好链接的套接字加入字典
            while True:
                received_bytes = connected_socket.recv(__BUF_SIZE__)  # 从客户端接收输入
                received_str = received_bytes.decode()  # 将接受的字节转为字符串
                encoded_bytes = received_str.upper().encode()  # 准备发回到客户端的字节
                connected_socket.send(encoded_bytes)  # 发回到客户端
            self.connected_sockets.pop(peer_address, None)  # 将地址和套接字从字典中移除
            print('connection to %s is closed!', peer_address)  # 打印客户端关闭连接的信息


if __name__ == '__main__':
    TCPServer().start_server(__SERVER_PORT__, __SERVER_CAPACITY__)
