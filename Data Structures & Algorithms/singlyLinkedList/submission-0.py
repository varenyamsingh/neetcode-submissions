class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, i: int) -> int:
        curr = self.head

        for _ in range(i):
            if curr is None:
                return -1
            curr = curr.next

        if curr is None:
            return -1

        return curr.val

    def insertHead(self, val: int) -> None:
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def remove(self, i: int) -> bool:
        if self.head is None:
            return False

        # Remove head
        if i == 0:
            self.head = self.head.next

            if self.head is None:
                self.tail = None

            return True

        curr = self.head

        for _ in range(i - 1):
            if curr.next is None:
                return False

            curr = curr.next

        # Index doesn't exist
        if curr.next is None:
            return False

        # Removing tail
        if curr.next == self.tail:
            self.tail = curr

        curr.next = curr.next.next

        return True

    def getValues(self) -> list[int]:
        result = []
        curr = self.head

        while curr:
            result.append(curr.val)
            curr = curr.next

        return result