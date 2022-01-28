class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level()
        print(spaces + self.data)

        if self.children:
            for child in self.children:
                child.print_tree()


def build_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Windows"))

    mobile = TreeNode("Mobile")
    mobile.add_child(TreeNode("iPhone"))
    mobile.add_child(TreeNode("Samsung"))
    mobile.add_child(TreeNode("OnePlus"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Sony"))
    tv.add_child(TreeNode("TCL"))
    tv.add_child(TreeNode("Toshiba"))

    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(tv)

    return root

if __name__ == "__main__":
    root = build_tree()
    root.print_tree()
    # # level = root.children[0].get_level()
    # print(level)