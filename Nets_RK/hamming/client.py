import socket
from hamming_code import *


if __name__ == '__main__':
    first = socket.socket()
    port = 1234
    first.connect(('127.0.0.1', port))
    input_string = gen_keyword()
    print("Информационный вектор:", input_string)
    data = encode(input_string)
    print("Кодовое слово:", data)
    print("Отправка сообщения ", data, ".", sep="")
    first.sendall(data.encode())
    print(first.recv(1024).decode())
    first.close()

    second = socket.socket()
    second.connect(('127.0.0.1', port))
    input_string = gen_keyword()
    print("Информационный вектор:", input_string)
    data = encode(input_string)
    print("Кодовое слово:", data)
    data = add_error(data)
    print("Кодовое слово с ошибкой:", data)
    print("Отправка сообщения ", data, ".", sep="")
    second.sendall(data.encode())
    print(second.recv(1024).decode())
    second.close()
