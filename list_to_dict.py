names = ["jeremy","isaac", "Matthew"]
ages = [25, 30, 20]

def makedict (keys, values):
    age_dict = dict(zip(keys, values))
    return (age_dict)

#Examine pop(k, deflt) vs popitem()
def pop(key):
    poped = rst_dict.pop(key, "Key not found!")
    print("\nPopped item: ", poped)

def popitem():
    poped = rst_dict.popitem()
    print("\nPopped item: ", poped)
    print(poped[0])

if __name__ == "__main__":
   rst_dict = makedict(names, ages)
   print( rst_dict)
   pop("isaac")
   print(rst_dict)
   popitem()
   print(rst_dict)



