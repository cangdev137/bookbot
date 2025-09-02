#count the number of words in a string of book text
def get_num_words(book_text):
    word_count = len(book_text.split())
    return word_count

#get character counts for each character in the text
def get_char_counts(book_text, verbose=False):
    punctuation_marks = set(['.', '?', '!', ':', ';', '-', ',', '\'', '\"'])
    book_text = book_text.lower()

    counts = {}
    for char in book_text:
        if char == ' ':
            if 'space' not in counts:
                counts['space'] = 1
            else:
                counts['space'] += 1
        elif char == '\n':
            if 'newline' not in counts:
                counts['newline'] = 1
            else:
                counts['newline'] += 1
        elif not verbose and not char.isalpha():
            if 'punctuation' not in counts:
                counts['punctuation'] = 1
            else:
                counts['punctuation'] += 1
        elif char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    return counts

#generate individual dictionaries for each 
def generate_individual_char_counts(counts):
    individual_counts = []

    for c in counts:
        next_count = {}
        next_count["char"] = c
        next_count["num"] = counts[c]
        individual_counts.append(next_count)

    return individual_counts

#sort a single dictionary based on individual character counts
def sort_on_num_key(items):
    return items["num"]
def sort_char_counts(unsorted_counts):
    individual_counts = generate_individual_char_counts(unsorted_counts)
    individual_counts.sort(reverse=True, key=sort_on_num_key)

    return individual_counts

