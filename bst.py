def intcmp(x, y):
    if x < y:
        return -1
    if x > y:
        return 1
    return 0


class Node:
    def __init__(self, element, cmp=intcmp):
        self.left = None
        self.right = None
        self.data = element
        self.cmp = cmp


def insert(tree, element):
    temp = Node(element)

    if tree.cmp(element, tree.data) < 0:
        if tree.left is None:
            tree.left = temp
        else:
            insert(tree.left, element)
    if tree.cmp(element, tree.data) > 0:
        if tree.right is None:
            tree.right = temp
        else:
            insert(tree.right, element)
        

def search(tree, element):
    if not tree:
        return False
    if not tree.cmp(element, tree.data):
        return True
    if tree.cmp(element, tree.data) < 0:
        return search(tree.left, element)
    return search(tree.right, element)


l = [3, 2, 5, 1, 7, 8, 11]
root = Node(4)
for i in l:
    insert(root, i)
    
print(search(root, 7))
print(search(root, 22))
        