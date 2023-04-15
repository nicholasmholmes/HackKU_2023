import socket

def host_server():
    # create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get the local machine name
    host = socket.gethostname()

    # set a port number
    port = 12345

    # bind the socket to a public host and a port
    server_socket.bind((host, port))

    # listen for incoming connections
    server_socket.listen(1)

    # wait for a client to connect
    print('Waiting for a client to connect...')
    client_socket, addr = server_socket.accept()
    print('Got a connection from', addr)

    # send a message to the client
    message = 'Thank you for connecting'
    client_socket.send(message.encode('ascii'))

    # close the connection
    client_socket.close()
    server_socket.close()

def connect_to_server():
    # create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get the server's IP address and port number
    host = input('Enter the server IP address: ')
    port = int(input('Enter the port number: '))

    # connect to the server
    client_socket.connect((host, port))
    print('Connected to the server')

    # receive data from the server
    data = client_socket.recv(1024)
    print(data.decode('ascii'))

    # close the connection
    client_socket.close()

# ask the user whether to host or connect to a server
option = input('Do you want to host or connect to a server? (h/c): ')

# perform the selected action
if option == 'h':
    host_server()
elif option == 'c':
    connect_to_server()
else:
    print('Invalid option')
