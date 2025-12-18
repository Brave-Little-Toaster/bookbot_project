from stats import word_count, number_of_characters

path = "books/frankenstein.txt"


def get_book_text(path):
    with open(path) as f:
        printed_book = f.read()
    return printed_book


def main():
    printed_book = get_book_text(path)
    total_words = word_count(printed_book)
    count = number_of_characters(printed_book)
    print(number_of_characters(printed_book))


main()
