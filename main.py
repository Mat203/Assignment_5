def caesar_encrypt(text, shift):
    shift = shift % 128
    encrypted_text = []
    for char in text:
        if char != '\n':
            ascii_value = ord(char)  
            shifted_value = ascii_value + shift
            encrypted_char = chr(shifted_value)  
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def caesar_decrypt(text, shift):
    shift = shift % 128
    decrypted_text = []
    for char in text:
        if char != '\n':
            ascii_value = ord(char) 
            shifted_value = ascii_value- shift 
            decrypted_char = chr(shifted_value) 
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def main():
    operation = input("Enter 'e' for encrypt or 'd' for decrypt: ")
    shift = int(input("Enter shift: "))
    if operation.lower() == 'e':
        file_path = input("Enter file name with text: ")
        text = read_file(file_path)
        encrypted_text = caesar_encrypt(text, shift)
        output_file_path = input("Enter file name for encrypted text: ")
        write_file(output_file_path, encrypted_text)
        print(f"Encrypted text is written in '{output_file_path}'")
    elif operation.lower() == 'd':
        file_path = input("Enter file name with enrypted text: ")
        encrypted_text = read_file(file_path)
        decrypted_text = caesar_decrypt(encrypted_text, shift)
        output_file_path = input("Enter file name for decrypted text:  ")
        write_file(output_file_path, decrypted_text)
        print(f"Decrypted text is written in '{output_file_path}'")
    else:
        print("Unknown operation")

if __name__ == "__main__":
    main()
