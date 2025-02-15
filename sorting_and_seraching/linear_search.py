
def index_of_item(collection,target):
    for i in range(len(collection)):
        if collection[i] == target:
            return i
        
    return None

search_names = [] # write a bunch of names here
collection = [] # write a bunch of names here

for m in search_names:
    index = index_of_item(collection,m)
    print(index)

    