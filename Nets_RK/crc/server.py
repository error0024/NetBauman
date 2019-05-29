import socket
from PyCRC.CRC16 import CRC16

crc16 = CRC16()

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
        print("Получены данные", data)
        if not data:
            break
        data_checkword = data[len(data) - 16:].decode()
        calculated_checkword = bin(crc16.calculate(data[:len(data) - 16]))[2:]
        if data_checkword == calculated_checkword:
            print("Ошибок не найдено, слово получено верно.")
            answer = "Получено сообщение " + data[:-16].decode() + " без ошибок."
            connection.sendall(answer.encode())
        else:
            answer = "Слово передано с ошибкой."
            print(answer)
            connection.sendall(answer.encode())
        connection.close()
