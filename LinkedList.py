from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        temp = None

    def add_array(self, array):
        for i in array:
            self.add(i)

    def pop(self, index=None):
        if index is None:
            index = self.size() - 1

        if index == 0:
            curr = self.head
            self.head = self.head.get_next()
            return curr
        else:
            curr = self.head
            i = 0
            while curr.get_next() is not None and i < index - 1:
                curr = curr.get_next()
                i += 1
            to_pop = curr.get_next()
            curr.set_next(to_pop.get_next())
            return to_pop

    def append(self, item):
        if self.size() == 0:
            self.head = Node(item)
        else:
            curr = self.head
            while curr.get_next() is not None:
                curr = curr.get_next()
            temp = Node(item)
            curr.set_next(temp)

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def __str__(self):
        list_str = ""
        curr = self.head
        while curr is not None:
            list_str += str(curr)
            list_str += ", "
            curr = curr.get_next()
        list_str += "End of list"
        return list_str

    def select_sort(self):
        count = 0

        currNode = self.head
        while currNode is not None:
            smallest_node = currNode
            # from next to tail
            nextNode = currNode.get_next()
            while nextNode is not None:
                if nextNode.data < smallest_node.data:
                    smallest_node = nextNode
                nextNode = nextNode.get_next()
            temp = currNode.data
            currNode.data = smallest_node.data
            smallest_node.data = temp
            currNode = currNode.get_next()

        return count

    def bubble_sort(self):
        count = 0
        exchanges = True

        currNode = self.head
        while currNode.get_next() is not None and exchanges:
            exchanges = False
            nextNode = self.head
            while nextNode.get_next() is not None:
                if nextNode.get_next().data < nextNode.data:
                    exchanges = True
                    temp = nextNode.get_next().data
                    nextNode.get_next().data = nextNode.data
                    nextNode.data = temp
                nextNode = nextNode.get_next()
            currNode = currNode.get_next()

        return count

    def copy_list(self):
        copiedList = LinkedList()
        buffer = self.head
        while buffer.get_next() is not None:
            copiedList.append(buffer.data)
            buffer = buffer.get_next()
        copiedList.append(buffer.data)
        return copiedList


def main():
    # Append puts it at the end, add puts it at the beginning

    # First one is already sorted
    # create sorted LL with 500 nodes
    ll_sorted1 = LinkedList()
    for i in range(1, 51):
        ll_sorted1.append(i)
    ll_sorted1_copy = ll_sorted1.copy_list()
    print(ll_sorted1)
    print(ll_sorted1_copy)


main()
