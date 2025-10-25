def count_words(text):
    words = text.split()  # split string into a list of words
    return len(words)     # return how many items are in that list

def count_characters(text):
    text = text.lower()  # make everything lowercase
    chars = {}           # empty dictionary to store counts

    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars

def sort_on(item):
    return item["num"]

def sort_characters(char_dict):
    sorted_list = []

    for char, num in char_dict.items():
        if char.isalpha():  # only count letters (skip spaces, punctuation)
            sorted_list.append({"char": char, "num": num})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list