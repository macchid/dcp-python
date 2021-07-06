
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_univals(node):
    if node.right is None and node.left is None:
        return node.val, True, 1

    l_val, l_is_unival, l_univals = count_univals(node.left)
    r_val, r_is_unival, r_univals = count_univals(node.right)

    return (
        node.val, 
        l_val == r_val and l_val == node.val and l_is_unival and r_is_unival, 
        l_univals + r_univals + (l_val == r_val and l_val == node.val and l_is_unival and r_is_unival)
    ) 


if __name__ == "__main__":
    root = Node(0, 
        Node(1), 
        Node(0, 
            Node(1, 
                Node(1, 
                    Node(1), Node(1)
                ), 
                Node(1, 
                    Node(0), Node(1)
                )
            ), 
            Node(0)
        )
    )

    _, _, univals = count_univals(root)
    print(f"univals = {univals}")

