# Vigenere Cipher (Interactive)

This Python program allows users to encrypt and decrypt messages using the **Vigenère Cipher** algorithm with interactive input.

## Features
- Choose operation mode: encryption or decryption
- Accepts plaintext or ciphertext input from the user
- Accepts only alphabetic characters as the key (auto-cleaning and converting to lowercase)
- Preserves spaces and punctuation
- Works with English alphabet (`a-z`)

## File 
- `vigenere_cipher.py` — Main program

## Usage

### 1. Run the script
````
python vigenere_cipher.py
````
### 2. Steps
1. Choose `e` to encrypt or `d` to decrypt.
2. Enter the plaintext or ciphertext.
3. Enter the key (letters only, case-insensitive).

### 3. Example

#### *-Encryption*
Type 'e' to encrypt or 'd' to decrypt: e  
Enter plaintext to encrypt: prince of darkness  
Enter the key (letters only): ripozzy

Plaintext: prince of darkness  
Key: ripozzy  
Encrypted text: tsgpmc pj btxgzhs  

#### *-Decryption*

Type 'e' to encrypt or 'd' to decrypt: d  
Enter ciphertext to decrypt: tsgpmc pj btxgzhs  
Enter the key (letters only): ripozzy  

Encrypted text: tsgpmc pj btxgzhs  
Key: ripozzy  
Decrypted text: prince of darkness  

## Note
Case sensitivity and additional alphabets can be added with further development.

<sub>kendime not: belki çok basit projelerle başlıyorum ama lisans hayatım boyunca yaptıklarımı burda biriktirmek istiyorum. vigenere şifrelemesini de kullanıcı girdili hale getirdim. eksik yerleri var ama şimdilik yeter. </sub>


