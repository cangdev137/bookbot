import re

#return the individual words of the book text
def get_words(book_text):
    return re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", book_text.lower())

#return average word length, longest and shortest word lengths
def get_word_length_stats(book_words):
    longest_word = ""
    shortest_word = book_words[0] if len(book_words) > 0 else ""
    sum_lengths = 0
    num_words = 0
    for current_word in book_words:
        next_length = len(current_word)
        #ignore punctuation characters
        if next_length == 1 and (not current_word.isalnum() or current_word == " "):
            continue
        if next_length > len(longest_word):
            longest_word = current_word
        if next_length < len(shortest_word):
            shortest_word = current_word

        #contribute to average
        sum_lengths += next_length
        num_words += 1
    return (sum_lengths/num_words), shortest_word, longest_word

#get character counts for each character in the text
def get_char_counts(book_words, verbose=False):
    book_words = book_words.lower()

    counts = {}
    for char in book_words:
        if char == ' ':
            if 'spaces' not in counts:
                counts['spaces'] = 1
            else:
                counts['spaces'] += 1
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

#generate individual dictionaries for each word count and put into a list
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

#return total character counts
def get_total_char_count(sorted_char_counts):
    total = 0
    for count in sorted_char_counts:
        total += count["num"]
    return total


