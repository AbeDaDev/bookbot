import sys
from stats import count_words, count_characters, sort_characters


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    # Check if the user provided a path to the book
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # exit the program with error status

    path = sys.argv[1]  # second argument is the book path

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    text = get_book_text(path)

    # Word count
    num_words = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # Character count
    chars_dict = count_characters(text)
    sorted_chars = sort_characters(chars_dict)

    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


# Run the program
main()