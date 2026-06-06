import socket
import subprocess;


host = "localhost"
port = 12800
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))


# generate 

subprocess.run([
        "openssl", "req", "-x509", 
        "-newkey", "rsa:2048", 
        "-nodes", 
        "-keyout", "key_out.txt", 
        "-out", "certificate.txt", 
        "-days", "365",
    ], check=True)


## send the certificate to the server
with open("certificate.txt", "rb") as f:
    client.sendall(f.read())

print("Finish")
client.close()
