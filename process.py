import difflib

from config import *
from ignorerules import *
from utils import *
import re


def preprocess(diff_list):
    diff_list = [one for one in diff_list if not one.startswith('?')]

    # only ignore punctuation
    if IGNORE_PUNCTUATION and not IGNORE_CASE:  # ignore punctuation? ignore , . " ' - ?
        diff_list = ignore_process(diff_list, is_ignore_punctuation)

    # only ignore case
    if IGNORE_CASE and not IGNORE_PUNCTUATION:  # ignore case?
        diff_list = ignore_process(diff_list, is_ignore_case)

    # all ignore
    if IGNORE_CASE and IGNORE_PUNCTUATION:
        diff_list = ignore_process(diff_list, is_all_ignore)

    return diff_list


def ignore_process(diff_list, ignore_rule):
    for i in range(len(diff_list)):
        if diff_list[i].startswith('-') \
                and i + 1 < len(diff_list) \
                and diff_list[i + 1].startswith('+') \
                and ignore_rule(diff_list[i + 1][2:], diff_list[i][2:]):
            # ignore, replace unmatched pair(like '- the', '+ The') to match content(like ' The')
            content = str(diff_list[i])[2:]  # use sample content as standard content
            match_prefix = "  "
            diff_list[i: i + 2] = [match_prefix + content, '?']  # '?' just a placeholder, keep list.len not change

    diff_list = [one for one in diff_list if not one.startswith('?')]
    return diff_list


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

    diff_list = preprocess(diff_list)
    corrected_words = correct(diff_list)  # correct
    corrected_line = gen_corrected_line(corrected_words)  # join
    corrected_line = postprocess(corrected_line)

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


# Use win+v to paste to siyuan
def gen_corrected_line(corrected_words):
    return " ".join(word.content for word in corrected_words).replace("~~ ~~", " ").replace("== ==", " ")


def postprocess(corrected_line):
    modified_line = re.sub(r'(?<!\\)\$', r'\\\\$', corrected_line)
    return modified_line
