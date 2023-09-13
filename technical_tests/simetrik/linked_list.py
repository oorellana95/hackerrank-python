def reversed_list(nodes):
    ############# DO NOT CHANGE ANYTHING BELOW #############
    my_ll = MySpecialList(nodes)
    head = my_ll.root
    reversed_head = my_ll.reverseList(head)
    return my_ll.print_as_list(reversed_head)


############# DO NOT CHANGE ANYTHING ABOVE #############

class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


class MySpecialList:
    def __init__(self, arr):
        self.root = None
        for item in arr:
            self.insert(self.root, Node(item))

    def __iter__(self):
        node = self.root
        while node is not None:
            yield node
            node = node.next

    def insert(self, root, item):
        if not self.root:
            self.root = item
            return self.root
        for current_node in self:
            pass
        current_node.next = item
        return self.root

    def reverseList(self, head):
        prev = None
        current = self.root
        while current:
            next_node = current.next  # Save the next node
            current.next = prev  # Reverse the pointer
            prev = current
            current = next_node
        self.root = prev
        return self.root

    def print_as_list(self, head):
        node = self.root
        linked_list_as_list = []
        while node is not None:
            linked_list_as_list.append(node.value)
            node = node.next
        return linked_list_as_list