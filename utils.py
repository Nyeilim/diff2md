from entity.word import *
from config import *
import difflib


def preprocess_text(text):
    if IGNORE_PUNCTUATION:
        text = str(text).replace('"', '').replace(',', '').replace('.', '')  # ignore punctuation?
    if IGNORE_CASE:
        text = text.lower()  # ignore case?

    clean_text = text
    return clean_text


def do_process(origin_line, sample_line):
    # diff
    differ = difflib.Differ()
    diff_list = list(differ.compare(preprocess_text(sample_line).split(), preprocess_text(origin_line).split()))

    corrected_words = correct(diff_list)  # correct
    corrected_text = gen_corrected_text(corrected_words)  # join

    return corrected_text



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
            exchange_word(words, i, i - 1)

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
def gen_corrected_text(corrected_words):
    return " ".join(word.content for word in corrected_words).replace("~~ ~~", " ").replace("== ==", " ")


# Warning: be sure the index i1/i2 are valid
def exchange_word(words, i1, i2):
    # content change
    tmp = words[i1]
    words[i1] = words[i2]
    words[i2] = tmp
    # index update
    words[i1].index = i1
    words[i2].index = i2


# Markdown highlight: ==test==
def md_highlight(content):
    return f"=={content}=="


# Markdown strikethrough: ~~test~~
def md_strikethrough(content):
    return f"~~{content}~~"
