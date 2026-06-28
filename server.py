import socket
import threading
import client
import json


class Server:
    def __init__(self):
        self.clients = {}
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("0.0.0.0", 5000))
        self.server.listen()

    def start(self):
        print("LISTENING ON PORT 5000")
        self.server_loop()

    


    def handle_client(self, conn, addr):

        print(f"New client from {addr}")
        
        

        while True:

            data = conn.recv(1024)

            if not data:
                break

            json_data = json.loads(data.decode())
            if json_data['type']==0:
                self.clients[json_data['content']] = conn
            elif json_data['type']==1:
                #handle real messages
                if json_data['sender'] in self.clients:
                    if json_data['receiver'] in self.clients:
                        #y = json.dumps(json_data).encode()
                        self.clients[json_data['receiver']].sendall(data)
            elif json_data['type']==2:
                if json_data['sender'] in self.clients:
                    self.clients[json_data['sender']].close()
                    self.clients.pop(json_data['sender'])
                    print("CLIENT DISCONNECTED")
                    break

            print(self.clients)

        
        
        #print("Client disconnected")
        #conn.close()
        #self.clients.remove(conn)
    

    def server_loop(self):
        while True:
            conn, addr = self.server.accept()
            threading.Thread(target=self.handle_client, args=(conn, addr)).start()
