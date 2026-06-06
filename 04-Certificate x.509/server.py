import socket
import subprocess;


host = "localhost"
port = 12800

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print("Server listening...")
client, infos_connexion = server.accept()
print(f"Connection from {infos_connexion}")


## get the client public key
certificate = b""

while True:
    chunk = client.recv(4096)
    if not chunk:  # client closed connection
        break
    certificate += chunk

print("Received", len(certificate), "bytes")

#print(certificate.decode(errors="ignore")[:200])

with open("certificate.txt", "wb") as f:
    f.write(certificate)

result = subprocess.run([
    'openssl',
    'x509',
    '-text',
    '-noout',
    '-in', "certificate.txt",
    "-out","certificate_cleare.txt"
    ],check=True)


with open("certificate_cleare.txt", "r") as f:
    result = f.read()

print("certificate contente: ",result)

# extract the public key 

subprocess.run(
    [
        "openssl",
        "x509",
        "-in", "certificate.txt",
        "-pubkey",
        "-noout",
        "-out", "public_key.txt"
    ],
    check=True
)

# read the public key

with open("public_key.txt", "r") as f:
    public_key = f.read()

# print the public key 

print("The public Key :",public_key)

client.close()
server.close()






