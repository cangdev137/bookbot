#count the number of words in a string of book text
def get_num_words(book_text):
    word_count = len(book_text.split())
    return word_count

#get character counts for each character in the text
def get_char_counts(book_text):
    #convert to lower case
    book_text = book_text.lower()

    #store char:count pairs
    counts = {}
    for char in book_text:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] = counts[char]+1

    return counts
