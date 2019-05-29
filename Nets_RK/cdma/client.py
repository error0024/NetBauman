import socket
import numpy as np


def encode(vec, seq):
    enc = 2*seq - 1
    xor = [x * vec for x in enc]
    return np.concatenate(xor).ravel()


if __name__ == '__main__':
    channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    channel.connect(('127.0.0.1', 12345))

    first_vec = np.array([1, -1])
    first_seq = np.random.randint(0, 2, 4)
    first_enc = encode(first_vec, first_seq)

    second_vec = np.array([1, 1])
    second_seq = np.random.randint(0, 2, 4)
    second_enc = encode(second_vec, second_seq)

    on_air = first_enc + second_enc
    channel.send(on_air.tobytes())

    print('Original data:', first_seq, second_seq)
    print('Encoded data: ', first_enc, second_enc)
    print('On air:       ', on_air)
    channel.close()


