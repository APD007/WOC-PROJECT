import socket
import threading


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(5)

clients = []
nicknames = []
print("SERVER LISTENING...")
def broadcast(message, client_sender):
    for client in clients:
        if client != client_sender:
            try:
                client.send(message)
            except:
                
                index = clients.index(client)
                nickname = nicknames[index]
                nicknames.remove(nickname)
                clients.remove(client)
                client.close()
                broadcast(f"{nickname} left the chat!".encode('utf-8'), None)
                break

def handle(client_socket, username):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break

            
            message = data.decode('utf-8')
            broadcast(f"FROM : {message}".encode('utf-8'), client_socket)
        except:
            
            index = clients.index(client_socket)
            nickname = nicknames[index]
            nicknames.remove(nickname)
            clients.remove(client_socket)
            client_socket.close()
            broadcast(f"{nickname} left the chat!".encode('utf-8'), None)
            break

def receive():
    while True:
        client,address =server.accept()
        nickname=(client.recv(1024)).decode("utf-8")
        print(client,"Connected")
        client.send(("Connected Users List "+str(nicknames)).encode('utf-8'))
        for client1 in clients:
            client1.send((nickname+" Connected").encode("utf-8"))
        clients.append(client)
        nicknames.append(nickname)
        thread=threading.Thread(target=handle, args=(client,nickname))
        thread.start()


receive()
