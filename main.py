from stats import get_num_words, get_char_frequency, get_sorted_dictionaries
import sys

if len(sys.argv) != 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    file_path = sys.argv[1]

def main(file_path):

    # Report to print
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {get_num_words(file_path)} total words")
    print(f"--------- Character Count -------")
    sorted_dictionary = get_sorted_dictionaries(file_path)
    for char, freq in sorted_dictionary.items():
        if char.isalpha() == True:
            print(f"{char}: {freq}")
    print(f"============= END ===============")

main(file_path)