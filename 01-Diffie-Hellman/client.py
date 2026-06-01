import socket
import random;
import secrets


host = "localhost"
port = 12800

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
client_file = client.makefile('rw')

# get  g and p from the server
g = int(client_file.readline())
p = int(client_file.readline())

## calculate our private number
b = secrets.randbelow(p - 2) + 2
## We can use "a = random.randint(2,p-2)" but "random" is not intended for cryptographic purposes.And "secrets" library was specifically designed for encryption.
B = pow(g, b, p);


# send B to the server
client_file.write(str(B) + '\n')
client_file.flush()

# Receive A from the server
A = int(client_file.readline())

# Calculate the shared number 
k = pow(A, b, p);

print(f"your secret key is :{b} , keep it safe ")
print("shared number: ",k)

client_file.close()
client.close()
