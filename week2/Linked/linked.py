class Node:
    # the singly linked node
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # where the list is created
        self.count = 0
        self.head = None
        self.tail = None

    def iteration(self):
        # where the iteration in the linked list takes place
        current_item = self.head
        while current_item:
            value = current_item.data
            current_item = current_item.next
            yield value

    def AppendItems(self, data):
        # appending items to list
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.count += 1


items = LinkedList()
items.AppendItems('PHP')
items.AppendItems('Python')
items.AppendItems('C#')
items.AppendItems('C++')
items.AppendItems('Java')
for value in items.iteration():
    print(value)
print("\nhead.data: ", items.head.data)
print("tail.data: ", items.tail.data)
