from stats import get_num_words, get_char_counts

#get the contents of a book using its relative file path
def get_book_text(file_path):

    file_contents = ""

    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def main():
    DIRECTORY_PATH= "./books/"
    book_title = "frankenstein"

    book_path = f"{DIRECTORY_PATH}{book_title}.txt"

    book_text = get_book_text(book_path)
    print(f"{get_num_words(book_text)} words found in the document")
    print(f"{get_char_counts(book_text)}")

main()
