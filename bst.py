#bst.py by Michael Tornatta
class bst:
    def __init__(self, value = None):
        self.parent = None
        self.right_child = None
        self.left_child = None
        self.value = value

    def is_root(self):
        if self.parent == None:
            return True
        else:
            return False

    def add(self, node):
        if self.value > node.value:
            if self.has_left_child():
                return self.left_child.add(node)
            else:
                self.left_child = node
                node.parent = self
                return node

        elif self.value < node.value:
            if self.has_right_child():
                self.right_child.add(node)
            else:
                self.right_child = node
                node.parent = self
                return node

        return node

    def get_parent(self):
        return self.parent

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_right_child(self, node):
        self.right_child = node

    def set_left_child(self, node):
        self.left_child = node

    def has_child(self):
        if self.right_child != None or self.left_child != None:
            return True
        else:
            return False

    def has_right_child(self):
        if self.right_child != None:
            return True
        else:
            return False

    def has_left_child(self):
        if self.left_child != None:
            return True
        else:
            return False

    def has_both_children(self):
        if self.right_child != None and self.left_child != None:
            return True
        else:
            return False

    def print_tree(self):
        pass
