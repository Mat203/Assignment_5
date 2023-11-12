import random

def caesar_encrypt(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = []
    
    for char in text:
        if char in alphabet: 
            ascii_value = ord(char) - ord('a')  
            shifted_value = (ascii_value + shift) % len(alphabet)  
            encrypted_char = chr(shifted_value + ord('a')) 
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    
    return ''.join(encrypted_text)



def caesar_decrypt(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted_text = []
    
    for char in text:
        if char in alphabet: 
            ascii_value = ord(char) - ord('a')  
            shifted_value = (ascii_value - shift) % len(alphabet)  
            decrypted_char = chr(shifted_value + ord('a')) 
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


def apply_caesar_operation(operation_function, shift):
    file_path = input("Enter the file name to read: ")
    text = read_file(file_path)

    result_text = operation_function(text, shift)
    output_file_path = input("Enter the file name to write: ")

    write_file(output_file_path, result_text)
    print("Operation is completed")

def main():
    operation = input("Enter 'e' for encrypt or 'd' for decrypt: ")
    shift = random.randint(1, 25)
    
    if operation.lower() == 'e':
        apply_caesar_operation(caesar_encrypt, shift)
    elif operation.lower() == 'd':
        apply_caesar_operation(caesar_decrypt, shift)
    else:
        print("Unknown operation")

if __name__ == "__main__":
    main()
