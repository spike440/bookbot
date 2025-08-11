def count_words():
    text = get_book_text("./books/frankenstein.txt")
    words = text.split()
    return len(words)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def character_count():
    answer = {}
    text = get_book_text("./books/frankenstein.txt").lower()
    for char in text:
        if char in answer:
            answer[char] += 1
        else:
            answer[char] = 1
    return answer

print(character_count())
