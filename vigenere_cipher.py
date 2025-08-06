while True:
    mode = input("Type 'e' to encrypt or 'd' to decrypt: ").strip().lower()
    if mode in ('e', 'd'):
        break
    print("Invalid input. Enter 'e' or 'd'.")
if mode == 'e':
    text = input("Enter plaintext to encrypt: ")
else:  
    text = input("Enter ciphertext to decrypt: ")
while True:  
    raw_key = input("Anahtarı gir (sadece harfler kullanılacak): ") 
    custom_key = ''
    for c in raw_key:  
        if c.isalpha():  
            custom_key += c.lower()

    if len(custom_key) > 0:  
        break  
    else:
        print("Lütfen en az bir harf içeren geçerli bir anahtar gir.")
def vigenere(message,key,direction=1):
    key=key.lower()
    alphabet="abcdefghijklmnopqrstuvwxyz"
    key_index=0
    final_message=""
    for char in message.lower():
        if not char.isalpha():
            final_message+=char
        else:
            key_char=key[key_index%len(key)]
            key_index+=1
            offset=alphabet.index(key_char)
            index=alphabet.index(char)
            new_index=(index+offset*direction)%len(alphabet)
            final_message+=alphabet[new_index]
    return final_message
def encrypt(message,key):
    return vigenere(message,key,1)
def decrypt(message,key):
    return vigenere(message,key,-1)
if mode=='e':
    encrypted_text = encrypt(text, custom_key)
    print(f"\nPlaintext: {text}")
    print(f"Key: {custom_key}")
    print(f"Encrypted text: {encrypted_text}")
else:
    decryption=decrypt(text,custom_key)
    print(f"\nEncrypted text: {text}")
    print(f"Key: {custom_key}")
    print(f"\nDecrypted text: {decryption}")

