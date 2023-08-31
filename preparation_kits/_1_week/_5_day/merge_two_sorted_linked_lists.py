from dstructure.SLL import SLL


# Create Singly Linkedlist.

def mergeLists(head1, head2):
    normal_list = []
    while head1.next is not None:
        normal_list.append(head1.data)
        head1 = head1.next
    head1.next = head2
    while head1 is not None:
        normal_list.append(head1.data)
        head1 = head1.next
    normal_list.sort()

    response = SLL()
    for x in range(len(normal_list)):
        res_item = normal_list[x]
        response.insert(res_item)
    return response.head


if __name__ == '__main__':
    llist1, llist2 = SLL(), SLL()
    llist1.insert(1)
    llist1.insert(3)
    llist1.insert(7)
    llist2.insert(1)
    llist2.insert(2)

    llist3 = mergeLists(llist1.head, llist2.head)