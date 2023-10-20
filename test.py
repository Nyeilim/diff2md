# just a file for testing python feature, I'm not good at python
import difflib

my_list = [1, 2, 3, 4, 5, 6]
my_list[3:6], my_list[1:3] = my_list[1:3], my_list[3:6]
print(my_list)

# diff
sample_line = ""
origin_line = ""

differ = difflib.Differ()
diff_list = list(differ.compare(sample_line.split(), origin_line.split()))
