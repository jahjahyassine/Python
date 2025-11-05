import string
from functions import *


with open("definition_python.txt", "rt") as file:
    sentence = file.read()

sentence_origin = sentence
phrases = sentence

for p in string.punctuation:
    sentence = sentence.replace(p, " ")
sentence = [word.lower() for word in sentence.split() if word.strip() != ""]

sentence_ending = ".!?"
for se in sentence_ending:
    phrases = phrases.replace(se, "ا")
phrases = [phrase for phrase in phrases.split("ا") if phrase.strip() != ""]


dict_words = frequency(sentence)
dict_phrases = length_phrase(phrases)

print(f"Frequence des mots: {dict_words}")
print(f"Longueur moyenne est {length_moy(sentence):.2f}")

print(f"Les mots les plus utilisés sont: {max_word(dict_words)}")
print(f"Le mot le plus utilisé est: {max_word(dict_words)[0]}")

print(f"Les mots les moins utilisés sont: {min_word(dict_words)}")
print(f"Le mot le moins utilisé est: {min_word(dict_words)[0]}")

print(f"les mots palindromes du sentence: {palindrome(sentence)}")

print(f"Le nombre des phrases est {num_phrases(phrases)}")

print(f"Le longueur des phrases {length_phrase(phrases)}")

print(f"Les types de ponctuations utilises sont: {type_punctuations(sentence_origin)}")

words_top_10, phrases_most_long = report(dict_words, dict_phrases)
print(f"Top 10 des mots sont {words_top_10}")
print(f"Les phrases les plus longues sont {phrases_most_long}")
