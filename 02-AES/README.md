# AES Mode Experiment (ECB vs CBC) — School Project

This folder contains a small **school project experiment** showing the practical difference between **AES-256-ECB** and **AES-256-CBC** when encrypting a **BMP image**.

The goal is to visually compare the output images:
- **ECB** tends to preserve visible patterns (not secure for images/data with structure).
- **CBC** hides patterns much better by using an **IV** and chaining between blocks.

## Requirements
- **Python 3.x**
- **OpenSSL installed on your device**
  - `openssl` must be available in your terminal (in PATH).
  - Test:
    ```sh
    openssl version
    ```

## Folder Structure
- [AES-256-ECB/](AES-256-ECB/)
  - [`AES-256-ECB.py`](AES-256-ECB/AES-256-ECB.py): encrypts the BMP pixel data using **AES-256-ECB**
  - `penguin.bmp`: input image
  - `aes.key`: 32-byte AES key
  - Outputs: `pixels_ecb.bin`, `image_ecb.bmp`
- [AES-256-CBC/](AES-256-CBC/)
  - [`AES-256-CBC.py`](AES-256-CBC/AES-256-CBC.py): encrypts the BMP pixel data using **AES-256-CBC**
  - `penguin.bmp`: input image
  - `aes.key`: 32-byte AES key
  - `iv.bin`: 16-byte IV (generated each run)
  - Outputs: `pixels_cbc.bin`, `image_cbc.bmp`

## How it works (what the scripts do)
Both scripts:
1. Read the BMP file and detect where pixel data starts (BMP header size / pixel offset).
2. Split the image into:
   - **Header** (kept unchanged so the result stays a valid BMP)
   - **Pixel bytes** (encrypted)
3. Encrypt only the pixel bytes using OpenSSL (`openssl enc ...`).
4. Rebuild a new BMP by writing: `header + encrypted_pixels`.

### ECB mode (AES-256-ECB)
Implemented in [`AES-256-ECB.py`](AES-256-ECB/AES-256-ECB.py).
- Encrypts each block independently.
- Repeated pixel patterns → repeated ciphertext blocks → visible patterns remain.

### CBC mode (AES-256-CBC)
Implemented in [`AES-256-CBC.py`](AES-256-CBC/AES-256-CBC.py).
- Uses an **IV** and chaining.
- Same plaintext blocks encrypt differently depending on previous blocks → patterns are mostly hidden.

## Run instructions

### 1) ECB
```sh
cd "02-AES/AES-256-ECB"
python AES-256-ECB.py
```
Output image: `image_ecb.bmp`

### 2) CBC
```sh
cd "02-AES/AES-256-CBC"
python AES-256-CBC.py
```
Output image: `image_cbc.bmp`

## Result:

### 1) ECB:
The outline of the penguin is still visible.

![Using AES-256-ECB ](AES-256-ECB/image_ecb.bmp)

### 2) CBC:
The image appears as random noise.

![Using AES-256-CBC ](AES-256-CBC/image_cbc.bmp)

## Notes / Limitations
- This is an **educational school project**, not production-ready encryption code.
- The scripts use `-nopad` and encrypt raw pixel bytes. This works here because BMP pixel data size is typically block-aligned in these examples; otherwise OpenSSL may error or you’d need padding.
- ECB is shown only to demonstrate why it is generally not recommended for structured data like images.

## License
This project is released under the MIT License.