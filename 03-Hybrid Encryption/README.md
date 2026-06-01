# Hybrid Encryption (School Project)

This repository contains a simple **client/server hybrid encryption demo** built for a **school project**.  
It uses:

- **RSA** (to encrypt / protect the AES session key)
- **AES-256-ECB** (to encrypt the message)
- **OpenSSL** (invoked from Python via `subprocess`)

## Requirements
- **Python 3.x**
- **OpenSSL installed on your device**
  - Make sure `openssl` is available in your terminal (in PATH).
  - Test with:
    - Windows / macOS / Linux: `openssl version`

## Project Files

- `server.py` — server: generates AES key, encrypts message, encrypts AES key with client public key, sends both
- `client.py` — client: generates RSA key pair, sends public key, receives encrypted message + key, decrypts both

## How it works 
1. Client generates RSA private/public key pair.
2. Client sends `public_key.pem` to server.
3. Server generates a random 32-byte AES key (`aes.key`).
4. Server encrypts:
   - the AES key using the client public key → `aes_enc.key`
   - the message using AES-256-ECB → `message_enc_aes.bin`
5. Server sends `message_enc_aes.bin` and `aes_enc.key` to the client.
6. Client decrypts `aes_enc.key` using `private_key.pem`, then decrypts the message.

## Run instructions
Open two terminals in the project folder.

### 1) Start the server
```sh
python server.py
```
Type a message when prompted.

### 2) Run the client
```sh
python client.py
```

The decrypted message will be printed by the client.

## Output / Generated files
Running the scripts creates files like:
- `private_key.pem`, `public_key.pem`
- `aes.key`, `aes_enc.key`
- `message.txt`, `message_enc_aes.bin`, `message_dec.txt`

## Notes / Limitations
- This is a **school project** example.
- Uses **AES-256-ECB**, which is not recommended for real-world secure messaging.
- Network reads use fixed `recv(1024)` which may truncate data for larger payloads.
- Intended for local testing (`localhost`).

## License
This project is released under the MIT License.