def binarysearch(list, x):
    """
    Searches a sorted list of numbers for item x.
    """
    if len(list) == 1:
        if list[0] == x:
            return True
        return False
    
    if x < list[len(list)//2]:
        return binarysearch(list[:len(list)//2], x)
    return binarysearch(list[len(list)//2:], x)
