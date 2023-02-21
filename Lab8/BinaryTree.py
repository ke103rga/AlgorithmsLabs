class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            cur_node = self.root
            while True:
                if value >= cur_node.value:
                    if cur_node.right is None:
                        cur_node.right = new_node
                        new_node.parent = cur_node
                        break
                    else:
                        cur_node = cur_node.right
                        continue
                elif value < cur_node.value:
                    if cur_node.left is None:
                        cur_node.left = new_node
                        new_node.parent = cur_node
                        break
                    else:
                        cur_node = cur_node.left
                        continue

    def raise_key_error(self, key, text=None):
        if text is None:
            text = f"There isn't value {key} in that tree"
        raise KeyError(text)

    def find_inorder_node(self, node, prev_node):
        prev = prev_node
        current = node
        while current.left:
            prev = current
            current = current.left
        return current, prev

    def delete(self, value):
        if self.root is None:
            self.raise_key_error(value)
        else:
            prev_node = None
            cur_node = self.root
            while True:
                if value > cur_node.value:
                    if cur_node.right is None:
                        self.raise_key_error(value)
                    else:
                        prev_node = cur_node
                        cur_node = cur_node.right
                        continue
                elif value < cur_node.value:
                    if cur_node.left is None:
                        self.raise_key_error(value)
                    else:
                        prev_node = cur_node
                        cur_node = cur_node.left
                        continue
                else:
                    if cur_node.left is None and cur_node.right is None:
                        if prev_node is None:
                            self.root = None
                        elif prev_node.value > value:
                            prev_node.left = None
                        else:
                            prev_node.right = None
                    elif cur_node.left is None:
                        if prev_node.value > value:
                            prev_node.left = cur_node.right
                        else:
                            prev_node.right = cur_node.right
                    elif cur_node.right is None:
                        if prev_node.value > value:
                            prev_node.left = cur_node.left
                        else:
                            prev_node.right = cur_node.left
                    else:
                        inorder_node, prev_inorder_node = self.find_inorder_node(cur_node.right, cur_node)
                        prev_inorder_node.left = None
                        if prev_node.value > value:
                            prev_node.left = inorder_node
                        else:
                            prev_node.right = inorder_node
                        inorder_node.left = cur_node.left
                        inorder_node.right = cur_node.right
                    break

    def traverse_preorder(self, root):
        yield root.value
        if root.left is not None:
            # recursively returns a generator object, so it's necessary to use yield from
            yield from self.traverse_preorder(root.left)
        if root.right is not None:
            yield from self.traverse_preorder(root.right)

    def __eq__(self, other):
        try:
            for self_value, other_value in zip(self.traverse_preorder(self.root),
                                               other.traverse_preorder(other.root), strict=True):
                if self_value != other_value:
                    return False
            return True
        except ValueError:
            # Trees have different amount of nodes
            return False


def print_tree(root, val="value", left="left", right="right"):
    def display(root, val=val, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = display(root, val, left, right)
    for line in lines:
        print(" "*10 + line)


def count_nodes(node, need_lvl, lvl=0):
    if node is None:
        return 0
    if lvl == need_lvl-1:
        return int(node.left is not None) + int(node.right is not None)
    return count_nodes(node.left, need_lvl, lvl+1) + count_nodes(node.right, need_lvl, lvl+1)


def contains_eq(tree):
    used_values = []
    for value in tree.traverse_preorder(tree.root):
        if value in used_values:
            return True
        used_values.append(value)
    return False


def test():

    def create_default_tree():
        bt = BinaryTree()
        bt.insert(8)
        bt.insert(10)
        bt.insert(12)
        bt.insert(10)
        bt.insert(9)
        bt.insert(5)
        bt.insert(4)
        bt.insert(7)
        bt.insert(7)
        return bt

    def create_tree_with_unique_values():
        bt = BinaryTree()
        bt.insert(9)
        bt.insert(8)
        bt.insert(10)
        bt.insert(12)
        bt.insert(5)
        bt.insert(4)
        bt.insert(7)
        return bt

    def create_dif_struct_tree():
        bt = BinaryTree()
        bt.insert(9)
        bt.insert(8)
        bt.insert(10)
        bt.insert(12)
        bt.insert(10)
        bt.insert(5)
        bt.insert(4)
        bt.insert(7)
        bt.insert(7)
        return bt

    print("Created tree:")
    bt = create_default_tree()
    print_tree(bt.root)

    print("Let's check if we can count nodes on particular level")
    print(count_nodes(bt.root, 2), end="\n\n")

    print("Also it's important to check if tree contains at least two equals values")
    print(f"The result of checking: {contains_eq(bt)}")
    print("To become more confident let's create a tree with unique values")
    un_bt = create_tree_with_unique_values()
    print(f"The result of checking tree with unique values: {contains_eq(un_bt)}", end="\n\n")

    print("And now we need to compare to trees")
    print("Creating the same tree")
    same_bt = create_default_tree()
    print_tree(same_bt.root)

    print(f"The result of comparing: {bt == same_bt}", end="\n\n")

    print("Let's test some other cases")
    print("1) Delete a node without child nodes:")
    same_bt.delete(10)
    print_tree(same_bt.root)
    print(f"The result of comparing: {bt == same_bt}", end="\n\n")

    print("2) Append an element")
    same_bt.insert(10)
    same_bt.insert(31)
    print_tree(same_bt.root)
    print(f"The result of comparing: {bt == same_bt}", end="\n\n")

    print("3) Create tree with the same values but different structure")
    dif_struct_tree = create_dif_struct_tree()
    print_tree(dif_struct_tree.root)
    print(f"The result of comparing: {bt == same_bt}")


test()

