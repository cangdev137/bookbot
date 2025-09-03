import sys
import os
from stats import *

#get the contents of a book using its relative file path
def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

#print report on text data
def print_report(path, word_count, char_counts):
    total_lines = 0

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(" ----------- Word Count ----------")
    print(f"Found {word_count} total words.")

    print("--------- Character Count -------")
    print(f"Found {get_total_char_count(char_counts)} total characters.")
    for count in char_counts:
        #don't display newline count. this will be used later
        if count['char'] == "newline":
            total_lines = count['num']
            continue
        print(f"{count['char']}: {count['num']}")

    print("--------- Line Count -------")
    print(f"Found {total_lines} total lines.")

    return

def main():
    book_path = ""
    want_verbose_count = False

    #verify that user attached a book to analyze
    if len(sys.argv) < 2:
        print("Incorrect command usage. please include a path to your book.")
        print("Usage: python3 main.py [flags] <path_to_book>")
        sys.exit(1)
    
    #check for any flags
    if len(sys.argv) > 2:
        if "-v" in sys.argv:
            want_verbose_count = True
        #other flags
        #TODO

    #check that file exists
    book_path = sys.argv[-1]
    if not os.path.isfile(book_path):
        print(f"'{book_path}' does not exist or is not a file.")
        print(f"Usage: python3 main.py [flags] <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_counts = sort_char_counts(get_char_counts(book_text, verbose=want_verbose_count))
    print_report(book_path, num_words, char_counts)

main()
