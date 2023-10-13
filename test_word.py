from unittest import TestCase
from word import *


class TestWord(TestCase):
    def test_str(self):
        word = Word(Source.ORIGIN, State.MISS, 0, "hello")
        print(word)