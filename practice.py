numbers = [23,6,34,56,6,3,97]
vertices = [(2,2),(3,6),(4,9)]

def det_min(list):
    min_num = min(list)
    print(min_num)

det_min(numbers)

def det_max():
    max_num = max(numbers)
    print(max_num)

det_max()

def det_ymax():
    ymax = max(vertices,key=lambda v : v[1])[1]
    print(ymax)
    ymin = min(vertices,key=lambda v : v[1])[1]
    print(ymin)

det_ymax()
