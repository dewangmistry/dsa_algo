class TreeNode:
    def __init__(self, name, designation) -> None:
        self.name = name
        self.designation = designation
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

    def print_tree(self, print_type):
        spaces = ' ' * self.get_level() + '  |--' if self.parent else ''
        if print_type == "name":
            to_print = self.name
        elif print_type == "designation":
            to_print = self.designation
        else:
            to_print = self.name + "(" + self.designation + ")"
        print(spaces + to_print)

        if self.children:
            for child in self.children:
                child.print_tree(print_type)

def build_management_tree():
    root = TreeNode("Nilupul","CEO")

    cto = TreeNode("Chinmay", "CTO")
    infra_head = TreeNode("Vishwa", "Infrastructure Head")
    infra_head.add_child(TreeNode("Dhaval", "Cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit", "App Manager"))
    cto.add_child(infra_head)
    cto.add_child(TreeNode("Aamir", "Application Head"))

    hr_head = TreeNode("Gels", "HR Head")
    hr_head.add_child(TreeNode("Peter", "Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

    root.add_child(cto)
    root.add_child(hr_head)
    return root

if __name__ == "__main__":
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy