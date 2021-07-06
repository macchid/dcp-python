# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
# For example, given the following Node class
# class Node:
#    def __init__(self, val, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right
#
# The following test should pass:
#
#node = Node('root', Node('left', Node('left.left')), Node('right'))
#assert deserialize(serialize(node)).left.left.val == 'left.left'
def serialize(root):
    if root is None:
        return ""

    serialized = f"{root.val} | {serialize(root.left)} | {serialize(root.right)}"


def deserialize(serialized):
    elements = serialized.split(' | ')
    return buildNodes(elements)


def buildNodes(elements):
    if len(elements) == 0:
        return None

    val = elements.pop(0)
    if val == "":
        return None

    root = Node(val)
    root.left = buildNodes(elements)
    root.right = buildNodes(elements)

    return root


class Node:
   def __init__(self, val, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

# The following test should pass:
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
