class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.prefix_count = 0


def add_contact(root, contact):
    node = root
    for char in contact:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
        node.prefix_count += 1
    node.is_end_of_word = True


def find_contacts_with_prefix(root, prefix):
    node = root
    for char in prefix:
        if char not in node.children:
            return 0
        node = node.children[char]
    return node.prefix_count


def contacts(queries):
    root = TrieNode()
    results = []

    for query in queries:
        operator = query[0]
        name = ' '.join(query[1:])

        if operator == "add":
            add_contact(root, name)
        elif operator == "find":
            matching = find_contacts_with_prefix(root, name)
            results.append(matching)

    return results


if __name__ == '__main__':

    queries_rows = 4
    queries_input = ['add hack run', 'add hackerrank', 'find hac', 'find hak']
    queries = []
    for query in queries_input:
        queries.append(query.rstrip().split())

    result = contacts(queries)

    print(result)
