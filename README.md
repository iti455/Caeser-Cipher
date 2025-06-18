# Caeser-Cipher

🏛️ Task 01 – Caesar Cipher Encryptor & Decryptor

🧩 Objective
Build a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. The user provides:
-A message to encrypt or decrypt
-A shift value (number of positions each letter will be shifted)

🔐 What Is Caesar Cipher?
The Caesar Cipher is a simple substitution cipher where each letter in the plaintext is shifted a fixed number of places down the alphabet. For example, with a shift of 3:
mathematica
A → D, B → E, C → F, ...

📁 Project Structure
![image](https://github.com/user-attachments/assets/f58cbf3a-f11e-4295-a8c4-0d0428334208)

🛠️ Features
-Accepts any message (letters + symbols).
-Allows the user to choose the shift value.
-Encrypts and decrypts using the same logic.
-Handles both uppercase and lowercase characters.
-Leaves spaces and punctuation untouched.

▶️ How to Run
Run the script:
python caesar_cipher.py
Provide inputs:
🔤 Enter your message: Hello world
🔁 Enter shift value: 4

# Output:
![image](https://github.com/user-attachments/assets/1c1e42bd-898b-468c-a1f3-9d504f2b67de)


💡 Code Overview
def encrypt(text, shift):
    ...
def decrypt(text, shift):
    return encrypt(text, -shift)
Uses character shifting via ASCII values.

Encryption and decryption logic is efficiently shared.

⚠️ Note
This is a basic educational project using a classical cipher. It is not suitable for secure communication. For real-world encryption, use modern cryptography libraries.

