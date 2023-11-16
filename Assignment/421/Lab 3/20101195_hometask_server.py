import socket

HEADER = 64
FORMAT = 'utf-8'

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050 # Do not use well known. Can cause error

disconnect_msg = "End"
ADDR = (SERVER, PORT)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)
print("---Server is starting---")

# Listening stage
server.listen()
print("Listening on:", SERVER)



# Accepting stage
while True: # For multiple client to be accepted
    conn, addr = server.accept()
    print("Connected to:", addr) # Socket address
    
    connected = True # Meaning server is connected to a client 
    while connected: # Client will be connected till disconnect message
        # Buffer size should be exactly message length (optimized)
        msg_length = conn.recv(HEADER).decode(FORMAT) # Header is a dummy value i.e. message length should not be greater than 64 byte
        # Check if any length (otherwise would have given error if empty)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT) # Actual message
            
            if msg == disconnect_msg:
                connected = False # Terminating the connection with 
                conn.send(f"Terminating {addr}".encode(FORMAT))
            else: # Important - Client has ip / device information
                print("Entered hours:", msg)
                hour = int(msg)
                salary = 0

                if hour <= 40:
                  salary += hour*200
                else:
                  salary += 8000+300*(hour-40)
                conn.send(f"Salary will be: {salary}".encode(FORMAT))

                # print(msg)
                # conn.send("Received".encode(FORMAT))
    conn.close() # Will close if any other client not there
                
