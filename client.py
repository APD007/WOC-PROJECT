import socket
import threading

print("HELLO RESPECTED CLIENT")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))
nickname=input("Enter Nickname ")
client.send(nickname.encode("utf-8"))
message=client.recv(1024)
print("Enter '/quit' to exit the chat")
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            print("An error occurred!")
            client.close()
            break

def write():
    while True:
        message = input('')
        if message.lower() == '/quit':
            client.send(f"{nickname} has left the chat.".encode('utf-8'))
            break
        else:
            client.send(f"{nickname}: {message}".encode('utf-8'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
