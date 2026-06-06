# Certificate Exchange Using Python Sockets and OpenSSL (School Project)

## Overview

This code demonstrates a simple client-server communication system in Python using TCP sockets. The client generates a self-signed X.509 certificate with OpenSSL and sends it to the server. The server receives the certificate and extracts information such as the certificate details and the public key.

## Requirements
- **Python 3.x**
- **OpenSSL installed on your device**
  - Make sure `openssl` is available in your terminal (in PATH).
  - Test with:
    - Windows / macOS / Linux: `openssl version`
	
## Project Files

- `client.py` — client: generates a self-signed certificate and sends it to the server.
- `server.py` — server: receives the certificate and extracts certificate information.

## Run instructions
Open two terminals in the project folder.

### 1) Start the server
```sh
python server.py
```
Type the certificate information.

### 2) Run the client
```sh
python client.py
```

## License
This project is released under the MIT License.