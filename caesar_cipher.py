def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# User input
message = input("🔤 Enter your message: ")
shift = int(input("🔁 Enter shift value: "))

encrypted = encrypt(message, shift)
decrypted = decrypt(encrypted, shift)

print("\n🔐 Encrypted Message: " + encrypted)
print("🔓 Decrypted Message: " + decrypted)
