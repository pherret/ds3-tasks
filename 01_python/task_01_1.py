# coding: utf-8
"""
Посчитайте распределение тематик новостей в файле URL.txt
(то есть какое количество раз встречается страница с каждой темой).
Тематикой можно считать первое слово между знаками '/' в URL новости.
"""

from re import compile

theme_regex = compile(r"^\/(?P<theme>[^?][^\/]+)")

themes = {}

with open('URLs.txt') as f:
    for line in f:
        url = line.strip()
        matches = theme_regex.match(url)
        if matches:
            theme = matches.group('theme')
            themes.setdefault(theme, 0)
            themes[theme] += 1

print(themes)
