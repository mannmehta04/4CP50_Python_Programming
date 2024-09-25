def count_file_stats(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)
        return num_lines, num_words, num_chars

def main():
    file_name = input("Enter the file name: ")
    stats = count_file_stats(file_name)
    if stats:
        num_lines, num_words, num_chars = stats
        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
        print(f"Number of characters: {num_chars}")

if __name__ == "__main__":
    main()