from stats import word_count, number_of_characters, chars_dict_to_sorted_list
import sys


print("Usage: python3 main.py <path_to_book>")

args = sys.argv
path = args[1]


def get_book_text(path):
    with open(path) as f:
        printed_book = f.read()
    return printed_book


def main():
    printed_book = get_book_text(path)
    total_words = word_count(printed_book)
    count = number_of_characters(printed_book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    sorted_chars = chars_dict_to_sorted_list(count)
    for entry in sorted_chars:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")


main()
