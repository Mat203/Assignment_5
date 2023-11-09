import random

def caesar_encrypt(text, shift):
    shift = shift % 95  
    encrypted_text = []
    for char in text:
        if 32 <= ord(char) <= 126: 
            ascii_value = ord(char) - 32  
            shifted_value = (ascii_value + shift) % 95  
            encrypted_char = chr(shifted_value + 32) 
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
    return ''.join(decrypted_text)

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


def apply_caesar_operation(operation_function, shift):
    file_path = input("Enter the file name to read: ")
    text = read_file(file_path)

    result_text = operation_function(text, shift)
    output_file_path = input("Enter the file name to write: ")

    write_file(output_file_path, result_text)
    print("Operation is completed")

def main():
    operation = input("Enter 'e' for encrypt or 'd' for decrypt: ")
    shift = random.randint(1, 20)
    
    if operation.lower() == 'e':
        apply_caesar_operation(caesar_encrypt, shift)
    elif operation.lower() == 'd':
        apply_caesar_operation(caesar_decrypt, shift)
    else:
        print("Unknown operation")

if __name__ == "__main__":
    main()
