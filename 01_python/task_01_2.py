# coding: utf-8
"""
Какое количество различных слов русского языка можно составить из букв слова «Ростелеком»?
Примеры: кот, стекло, лето.
Используйте любой словарь русского языка.
"""

from collections import Counter


def generate_matcher(source_word):
    source_chars_count = Counter(source_word.lower())

    def matcher(str):
        chars_count = Counter(str)
        for x in chars_count:
            if source_chars_count[x] < chars_count[x]:
                return False
        return True

    return matcher


matcher = generate_matcher('Ростелеком')

with open('dict.txt') as f:
    words = []
    for line in f:
        word = line.strip()
        if matcher(word):
            words.append(word)

print(len(words))
