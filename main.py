path = "books/frankenstein.txt"


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main(get_book_text, filepath):
    printed_book = get_book_text(filepath)
    print(printed_book)
    return (printed_book)


main()
