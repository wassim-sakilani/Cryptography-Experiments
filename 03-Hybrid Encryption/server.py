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


message = str(input("Please write you msg here : "))

with open("message.txt", "w", encoding="utf-8") as f:
    f.write(str(message))

# create AES key 
subprocess.run([
    "openssl",
    "rand",
    "-out",
    "aes.key",
    "32"
], check=True)

## convert AES key to hexadecimal

with open("aes.key", "rb") as f:
    key_hex = f.read().hex()


## get the client public key
public_key = client.recv(1024 )

with open("public_key.pem", "wb") as f:
    f.write(public_key)

## encrypte the AES key with the public key (RSA)

subprocess.run([
    "openssl",
    "pkeyutl",
    "-encrypt",
    "-pubin",
    "-inkey", "public_key.pem",
    "-in", "aes.key",
    "-out", "aes_enc.key"
], check=True)

## encrypte the message with AEC key using AES-256-ECB
subprocess.run([
    "openssl",
    "enc",
    "-aes-256-ecb",
    "-K", key_hex,
    "-in", "message.txt",
    "-out", "message_enc_aes.bin"
], check=True)


## send the ecrypted message
with open("message_enc_aes.bin", "rb") as f:
    client.send(f.read())

## send the encrypted AES key

with open("aes_enc.key", "rb") as f:
    client.send(f.read())

client.close()
server.close()






