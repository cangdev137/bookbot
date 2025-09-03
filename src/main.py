import sys
import os
from report import print_report

#get the contents of a book using its relative file path
def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_path= ""
    want_verbose_report = False
    want_truncated_counts = False
    max_char_counts = 1000

    #verify that user attached a book to analyze
    if len(sys.argv) < 2:
        print("Incorrect command usage. please include a path to your book.")
        print("Usage: ./bookbot.sh [flags] <path_to_book>")
        sys.exit(1)
    
    #check for any flags
    if len(sys.argv) > 2:
        #remove umbrella "punctuation" term from character counts
        if "-v" in sys.argv:
            want_verbose_report = True
        #truncate character counts
        if "-n" in sys.argv:
            want_truncated_counts = True
            #get number of counts to print from next argument
            max_char_counts = int(sys.argv[sys.argv.index("-n")+1])
    
    #check that file exists
    file_path= sys.argv[-1]
    if not os.path.isfile(file_path):
        print(f"'{file_path}' does not exist or is not a file.")
        print("Usage: ./bookbot.sh [flags] <path_to_book>")
        sys.exit(1)

    #extract the text from the file
    book_text = get_book_text(file_path)

    #print stats
    print_report(file_path, book_text, want_verbose_report, want_truncated_counts, max_char_counts)

main()
