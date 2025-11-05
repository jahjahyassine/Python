import string

def frequency(words):
    frequency_dict = {}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1
    return frequency_dict

def length_moy(words):
    length_total = [len(word) for word in words if word != ""]
    return sum(length_total) / len(length_total)

def max_word(words):
    word_most_used_value = max(words.values())
    word_most_used = [word for word, its_value in words.items() if its_value == word_most_used_value]
    return word_most_used

def min_word(words):
    word_less_used_value = min(words.values())
    word_less_used = [word for word, its_value in words.items() if its_value == word_less_used_value]
    return word_less_used

def palindrome(words):
    palindrome_words = [word for word in words if word == word[::-1]]
    return palindrome_words if palindrome_words else "None"


def num_phrases(lines):
    return len(lines)

def length_phrase(lines):
    phrases_dict = {}
    for line in lines:
        phrases_dict[line] = len(line)
    return phrases_dict

def type_punctuations(txt):
    list_punctuations = set([p for p in txt if p in string.punctuation])
    return list_punctuations


def report(words, phrases):
    words_top_10 = sorted(words.items(), key = lambda x:x[1], reverse = True)
    phrases_most_long = sorted(phrases.items(), key = lambda x:x[1], reverse = True)
    return words_top_10[:10], phrases_most_long
