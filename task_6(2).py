import matplotlib.pyplot as plt
from collections import Counter
from task_5 import caesar_decrypt

reference_freq = {
    'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702,
    'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153,
    'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507,
    'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056,
    'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974, 'z': 0.074
}

def read_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read().replace('\n', '')
    return text

def calculate_frequencies(text):
    text = text.replace(' ', '') 
    letter_freq = Counter(text)
    total_letters = sum(letter_freq.values())
    
    freq_dict = {}
    for letter, count in letter_freq.items():
        freq = (count / total_letters) * 100
        freq_dict[letter] = freq
    
    return freq_dict


def calculate_difference(freq1, freq2):
    total_difference = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    for letter in alphabet:
        freq1_value = freq1.get(letter, 0)
        freq2_value = freq2.get(letter, 0)
        
        difference = abs(freq1_value - freq2_value)
        total_difference += difference
    
    average_difference = total_difference / len(alphabet)
    
    return average_difference


def main():
    text = read_file('123456.txt')
    differences = []
    for shift in range(26):
        decrypted_text = caesar_decrypt(text, shift)
        decrypted_freq = calculate_frequencies(decrypted_text)
        difference = calculate_difference(decrypted_freq, reference_freq)
        differences.append((shift, difference))
    differences.sort(key=lambda x: x[1])
    print('Top 3 most suitable keys:', differences[:3])

if __name__ == "__main__":
    main()
