from entity.word import *
import re


# Sort the list, make words which are the same state together, for example:
# ----------------------------------------------------------
# This is ==another== ~~a~~ ==example== ~~sample~~ sentence.
# This is ~~a~~ ~~sample~~ ==another== ==example== sentence.
def sort_corrected_words(words):
    # first, find whether has ==?== before ~~?~~, if has then exchange
    for i in range(1, len(words)):
        if (words[i - 1].state == State.MISS
                and words[i].state == State.REDUNDANT):
            red_start = red_end = i
            miss_end = miss_start = i - 1

            # try to find consecutive REDUNDANT and MISS area
            while red_end + 1 < len(words) \
                    and words[red_end + 1].state == State.REDUNDANT:
                red_end = red_end + 1
            while miss_start - 1 >= 0 \
                    and words[miss_start - 1].state == State.MISS:
                miss_start = miss_start - 1

            # exchange
            exchange_words(words, miss_start, miss_end, red_start, red_end)

    # second, make words which are the same state together
    # main focus "miss redundant miss" and "redundant miss redundant" two types
    for i in range(2, len(words)):
        # "miss redundant miss"
        if ((words[i].state == State.MISS
             and words[i - 1].state == State.REDUNDANT
             and words[i - 2].state == State.MISS)
                # "redundant miss redundant"
                or (words[i].state == State.REDUNDANT
                    and words[i - 1].state == State.MISS
                    and words[i - 2].state == State.REDUNDANT)):
            exchange_word(words, i, i - 1)


# Warning: be sure the index i1/i2 are valid and consecutive
def exchange_word(words, i1, i2):
    exchange_words(words, i1, i1, i2, i2)


# exchange the [start1, end1] and [start2, end2]
# index order: start1 < end1 < start2 < end2; and index are consecutive
def exchange_words(words, start1, end1, start2, end2):
    words[start2:end2 + 1], words[start1:end1 + 1] \
        = words[start1:end1 + 1], words[start2:end2 + 1]
    for i in range(start1, end2 + 1):
        words[i].index = i


# bug fix: add the procession towards $
# Markdown highlight: ==test==
def md_highlight(content):
    content = re.sub(r'\$', r'\\$', content)
    return f"=={content}=="


# Markdown strikethrough: ~~test~~
def md_strikethrough(content):
    content = re.sub(r'\$', r'\\$', content)
    return f"~~{content}~~"
