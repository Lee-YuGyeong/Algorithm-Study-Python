from logging import root


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def init_tree():
    global root

    new_node = Node("A")
    root = new_node

    new_node = Node("B")
    root.left = new_node
    new_node = Node("C")
    root.right = new_node

    new_node_1 = Node("D")
    new_node_2 = Node("E")
    node = root.left
    node.left = new_node_1
    node.right = new_node_2

    new_node_1 = Node("F")
    new_node_2 = Node("G")
    node = root.right
    node.left = new_node_1
    node.right = new_node_2

def preorder_traverse(node): # 전위 순회
    if node == None : return
    print(node.data, end='->')
    preorder_traverse(node.left)
    preorder_traverse(node.right)

def inorder_traverse(node): # 중위 순회
    if node == None : return
    inorder_traverse(node.left)
    print(node.data, end='->')
    inorder_traverse(node.right)

def postorder_traverse(node): # 후회 순회
    if node == None : return
    postorder_traverse(node.left)
    postorder_traverse(node.right)
    print(node.data, end='->')
    
init_tree()

if __name__ == "__main__":
    preorder_traverse(root)
    print()
    inorder_traverse(root)
    print()
    postorder_traverse(root)