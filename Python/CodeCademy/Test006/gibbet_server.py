# coding: utf-8

import socketserver
import random

class MyTCPHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        self.data = self.request.recv(1024).decode()
        print('Клиент {} сообщает {}'.format(self.client_address[0], self.data))
        
        if self.data == 'START':
            x = random.randint(1, 100)
            self.request.sendall(bytes('GUESS;1;100', 'utf-8'))
            try_count = 10      # счетчик попыток
            while True:
                self.data = self.request.recv(1024).decode()
                resp = self.data.split(';')
                print(resp)
                if resp[0] == 'TRY':
                    if int(resp[1]) == x:
                        self.request.sendall(bytes('TRUE', 'utf-8'))
                        print('Клиент {} выиграл'.format(self.client_address[0]))
                    else:
                        try_count -= 1
                        if try_count == 0:
                            self.request.sendall(bytes('FAIL', 'utf-8'))
                            print('Клиент {} проиграл'.format(self.client_address[0]))
                            break
                        else:
                            if x < int(resp[1]):
                                self.request.sendall(bytes('FALSE;{};<'.format(try_count), 'utf-8'))
                            else:    
                                self.request.sendall(bytes('FALSE;{};>'.format(try_count), 'utf-8'))
                elif resp[0] == 'GOODBYE':    
                    self.request.sendall(bytes('GOODBYE', 'utf-8'))
                    print('Клиент {} отключился'.format(self.client_address[0]))
                    break
                else:
                    print('Неизвестный запрос')
                    break
        
    #  START - GUESS;1;100
    #  TRY;x - TRUE
    #        - FALSE;y;<
    #        - FALSE;y;>   
    #        - FAIL
    #  GOODBYE - GOODBYE
    #      

if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 7777
    
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    print('Сервер игры "Виселица" запущен')
    
    server.serve_forever()
    