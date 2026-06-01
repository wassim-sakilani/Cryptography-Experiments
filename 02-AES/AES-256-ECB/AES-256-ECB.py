import subprocess;

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

## open the Image , it must be .bmp
with open("penguin.bmp", "rb") as f:
    data = f.read()


pixel_offset = int.from_bytes(data[10:14], byteorder="little")
print("Pixel data starts at:", pixel_offset)


header = data[:pixel_offset]
pixels = data[pixel_offset:]

## separate the header from the pixels 
#header = data[:54]
#pixels = data[54:]

with open("pixels.bin", "wb") as f:
    f.write(pixels)


## encypte the pixels 

subprocess.run([
    "openssl",
    "enc",
    "-aes-256-ecb",
    "-K", key_hex,
    "-nosalt",
    "-nopad",
    "-in", "pixels.bin",
    "-out", "pixels_ecb.bin"
], check=True)

## rebuild the Image

with open("pixels_ecb.bin", "rb") as f:
    encrypted_pixels = f.read()

with open("image_ecb.bmp", "wb") as f:
    f.write(header)
    f.write(encrypted_pixels)


#print(len(pixels))
#print(len(encrypted_pixels))