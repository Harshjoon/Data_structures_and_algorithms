# given that collection is sorted
def binary_search(collection, target):
    first = 0
    last  = len(collection) - 1

    while( first <= last ):
        mid = (first + last)//2
        if collection[mid] == target: return mid
        elif collection[mid] < target:
            last = mid - 1
        elif collection[mid] > target:
            first = mid + 1
    
    return None

search_names = [] # define some serach names
collection = [] # define some collection

for n in search_names:
    index = binary_search(collection,n)
    print(index)