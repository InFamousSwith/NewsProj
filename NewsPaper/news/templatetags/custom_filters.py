from random import random

from django import template

register = template.Library()  # если мы не зарегистрируем наши фильтры, то Django никогда не узнает, где именно их искать, и фильтры потеряются

chars = ["*", "#", "%", "&", "?", "@"]
bw = ["черт", "дурак"]
not_alphabet = [' ', ',', '.']


@register.filter(name='censor')
def censor(value):
    word = ''
    for i in range(len(value)):
        if value[i] != not_alphabet:
            word += value[i]
        elif word in bw:
            word = random.sample(chars, len(word))

    return random.sample(chars, len(word))

    forbidden_list = ["военн", "жир", "просто", "даже", "клуб", "операц", "евро"]

    check_list = value.split()
    for i in range(len(check_list)):
        for forb_word in forbidden_list:
            post_word = check_list[i]
            pos = post_word.lower().find(forb_word)
            if pos != -1:
                post_word = post_word[:pos] + "*" * len(forb_word) + post_word[pos + len(forb_word):]
            check_list[i] = post_word

    res = " ".join(check_list)
    return res