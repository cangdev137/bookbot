import sys
import os
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
    #verify that user attached a book to analyze
    if len(sys.argv) != 2:
        print("Incorrect command usage. please include a path to your book.")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    #check that file exists
    if not os.path.isfile(book_path):
        print(f"'{book_path}' does not exist or is not a file.")
        sys.exit(1)

    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_counts = get_char_counts(book_text)

    print_report(book_path, num_words, char_counts)

main()
