def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
def get_num_words(file_path):
    num_words = 0
    book_text = get_book_text(file_path)
    separate_words = book_text.split()
    for num in separate_words:
        num_words += 1
    return num_words


def get_char_frequency(file_path):
    book_text = get_book_text(file_path)
    if not book_text:
        return {}
    lower_case = book_text.lower()  # Convert to lowercase
    char_freq = {}  # Initialize dictionary
    for char in lower_case:  # Use lower_case instead of book_text
        char_freq[char] = char_freq.get(char, 0) + 1
    return char_freq

def get_sorted_dictionaries(file_path):
#    dictionary = get_char_frequency()

    char_freq = get_char_frequency(file_path)
    return dict(sorted(char_freq.items(), key=lambda x: (-x[1], x[0])))