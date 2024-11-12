import re

def regex_findall():
    search_str = "Phone numbers are 0713-9168-94, 0723-9106-52"
    phoneRegex = re.compile(r'(\d{4})-(\d{4})-(\d{2})')
    match = phoneRegex.findall(search_str) # has no group()
    print(match[1][0])

regex_findall()

def regex_search():
    search_str = "Phone numbers are 0713-9168-94, 0723-9106-52"
    phoneRegex = re.compile(r'(\d{4})-(\d{4})-(\d{2})')
    match = phoneRegex.search(search_str)
    print(f"Phone num found: {match.group()}")
    
regex_search()
    


