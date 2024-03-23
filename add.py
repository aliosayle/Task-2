import os

def read_words(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    return words

def write_words_to_files(words, num_files, words_per_file):
    # Create directories if they don't exist
    if not os.path.exists('output_files'):
        os.makedirs('output_files')
        
    for i in range(num_files):
        filename = f"output_files/{str(i+1).zfill(3)}.txt"
        with open(filename, 'w') as file:
            for _ in range(words_per_file):
                if words:
                    word = words.pop(0).strip()
                    file.write(word + '\n')
                else:
                    break

def main():
    words = read_words('words.txt')
    num_files = 200
    words_per_file = 100
    total_words_needed = num_files * words_per_file
    print(len(words))
    if len(words) < total_words_needed:
        print("Error: Not enough words in words.txt to fill 200 files with 100 words each.")
        return
    write_words_to_files(words, num_files, words_per_file)

if __name__ == "__main__":
    main()

