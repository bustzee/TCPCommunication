import json    
    
class Message:
    #this class handles what kind of message we want

    def __init__(self, message_type, sender, receiver, content):
        self.message_type = message_type #(message type 0 = sending username (happens when we first connect) 1 = sending actual message)
        self.sender = sender
        self.receiver = receiver
        self.content = content


    def to_dict(self):
        return {
            "type": self.message_type,
            "sender": self.sender,
            "receiver": self.receiver,
            "content": self.content
        }

    def return_json(self):
        json_string = json.dumps(self.to_dict())
        return json_string
    
