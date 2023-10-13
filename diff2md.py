import difflib
from utils import *

origin_txt = "This is a sample sentence."
corrective_text = "This is another example sentence."

differ = difflib.Differ()
diff_list = list(differ.compare(corrective_text.split(), origin_txt.split()))
print(diff_list)  # ['  This', '  is', '- another', '+ a', '- example', '? ^^\n', '+ sample', '? ^\n', '  sentence.']

print("------------------------")

origin_words, corrective_words = postprocess_diff_list(diff_list)
for one in origin_words:
    print(one)

print("------------------------")

for one in corrective_words:
    print(one)