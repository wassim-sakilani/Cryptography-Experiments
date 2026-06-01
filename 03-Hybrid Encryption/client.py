import socket
import subprocess;


host = "localhost"
port = 12800
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))


#generate private key
subprocess.run([
    "openssl",
    "genrsa",
    "-out",
    "private_key.pem",
    "1024"
], check=True)

## Extract the public key 
subprocess.run([
    "openssl",
    "rsa",
    "-in", "private_key.pem",
    "-pubout",
    "-out", "public_key.pem"
], check=True)


## send the public key to the server
with open("public_key.pem", "rb") as f:
    client.send(f.read())


## get the message 

message_enc_aes = client.recv(1024)

with open("message_enc_aes.bin", "wb") as f:
    f.write(message_enc_aes)

## get the encrypted AES key

aec_enc = client.recv(1024)

with open("aes_enc.key", "wb") as f:
    f.write(aec_enc)

## decrypt the AES key with our private key
subprocess.run([
    "openssl",
    "pkeyutl",
    "-decrypt",
    "-inkey", "private_key.pem",
    "-in", "aes_enc.key",
    "-out", "aes.key"
], check=True)

## decypte the message with the AES key

with open("aes.key", "rb") as f:
    key_hex = f.read().hex()

subprocess.run([
    "openssl",
    "enc",
    "-d",
    "-aes-256-ecb",
    "-K", key_hex,
    "-in", "message_enc_aes.bin",
    "-out", "message_dec.txt"
], check=True)


#get the message

with open("message_dec.txt", "r",encoding="utf-8") as f:
    message_dec = f.read()


#print the message

print("The message is:  ",message_dec)

client.close()
