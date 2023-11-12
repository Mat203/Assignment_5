import matplotlib.pyplot as plt
from collections import Counter
from task_5 import caesar_decrypt

reference_freq = {
    'a': 8.04, 'b': 1.54, 'c': 2.73, 'd': 4.14, 'e': 12.60, 'f': 2.03, 'g': 1.92, 'h': 6.11,
    'i': 6.71, 'j': 0.23, 'k': 0.87, 'l': 4.24, 'm': 2.53, 'n': 6.80, 'o': 7.70, 'p': 1.66,
    'q': 0.09, 'r': 5.68, 's': 6.11, 't': 9.37, 'u': 2.85, 'v': 1.06, 'w': 2.34, 'x': 0.20,
    'y': 2.04, 'z': 0.06
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
