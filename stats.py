import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(document_path):
    text = get_book_text(document_path)
    words = text.split()
    return len(words)

def character_count(document_path):
    answer = {}
    text = get_book_text(document_path).lower()
    for char in text:
        if char in answer:
            answer[char] += 1
        else:
            answer[char] = 1
    return answer

def chars_dict_to_list(character_dict):
    sorted_list = []
    for ch in character_dict:
        sorted_list.append({"char":ch,"num": character_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def sort_on(d):
    return d["num"]

def print_report(document_path):
    test = character_count(document_path)
    sorted_list = (chars_dict_to_list(test))
    print("============ BOOKBOT ============")
    print("Analyzing book found at", document_path)
    print("----------- Word Count ----------")
    print("Found", count_words(document_path), "total words")
    print("--------- Character Count -------")
    for i in range(0,len(sorted_list)):
        # Only print alphabetic characters
        if sorted_list[i]["char"].isalpha() == True:
           print (f"{sorted_list[i]["char"]}: {sorted_list[i]["num"]}")
    print("============= END ===============")
