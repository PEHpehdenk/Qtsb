from socket import *
import time


class Client:
    def __init__(self):
        self.conn = socket()  # По умолчанию это TCP

    def connect(self, ip: str, port: int):
        self.conn.connect((ip, port))
        self.send('I am the Qtsb client!\n')
        if self.read() == 'I am the Qtsb server!\n':
            self.send('Привет!')
            print('Юхху! Мы подключились!')

    def send(self, data):
        self.conn.send(str(data).encode())

    def read(self):
        return self.conn.recv(1024).decode()

    def close(self):  # Не знаю, почему, но если это запихать в __del__, то оно не работает
        self.sock.close()
        self.conn.close()


client = Client()
client.connect('127.0.0.1', 1777)
