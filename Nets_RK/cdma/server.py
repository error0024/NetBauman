import socket
import numpy as np


def decode(vec, seq):
    xor = seq.reshape((-2, 2)) * vec
    sum = np.sum(xor, 1)
    return np.clip(sum, 0, 1)


if __name__ == '__main__':
    channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    channel.bind(('0.0.0.0', 12345))
    channel.listen(1)
    conn, addr = channel.accept()

    data = conn.recv(128)
    on_air = np.frombuffer(data, np.dtype('int'))

    first_vec = np.array([1, -1])
    first_dec = decode(first_vec, on_air)

    second_vec = np.array([1, 1])
    second_dec = decode(second_vec, on_air)

    print('On air:      ', on_air)
    print('Decoded data:', first_dec, second_dec)
    channel.close()
