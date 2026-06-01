# Diffie-Hellman Key Exchange (Socket Simulation)

This project is a simple **client/server simulation** of the **Diffie–Hellman key exchange** using Python sockets on `localhost`.  
The server and client exchange public values and independently compute the same **shared secret**.

## Features
- Generation of private keys using cryptographically secure randomness.
- Computation of public keys.
- Exchange of public values between two participants.
- Generation and verification of the shared secret.
- Educational implementation with clear and readable code.

## Files

- [server.py](server.py): waits for a client connection, asks user for `(p, g)`, computes server public value, and derives the shared secret.
- [client.py](client.py): connects to the server, receives `(p, g)`, computes client public value, and derives the shared secret.

## How it works (high level)

1. **Server** asks for:
   - `p`: a large prime number
   - `g`: a generator (`g < p`)
2. Server sends `g` and `p` to the client.
3. Both sides generate private secrets:
   - Server secret: `a`
   - Client secret: `b`
4. Public values are computed:
   - Server: `A = g^a mod p`
   - Client: `B = g^b mod p`
5. They exchange `A` and `B` via the socket.
6. Both compute the shared key:
   - Server: `k = B^a mod p`
   - Client: `k = A^b mod p`
7. Both should display the same `k`.

## Requirements

- Python 3.x
- No external dependencies (uses built-in modules like `socket` and `secrets`)

## Run instructions (VS Code / Terminal)

Open **two terminals**:

### Terminal 1 (Server)
```sh
python server.py
```

Enter values when prompted, for example:
- `p`: `23`
- `g`: `5`

### Terminal 2 (Client)
```sh
python client.py
```

## Expected output

- Server prints its private key `a` and the computed shared number `k`
- Client prints its private key `b` and the computed shared number `k`

Both sides should output the **same shared number**.

## Notes / Limitations

- This is a **learning/demo** implementation, not production-ready cryptography.
- The server checks that `p` is prime using a simple trial division method (fine for small demo primes, slow for large primes).
- The code prints private secrets (`a` and `b`) for demonstration—**do not do this in real applications**.
- Communication is unencrypted and unauthenticated (susceptible to MITM in real networks).

## License

This project is released under the MIT License.