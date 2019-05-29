import socket
from hamming_code import *


if __name__ == '__main__':
    socket = socket.socket()
    print("Сокет создан.")
    port = 1234
    socket.bind(('127.0.0.1', port))
    socket.listen(5)
    print("Прослушивание канала на 127.0.0.1.")
    while True:
        connection, addr = socket.accept()
        print('Подключение с адреса', addr)
        data = connection.recv(1024)
        print("Получены данные", data.decode())
        if not data:
            break
        error = lookup_for_error(data)
        message = correct(data.decode(), error)
        answer = "Ошибка в разряде " + str(error) + ", информационное сообщение " + str(message) + "."
        print(answer)
        connection.sendall(answer.encode())
        connection.close()
