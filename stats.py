def word_count(printed_book):
    words = printed_book.split()
    count = len(words)
    return count


def number_of_characters(printed_book):
    char_counts = {}
    letters = printed_book.lower()
    for letter in letters:
        if letter not in char_counts:
            char_counts[letter] = 0
        char_counts[letter] += 1
    return char_counts


def chars_dict_to_sorted_list(char_counts):
    sorted_chars = []
    for char, count in char_counts.items():
        combo = {"char": char, "num": count}
        sorted_chars.append(combo)
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars


def sort_on(item):
    return item["num"]
