from word import *


def postprocess_diff_list(diff_list):
    origin_index = 0
    corrective_index = 0
    origin_words = list()
    corrective_words = list()

    for one in diff_list:
        content = str(one)[2:]
        if str(one).startswith(' '):
            # match
            origin_words.append(Word(Source.ORIGIN, State.MATCH, origin_index, content))
            corrective_words.append(Word(Source.CORRECTIVE, State.MATCH, corrective_index, content))
            origin_index += 1
            corrective_index += 1

        elif str(one).startswith('+'):
            # redundant
            origin_words.append(Word(Source.ORIGIN, State.REDUNDANT, origin_index, content))
            origin_index += 1

        elif str(one).startswith('-'):
            # miss
            corrective_words.append(Word(Source.CORRECTIVE, State.MISS, corrective_index, content))
            corrective_index += 1
        else:
            # start with '?', diff, do nothing
            pass

    return origin_words, corrective_words
