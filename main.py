def caesar_encrypt(text, shift):
    shift = shift % 128
    encrypted_text = []
    for char in text:
        ascii_value = ord(char)  
        shifted_value = ascii_value + shift
        encrypted_char = chr(shifted_value)  
        encrypted_text.append(encrypted_char)
    return ''.join(encrypted_text)

def caesar_decrypt(text, shift):
    shift = shift % 128
    decrypted_text = []
    for char in text:
        ascii_value = ord(char) 
        shifted_value = ascii_value- shift 
        decrypted_char = chr(shifted_value) 
        decrypted_text.append(decrypted_char)
    return ''.join(decrypted_text)


def main():
    text = input("Enter the text: ")
    shift = int(input("Enter the shift "))
    encrypted_text = caesar_encrypt(text, shift)
    print(f"Encrypted text: {encrypted_text}")
    decrypted_text = caesar_decrypt(encrypted_text, shift)
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
