
def merge_sort(list):
    """
    Sort list in asending order
    return a new sorted list

    Divide: Find the midpoint of the list
    Conquer: Recursively sort the sublist created in previous step
    Combine: Merge sorted sublist created in previous step
    """

    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)


def split(list):
    """
    Divide the unsorted list at midpoint into sublist
    """
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left,right

def merge(left, right):
    """
    Merge two lists, sorting them in the process.
    returns a new merged list
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if ( left[i] < right[j] ):
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1


    while i < len(left):
        l.append(left[i])
        i+=1

    while j < len(right):
        l.append(right[j])
        j+=1
    
    return l