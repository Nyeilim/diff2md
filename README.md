# diff2md
Find the differences between two texts and output the corrected text with Markdown

The code is used for correcting my dictation of English listening materials. So there's some special feature between the sample text and dictation(origin) text.
1. Two texts will have the same number of lines.
2. The text maybe lacks a lot. Forgive my poor English~ 😂
3. The text usually contains multiple lines and split with '\n\n'.

And the program will do some preprocessing to the text for ignoring some unimportant mistake.
1. Ignore case. That means 'The' and 'the' will be recognized the same text.
2. Ignore punctuation. That means 'day.' and 'day' will be recognized the same text.