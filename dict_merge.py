d1 = {"Name":"Mulwa", "age":26}
d2 = {"Name":"Mulwa", "city":"Machakos"}

#syntax1
merged1 = {**d1, **d2}
print(merged1)

#Syntax2
merged2 = d1 | d2
print(merged2)

#Syntax3
merged3 = d1.update(d2)
print(merged3)