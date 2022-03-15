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
