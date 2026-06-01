import socket
import random;
import secrets


host = "localhost"
port = 12800

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print("Server listening...")
client, infos_connexion = server.accept()
print(f"Connection from {infos_connexion}")
client_file = client.makefile('rw')

p =int(input("enter p un grand nombre premier: "))
val=True
if p<2:
    val=False
else:
    for i in range(2, int(p**0.5) + 1):
        if p % i == 0:
            val = False
            break
if val==False :
    raise ValueError("p is not a prime number")

g=int(input("entrer the generator g : "))
if g >= p:
    raise ValueError("g must be inferior to p")

# send g and p to the client
client_file.write(str(g) + '\n')
client_file.write(str(p) + '\n')
client_file.flush()


## calculate our private number
a = secrets.randbelow(p - 2) + 2
## We can use "a = random.randint(2,p-2)" but "random" is not intended for cryptographic purposes.And "secrets" library was specifically designed for encryption.
A = pow(g, a, p)

# Receive the Client Result first
B = int(client_file.readline())

# Then send our result to the client
client_file.write(str(A) + '\n')
client_file.flush()

## Calculate the shared number 
k = pow(B, a, p)

print(f"your secret key is :{a} , keep it safe ")
print("shared number: ",k)

client_file.close()
client.close()
server.close()






