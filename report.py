from stats import *

#print report on text data
def print_report(path, book_text, want_verbose_report=False, want_truncated_counts=False, max_char_counts=1000):
    #get individual words from text
    individual_words = get_words(book_text)
    num_words = len(individual_words)

    #get character and line conts
    char_counts = sort_char_counts(get_char_counts(book_text, want_verbose_report))
    total_lines = 0

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(" ----------- Word Count ----------")
    print(f"Found {num_words} total words.")
    print(f"Text averages {get_avg_word_length(individual_words)} chars per word.")

    print("--------- Character Counts -------")
    print(f"Found {get_total_char_count(char_counts)} total characters.")
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
        if want_truncated_counts and printed_counts > max_char_counts:
            break
        print(f"\t{count['char']}: {count['num']}")
        printed_counts += 1

    print("--------- Line Count -------")
    print(f"Found {total_lines} total lines.")

    return

