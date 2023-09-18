from collections import deque


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''


def levelOrder(root):
    dictionary = {}
    recursiveLevelOrder(root=root, x=1, dictionary=dictionary)
    output = [y[0] for y in sorted(dictionary.items(), key=lambda x: x[1])]
    print(*output, sep=" ")


def recursiveLevelOrder(root, x, dictionary):
    if root is not None:
        dictionary[root.info] = x
        recursiveLevelOrder(root.left, x + 1, dictionary)
        recursiveLevelOrder(root.right, x + 1, dictionary)


def levelOrderOptimized(root):
    if root is None:
        return

    result = []
    queue = deque([(root, 1)])  # Queue to store nodes and their levels

    while queue:
        node, level = queue.popleft()
        if len(result) < level:
            result.append([])
        result[level - 1].append(node.info)

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    for level_nodes in result:
        print(*level_nodes, sep=" ")


if __name__ == '__main__':
    tree = BinarySearchTree()
    t = 6

    arr = [1, 2, 5, 3, 6, 4]

    for i in range(t):
        tree.create(arr[i])

    levelOrder(tree.root)
