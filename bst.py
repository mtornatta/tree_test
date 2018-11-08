#bst.py by Michael Tornatta
class bst:
    def __init__(self, parent = None, right_child = None, left_child = None):
        self.parent = parent
        self.right_child = right_child
        self.left_child = left_child
        self.height = 0

    def is_root(self):
        if self.parent == None:
            return True
        else:
            return False

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
