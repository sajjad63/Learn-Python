import re

txt = "Wish you were here"
result = re.search("^Wish.*here$", txt)
print(result)
print(re.Match)

# txt = "The rain in Spain falls mainly in the plain!"
#
# #Check if the string contains "ai" followed by 0 or more "x" characters:
#
# b = re.findall("aix*", txt)
#
# print(b)
#
# if b:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")