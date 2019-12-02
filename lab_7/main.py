import time
import os

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class Tree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, node):
        if value < node.value:
            if node.left is not None:
                self._add(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right is not None:
                self._add(value, node.right)
            else:
                node.right = Node(value)

    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, node):
        if value == node.value:
            return node
        elif value < node.value and node.left is not None:
            self._find(value, node.left)
        elif value > node.value and node.right is not None:
            self._find(value, node.right)

    def delete_tree(self):
        self.root = None

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node, n=1):
        if node is not None:
            n += 3
            self._print_tree(node.left, n)
            print(n * ' ' + str(node.value))
            self._print_tree(node.right, n)


def find_values_in_interval(root, low, high):

    if root is None:
        return

    if low < root.value:
        find_values_in_interval(root.left, low, high)

    if low <= root.value <= high:
        print(root.value, end=' ')

    if high > root.value:
        find_values_in_interval(root.right, low, high)
    return


def main():
    tree = Tree()
    with open('input.txt', 'r') as file:
        for line in file:
            tree.add(int(line))
    tree.print_tree()
    a, b = map(int, input('Print range for searching: ').split())
    find_values_in_interval(tree.root, a, b)
if __name__ == '__main__':
    start_time = time.time()
    main()
    print('\nTotal taken time: {:.5f}'.format(time.time() - start_time))
