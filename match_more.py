import  re

search_str = "The strongest Batman i know."
wrdRegex = re.compile(r'Bat(wo)*man')
match = wrdRegex.search(search_str)
print(f'Word found: {match.group()}')
