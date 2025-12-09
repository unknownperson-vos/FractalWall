![FractalWall Demo](https://cdn.discordapp.com/attachments/1437646588859383889/1447986154430529697/orange_yellow_plain_background_4k_hd_orandwdage-3840x2160.jpg?ex=69399db1&is=69384c31&hm=3ff3daebe286d0e16972bc621b90a438d2a5376f3376f9ad48df866c01960cde)
![Python](https://img.shields.io/badge/python-3.9+-blue)
![OS](https://img.shields.io/badge/OS-Windows%2010%2F11-green)
![License](https://img.shields.io/badge/license-MIT-orange)

# ![icon](https://cdn.discordapp.com/attachments/1437646588859383889/1447988090982498504/logo-removebg-preview_15_1.png?ex=69399f7f&is=69384dff&hm=c745ac30d446a0f1062045cd8d2e33bbcc858e2fc04008898b63073f7d98c801) FractalWall Obfuscator

Semi-Advanced Multi-Layer Python Obfuscator (GUI)

FractalWall Obfuscator is a multi-stage, GUI-based Python obfuscation tool designed to make reverse-engineering extremely difficult.
It combines multiple layers of protection, including marshal, base64, zlib, PyArmor, pickle, UTF-16 transformations, randomized symbol mutation, encrypted split payloads, and false code injection.

This tool is built for users who want to protect their Python source code from tampering, analysis, and decompilation.

---

# ✨ Features

## 🧱 Four-Layer Obfuscation System

FractalWall includes a fully stacked obfuscation pipeline:

### 1️⃣ First Wall -> Split Payload Encryption

- Compresses + marshals the code

- Encodes it using a custom base16 obfuscation map

- Splits the encrypted payload into two separate files under /cache

- Reconstructs and runs through a self-decoding loader

### 2️⃣ Second Wall -> PyArmor Protection

- Automatically runs pyarmor gen on the generated script

- Adds an additional runtime VM-based obfuscation layer

### 3️⃣ Third Wall -> Binary Confusion Layer

- ROT13 + HEX + zlib + pickle + marshal

- Heavy variable mutation (random 30–120 character names)

- UTF-16 encoded payloads

- Dynamic replacement chain using randomly chosen replacement operations

- Encoded exec(), compile(), base64, marshal, pickle, zlib loaders

- Fake null lines + junk variable injections

### 4️⃣ Fourth Wall -> Final Compression Barrier

- Entire file reprocessed into a deeper marshal → zlib → pickle → base16 → mapped-character blob

- Randomized entry loader

- Further confusion of the final code execution

---

# 📦 Requirements

To automatically install the correct modules with pinned versions:
```pip install -r requirements.txt```

---

# 📁 Output Structure
```
<filename>-Obfuscated/
│
├── <filename>.py          <- Fully obfuscated file
└── cache/
    ├── os.py              <- part 1 of encrypted payload
    └── sys.py             <- part 2 of encrypted payload
```

---

# ⭐ Support

If you like FractalWall, consider starring the project on GitHub, it helps a lot!

---

