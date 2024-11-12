import re

str = "HaHaHaHaHa"
# wrdRegex = re.compile(r'(Ha){3,5}?') #non-greedy match
wrdRegex = re.compile(r'(Ha){3,5}') #greedy match
match = wrdRegex.search(str)
print(f'Word found: {match.group()}')
