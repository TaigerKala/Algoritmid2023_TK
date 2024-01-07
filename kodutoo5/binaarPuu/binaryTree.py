class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.val = key

    def liiguPreOrder(self):
        print(self.val, end =" ")
        if self.left:
            self.left.liiguPreOrder()
        if self.right:
            self.right.liiguPreOrder()

    def liiguInOrder(self):
        if self.left:
            self.left.liiguInOrder()
        print(self.val, end = " ")
        if self.right:
            self.right.liiguInOrder()

    def liiguPostOrder(self):
        if self.left:
            self.left.liiguPostOrder()
        if self.right:
            self.right.liiguPostOrder()
        print(self.val, end = " ")

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)

print("Pre order Traversal: ", end="")
root.liiguPreOrder()
print("\nIn order Traversal: ", end="")
root.liiguInOrder()
print("\nPost order Traversal: ", end="")
root.liiguPostOrder()