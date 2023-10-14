from enum import Enum, unique


@unique
class Source(Enum):
    ORIGIN = 0  # origin text
    SAMPLE = 1  # sample text


# the state origin text towards sample text
@unique
class State(Enum):
    MISS = 0
    MATCH = 1
    REDUNDANT = 2
    DIFF = 3


class Word(object):
    source = None  # Source Enum Class
    state = None  # State Enum Class
    index = None  # index at related sentence, start from 0
    content = None

    # Constructor
    def __init__(self, source, state, index, content):
        self.source = source
        self.state = state
        self.index = index
        self.content = content

    # To String
    def __str__(self):
        return f"{self.index} {self.content} \t\t {self.state}"
