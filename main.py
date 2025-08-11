def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words():
    text = get_book_text("./books/frankenstein.txt")
    words = text.split()
    return len(words)

def main():
    print(count_words(), "words found in the document")

main()
