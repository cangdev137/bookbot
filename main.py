import sys
from stats import get_num_words, get_char_counts, sort_char_counts

#get the contents of a book using its relative file path
def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

#print report on text data
def print_report(relative_path, word_count, char_counts):
    individual_counts = sort_char_counts(char_counts) 

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {relative_path}...")
    print(" ----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for count in individual_counts:
        print(f"{count['char']}: {count['num']}")

    return

def main():
    DIRECTORY_PATH= "books/"
    book_title = "frankenstein"
    book_path = f"{DIRECTORY_PATH}{book_title}.txt"

    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_counts = get_char_counts(book_text)

    print_report(book_path, num_words, char_counts)

main()
