from stats import *

#print report on text data
def print_report(path, book_text, want_verbose_report=False, want_truncated_counts=False, max_char_counts=1000):
    #get individual words from text
    book_words = get_words(book_text)
    #get stats about the words in the book
    num_words = len(book_words)
    (average_word_length, shortest_word, longest_word) = get_word_length_stats(book_words)
    #get stats about the characters in the book
    char_counts = sort_char_counts(get_char_counts(book_text, want_verbose_report))
    total_char_count = get_total_char_count(char_counts)
    total_lines = 0

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(" ----------- Word Count ----------")
    print(f"Found {num_words} total words.")
    print(f"Text averages {average_word_length} chars per word.")
    print(f"Shortest word is {len(shortest_word)} chars long. ({shortest_word})")
    print(f"Longest word is {len(longest_word)} chars long. ({longest_word})")
    print("--------- Character Counts -------")
    print(f"Found {total_char_count} total characters.")

    print("Individual character counts", end="")
    if want_truncated_counts:
        print(f" (truncated to top {max_char_counts} chars)", end="")
    print(" are:")
    printed_counts = 1 
    for count in char_counts:
        #don't display newline count. this will be used later
        if count['char'] == "newline":
            total_lines = count['num']
            continue
        #exit early if count should be truncated
        if not want_truncated_counts or printed_counts <= max_char_counts:
            percentage_of_total_chars = (count['num'] / total_char_count * 100)
            print(f"\t{count['char']}: {count['num']} ({percentage_of_total_chars:.2f}%)")
        printed_counts += 1

    print("--------- Line Count -------")
    print(f"Found {total_lines} total lines.")

    return

