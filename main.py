frankenstein_book = "books/frankenstein.txt"


def read_book(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents


def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    letter_count = {}
    for c in text:
        lowered = c.lower()
        if lowered in letter_count:
            letter_count[lowered] += 1
        else:
            letter_count[lowered] = 1
    return letter_count


def print_report(word_count, char_count):
    print(f"--- Begin report of {frankenstein_book} ---")
    print(f"{word_count} words found in the document")
    char_counts = list(char_count.items())
    char_counts.sort()
    for pair in char_counts:
        if pair[0].isalpha():
            print(f"The '{pair[0]}' character was found {pair[1]} times")


def main():
    text = read_book(frankenstein_book)
    word_count = count_words(text)
    letter_count = count_letters(text)
    print_report(word_count, letter_count)


main()
