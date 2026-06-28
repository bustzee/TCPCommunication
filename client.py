import socket
import message
import threading
import json
import sys
class Client:
    def __init__(self):
        self.conn = None
        self.addr = None
        self.username = ""
        self.client = None

    def start(self):
        self.create_connection()
        threading.Thread(target=self.receiving_loop).start()
        self.message_loop()
        
        
        #i know this is weird but maybe there are other functions i want to run in start so that's why im including create_connection in start() instead of directly calling it
        
    def disconnect_client(self):
        print("DISCONNECTED")
        self.send_msg(2, self.username, "", "")
        sys.exit()
        #self.client.close()

    def receiving_loop(self):
        #print("STARTED THREAD")
        while True:
            data = self.client.recv(1024)
            if not data:
                
                #self.disconnect_client()
                break

            

            msg = data.decode()
            json_data = json.loads(msg)
            print(f"\n{json_data['sender']} : {json_data['content']}")
            #print("New message:", msg)

    def create_connection(self):
        txt = input("What's your username? ")
        self.username = txt
        self.client = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        self.client.connect(("127.0.0.1", 5000))
        print("Connected")
        self.send_msg(0, "", "", self.username)
        

    def message_loop(self):
        while True:
            receiver = input("Who do you want to send message to? ")
            if receiver.lower()=="exit":
                self.disconnect_client()
                break
            msg = input("Message: ")
            if msg.lower()=="exit":
                self.disconnect_client()
                break
            self.send_msg(
                message_type=1,
                sender=self.username,
                receiver=receiver,
                content=msg

            )


    
    def send_msg(self, message_type, sender, receiver, content):
        ms = message.Message(message_type, sender, receiver, content)
        #print(ms)
        self.client.send(ms.return_json().encode())





        