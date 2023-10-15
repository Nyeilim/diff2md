# just junk codes, maybe used later
from entity.word import *


# metadata
def parse_diff_list(diff_list):
    origin_index = 0
    sample_index = 0
    origin_words = list()
    sample_words = list()

    for one in diff_list:
        content = str(one)[2:]
        if str(one).startswith(' '):
            # match
            origin_words.append(Word(Source.ORIGIN, State.MATCH, origin_index, content))
            sample_words.append(Word(Source.SAMPLE, State.MATCH, sample_index, content))
            origin_index += 1
            sample_index += 1

        elif str(one).startswith('+'):
            # redundant
            origin_words.append(Word(Source.ORIGIN, State.REDUNDANT, origin_index, content))
            origin_index += 1

        elif str(one).startswith('-'):
            # miss
            sample_words.append(Word(Source.SAMPLE, State.MISS, sample_index, content))
            sample_index += 1
        else:
            # start with '?', diff, do nothing
            pass

    return origin_words, sample_words
