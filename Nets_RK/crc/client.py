import socket
from PyCRC import CRC16

crc16 = CRC16.CRC16()


if __name__ == '__main__':
    first = socket.socket()
    port = 1234
    first.connect(('127.0.0.1', port))
    input_string = input("Введите данные для отправки: ")
    data = (''.join(format(ord(x), 'b') for x in input_string))
    checkword = bin(crc16.calculate(data))[2:]
    codeword = data + checkword
    print("Отправка сообщения ", data, " с проверочными разрядами ", checkword, ".", sep="")
    first.sendall(codeword.encode())
    print(first.recv(1024).decode())

    second = socket.socket()
    second.connect(('127.0.0.1', port))
    input_string = input("Введите данные для отправки: ")
    checkword = bin(crc16.calculate(input_string))[2:]
    data = (''.join(format(ord(x), 'b') for x in input_string))
    data = list(data)
    data[-1] = '1' if data[-1] == '0' else '0'
    data = "".join(data)
    codeword = data + checkword
    print("Отправка сообщения c ошибкой в последнем разряде ", data, " с проверочными разрядами ", checkword, ".", sep="")
    second.sendall(codeword.encode())
    print(second.recv(1024).decode())
    second.close()
