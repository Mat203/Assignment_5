import matplotlib.pyplot as plt
from collections import Counter
from task_5 import caesar_decrypt

def read_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read().replace('\n', '')
    return text

def calculate_frequencies(text):
    text = text.replace(' ', '') 
    return Counter(text)

def find_most_frequent_letter(letter_freq):
    return letter_freq.most_common(1)[0][0]

def calculate_shift(most_frequent_letter, most_frequent_english_symbol='e'):
    return ord(most_frequent_letter) - ord(most_frequent_english_symbol)

def plot_frequencies(letter_freq):
    letters = list(letter_freq.keys())
    freq = list(letter_freq.values())
    plt.figure(figsize=(10, 5))
    plt.bar(letters, freq)
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.title('Frequency of each letter')
    plt.show()

def main():
    text = read_file('123456.txt')
    letter_freq = calculate_frequencies(text)
    most_frequent_letter = find_most_frequent_letter(letter_freq)
    print(most_frequent_letter)
    shift = calculate_shift(most_frequent_letter)
    print(shift)
    decrypted_text = caesar_decrypt(text, shift)
    print(decrypted_text)
    plot_frequencies(letter_freq)

if __name__ == "__main__":
    main()
