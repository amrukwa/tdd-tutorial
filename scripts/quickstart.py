import numpy as np


def foo(x):
    return x + 1


def find_letters(word, letter):
    if not isinstance(word, str):
        raise ValueError("word must be a string")
    if not isinstance(letter, str):
        raise ValueError("letter must be a string")
    return [i for i, l in enumerate(word) if l == letter]


def get_pi():
    return 22 / 7


def choose_by_random(word, seed=None):
    rng = np.random.default_rng(seed)
    return rng.choice(list(word))
