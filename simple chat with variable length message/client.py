from socket import *

try:
    s = socket(AF_INET, SOCK_STREAM)
    host = "127.0.0.1"
    port = 7002
    s.connect((host, port))

    while True:
        # Input message
        msg = input("Client: ")

        # Send the length of the message
        s.send(len(msg).to_bytes(4, byteorder='big'))

        # Send the message
        s.send(msg.encode('utf-8'))

        # Receive response length
        len_response = s.recv(4)
        response_len = int.from_bytes(len_response, byteorder='big')

        # Receive response
        response = s.recv(response_len).decode('utf-8')
        print("Server:", response)

    s.close()
except error as e:
    print(e)
except KeyboardInterrupt:
    print("Chat is terminated")

