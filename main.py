def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    book_words_count = count_book_words(book_text)
    book_characters_counter = count_characters(book_text)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def count_book_words(book_text):
    words = book_text.split()
    return len(words)

def count_characters(book_text):
    counter = {}
    book_text = book_text.lower()
    for char in book_text:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    return counter

def sort_on(dict):
    key = list(dict.keys())[0]
    return dict[key]

main()
