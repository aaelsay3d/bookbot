def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    book_words_count = count_book_words(book_text)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def count_book_words(book_text):
    words = book_text.split()
    return len(words)

main()
