# Cryptography Experiments

A collection of small, self-contained cryptography experiments for a university project. Each experiment is organized in its own folder with code and (when relevant) sample inputs/outputs.

## What you'll find here

- **Toy implementations** of cryptographic primitives and protocols for learning purposes.
- **Small demos** showing how common crypto building blocks work.
- **Notes and references** to help understand the concepts.

> ⚠️ **Educational use only:** The code in this repository is meant for learning and experimentation. Do **not** use these implementations in production.

---

## Repository structure

Each experiment should follow this structure:

```
<experiment-folder>/
  README.md           # short explanation of the experiment
  *.py                # implementation / demo scripts
  data/ (optional)    # sample inputs
  output/ (optional)  # sample outputs
```

If an experiment folder does not yet have its own `README.md`, please add one when you create the experiment.

---

## Experiments

| Folder | Description | How to run |
|--------|-------------|------------|
| `01-Diffie-Hellman/` | Diffie–Hellman key exchange simulated over a local Python socket client/server. Both sides compute the same shared secret. | `cd 01-Diffie-Hellman && python server.py` *(terminal 1)*, `python client.py` *(terminal 2)* |
| `02-AES/` | AES mode experiment on a BMP image: visual comparison of **AES-256-ECB** vs **AES-256-CBC** (ECB keeps patterns, CBC hides them). Uses OpenSSL via Python. | `cd 02-AES/AES-256-ECB && python AES-256-ECB.py` and `cd 02-AES/AES-256-CBC && python AES-256-CBC.py` |
| `03-Hybrid Encryption/` | Hybrid encryption demo: client/server where **RSA** protects an **AES** session key and AES encrypts the message (OpenSSL used from Python). | `cd "03-Hybrid Encryption" && python server.py` *(terminal 1)*, `python client.py` *(terminal 2)* |

For details, see the `README.md` inside each experiment folder.


## Requirements

- Python 3.x
- OpenSSL (required by experiments that invoke `openssl` from the terminal)

If you use additional dependencies later, list them here (or add a `requirements.txt`).

---

## How to run

From the repository root, run the commands shown in the table above (they differ by experiment).

---

## License

This project is released under the MIT License.
