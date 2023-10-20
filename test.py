# just a file for testing python feature, I'm not good at python
import difflib

my_list = [1, 2, 3, 4, 5, 6]
my_list[3:6], my_list[1:3] = my_list[1:3], my_list[3:6]
# print(my_list)

# diff
sample_line = "the 55-year-old woman's neighbor blame her for making the area red problem worse"
origin_line = "The 55-year-old woman's neighbors blame her for making the area's rat problem worse."

differ = difflib.Differ()
diff_list = list(differ.compare(sample_line.split(), origin_line.split()))
diff_list = [one for one in diff_list if not one.startswith('?')]

print(diff_list)

print("-------")

sample_line2 = "newly activate in the several days"
origin_line2 = "Newly installed cameras captured several rats active in the middle of the day."

differ2 = difflib.Differ()
diff_list2 = list(differ2.compare(sample_line2.split(), origin_line2.split()))
diff_list2 = [one for one in diff_list2 if not one.startswith('?')]

print(diff_list2)
