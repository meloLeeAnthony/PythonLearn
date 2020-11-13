# 导入模块
from socket import socket, AF_INET, SOCK_DGRAM

# 创建UDP套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)
# 创建接收信息的地址
addr = ('10.20.17.235', 8080)
# 键盘接收发送的消息
data = input('请输入要发送信息：')
# 调用sendto方法发送信息
udp_socket.sendto(data.encode('gbk'), addr)
# 关闭套接字
udp_socket.close()
