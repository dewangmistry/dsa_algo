class BinarySearchTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return
        
        # Add child on left subtree
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add child on right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        # visit left subtree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit root node
        elements.append(self.data)

        # visit right subtree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):

        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

        # Can also do as below
        # return min(self.in_order_traversal())

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

        # Can also do as below
        # return max(self.in_order_traversal())

    def calculate_sum(self):
        return sum(self.in_order_traversal())

    def post_order_traversal(self):
        elements = []

        # visit left subtree
        if self.left:
            elements += self.left.post_order_traversal()

        # visit right subtree
        if self.right:
            elements += self.right.post_order_traversal()

        # visit root node
        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = []

        # visit root node
        elements.append(self.data)

        # visit left subtree
        if self.left:
            elements += self.left.pre_order_traversal()

        # visit right subtree
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def delete(self, val):

        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete(min_val)

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)
        
        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__":
    # numbers = [40,30,50,25,35,45,60,15,28,55,70]
    # root = build_tree(numbers)
    # print(root.in_order_traversal())
    # # print(root.search(19))
    # # # root.add_child(12)
    # # print(root.in_order_traversal())
    # # # root.add_child(13)
    # # print(root.in_order_traversal())
    # # print(root.find_min())
    # # print(root.find_max())
    # # print(root.calculate_sum())
    # # print(root.post_order_traversal())
    # # print(root.pre_order_traversal())
    # root.delete(45)
    # print(root.in_order_traversal())

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(20)
    print("After deleting 20 ",numbers_tree.in_order_traversal()) # this should print [1, 4, 9, 17, 18, 23, 34]

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(9)
    print("After deleting 9 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 17, 18, 20, 23, 34]

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(17)
    print("After deleting 17 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 9, 18, 20, 23, 34]