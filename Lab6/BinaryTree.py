class Node:
    def __init__(self, value):
        self.value = value
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
                        break
                    else:
                        cur_node = cur_node.right
                        continue
                elif value < cur_node.value:
                    if cur_node.left is None:
                        cur_node.left = new_node
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


def test():
    print("After inserting:")
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

    print_tree(bt.root)

    print("Tree after deleting element which hasn't any child nodes")
    bt.delete(4)
    print_tree(bt.root)

    print("Tree after deleting element which has only one child node")
    bt.delete(7)
    print_tree(bt.root)

    print("Tree after deleting element which has two child nodes")
    bt.delete(10)
    print_tree(bt.root)


test()






