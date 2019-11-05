from socket import *
import time


class Server:
    def __init__(self, game_port):
        self.conn = None
        self.conn_ip = None
        self.sock = socket()  # По умолчанию это TCP
        self.sock.bind(('0.0.0.0', game_port))

    def wait_conn(self):
        valid = False  # Ну, поключения нет, значит оно не валидно
        while not valid:
            self.sock.listen(1)
            self.conn, (self.conn_ip, port) = self.sock.accept()
            self.conn.settimeout(5)  # Не будем долго ждать
            try:
                ans = self.conn.recv(22)
                valid = ans == b'I am the Qtsb client!\n'  # А это точно Qtsb? Вдруг это случайность?
            except timeout:
                pass
        self.send('I am the Qtsb server!\n')
        print(f'Опа, подключение: {self.conn_ip}')
        self.conn.settimeout(None)
        print(self.read())

    def send(self, data):
        self.conn.send(str(data).encode())

    def read(self):
        return self.conn.recv(1024).decode()

    def close(self):  # Не знаю, почему, но если это запихать в __del__, то оно не работает
        self.sock.close()
        self.conn.close()


server = Server(1777)
server.wait_conn()
server.close()
