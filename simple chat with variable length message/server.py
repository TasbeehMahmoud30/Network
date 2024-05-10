from socket import *

try: 
    s = socket(AF_INET, SOCK_STREAM)
    host = "127.0.0.1"
    port = 7002
    s.bind((host,port))
    s.listen(5)
    client, addr = s.accept()
    print("Connection from", addr[0])

    while True:
        # Receive the length of the message
        len_msg = client.recv(4)
        if not len_msg:
            break
        msg_len = int.from_bytes(len_msg, byteorder='big')
        
        # Receive the message
        msg = client.recv(msg_len).decode('utf-8')
        print("Client:", msg)
        
        # Send response
        response = input("Server: ")
        client.send(len(response).to_bytes(4, byteorder='big') + response.encode('utf-8'))

    client.close()
except error as e:
    print(e)
except KeyboardInterrupt:
    print("Chat is terminated") 
    s.close()
