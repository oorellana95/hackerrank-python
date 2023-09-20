import sys

# This line sets the recursion limit for Python. It's set to a very high value (1 billion) to allow for deep
# recursion in the code. This is important because the code uses recursion to traverse the binary tree.
sys.setrecursionlimit(int(1e9))


def swapNodes(indexes, queries):
    """
        Swaps and traverses a binary tree for specified queries.

        Parameters:
            indexes: A list of lists representing the binary tree structure.
                     Each inner list contains two integers, indicating the left and right children of a node.
            queries: A list of integers representing the values of 'k' for each query.

        Returns:
            List of lists, where each inner list contains node values visited in in-order traversal after applying swaps
            for the corresponding query.
        """
    # Prepends an empty list [] to the t list. The purpose of this line is to make the indexing 1-based rather than
    # 0-based. Example: [[], [2, 3], [4, -1], [5, -1], other indexes...]
    indexes = [[]] + indexes

    def f(k, r=1, d=1):
        """
        Recursive function to swap and traverse a binary tree.

        Parameters:
            k: The value of k for the current query.
            r: The current root node's index in the binary tree (initially set to 1 for the root node).
            d: The current depth in the tree (initially set to 1 for the root node).

        Returns:
            List of node values visited in the in-order traversal after applying swaps.
        """
        # Check if the current depth 'd' is divisible by 'k'.
        # If divisible, reverse the order of the children nodes.
        indexes[r] = indexes[r] if d % k else indexes[r][::-1]

        # Recursively swap and traverse the left subtree, visit the current node,
        # and then recursively swap and traverse the right subtree if 'r+1' is not zero.
        result = (
            (f(k, indexes[r][0], d + 1)  # Swap and traverse the left subtree
             + [r]  # Visit the current node and add it to the result
             + f(k, indexes[r][1], d + 1))  # Swap and traverse the right subtree
            if r + 1 else []  # Check if 'r+1' is not zero
        )

        return result

    # Apply the f function to each value of i in the queries list. It effectively swaps and traverses the tree for each
    # query and returns a list of the results.
    return [f(i) for i in queries]


if __name__ == '__main__':
    # Example usage with corrected input format:
    tree_indices = [[2, 3], [4, -1], [5, -1], [6, -1], [7, 8], [-1, 9], [-1, -1], [10, 11], [-1, -1], [-1, -1],
                    [-1, -1]]
    queries = [2, 4]
    result = swapNodes(tree_indices, queries)
    print(result)
