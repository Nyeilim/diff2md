import difflib
from utils import *

# example
# origin_txt = "This is a sample sentence."
# sample_text = "This is another example sentence."
origin_txt = "a woman was charged allegedly Role Island city law against feeding animals."
sample_text = "A woman was charged with allegedly violating a Rhode Island city law against feeding wild animals."

# diff
differ = difflib.Differ()
diff_list = list(differ.compare(sample_text.split(), origin_txt.split()))
print(diff_list)  # ['  This', '  is', '- another', '+ a', '- example', '? ^^\n', '+ sample', '? ^\n', '  sentence.']

# get metadata
origin_words, sample_words = postprocess_diff_list(diff_list)

# correct
corrected_words = correct(diff_list)

# join
corrected_text = gen_corrected_text(corrected_words)

# print and paste to siyuan!
print(corrected_text)
