from random import random

from django import template

register = template.Library()  # если мы не зарегистрируем наши фильтры, то Django никогда не узнает, где именно их искать, и фильтры потеряются

chars = ["*", "#", "%", "&", "?", "@"]

not_alphabet = [' ', ',', '.']


@register.filter(name='censor')
def censor(value):
    bw = ["черт", "дурак"]
    check_list = value.split()
    for i in range(len(check_list)):
        for ban in bw:
            post_word = check_list[i]
            pos = post_word.lower().find(ban)
            if pos != -1:
                post_word = post_word[:pos] + "*" * len(ban) + post_word[pos + len(ban):]
            check_list[i] = post_word

    res = " ".join(check_list)
    return res