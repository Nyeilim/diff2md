from entity.word import *
from config import *
import difflib


def preprocess(text):
    if IGNORE_PUNCTUATION:
        text = str(text).replace('"', '').replace(',', '').replace('.', '')  # ignore punctuation?
    if IGNORE_CASE:
        text = text.lower()  # ignore case?

    clean_text = text
    return clean_text


def process(origin_text, sample_text):
    origin_lines = origin_text.split('\n\n')
    sample_lines = sample_text.split('\n\n')
    if len(origin_lines) != len(sample_lines):
        return "Error: lines unmatched!"

    corrected_lines = list()
    for i in range(len(origin_lines)):
        corrected_line = do_process(origin_lines[i], sample_lines[i])
        corrected_lines.append(corrected_line)

    return "\n\n".join(corrected_lines)


def do_process(origin_line, sample_line):
    # diff
    differ = difflib.Differ()
    diff_list = list(differ.compare(sample_line.split(), origin_line.split()))

    # TODO: preprocess
    corrected_words = correct(diff_list)  # correct
    corrected_line = gen_corrected_line(corrected_words)  # join

    return corrected_line


def correct(diff_list):
    index = 0
    words = list()

    for one in diff_list:
        content = str(one)[2:]
        if str(one).startswith(' '):
            words.append(Word(Source.ORIGIN, State.MATCH, index, content))
            index += 1
        elif str(one).startswith('+'):
            words.append(Word(Source.ORIGIN, State.REDUNDANT, index, md_strikethrough(content)))
            index += 1
        elif str(one).startswith('-'):
            words.append(Word(Source.SAMPLE, State.MISS, index, md_highlight(content)))
            index += 1
        else:
            pass

    sort_corrected_words(words)
    corrected_words = words
    return corrected_words


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

            # try find consecutive REDUNDANT and MISS area
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


# Use win+v to paste to siyuan
def gen_corrected_line(corrected_words):
    return " ".join(word.content for word in corrected_words).replace("~~ ~~", " ").replace("== ==", " ")


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


# Markdown highlight: ==test==
def md_highlight(content):
    return f"=={content}=="


# Markdown strikethrough: ~~test~~
def md_strikethrough(content):
    return f"~~{content}~~"
