class DynamicArray:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * self.capacity

    def append(self, x):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        
        self.array[self.size] = x
        self.size += 1

    def _resize(self, new_capacity):
        print(f"Resizing: {self.capacity} -> {new_capacity}")
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def pop(self):
        if self.size == 0: 
            return None
        val = self.array[self.size - 1]
        self.array[self.size - 1] = None 
        self.size -= 1
        return val

    def __str__(self):
        return str([self.array[i] for i in range(self.size)])

# --- TASK 2: LINKED LISTS ---
class SNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, x):
        new_node = SNode(x)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, x):
        new_node = SNode(x)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next: 
            curr = curr.next
        curr.next = new_node

    def delete_by_value(self, x):
        if not self.head: return
        if self.head.data == x:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next and curr.next.data != x:
            curr = curr.next
        if curr.next: 
            curr.next = curr.next.next

    def traverse(self):
        res = []
        curr = self.head
        while curr:
            res.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(res) if res else "Empty List")

class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_after_node(self, target, x):
        curr = self.head
        while curr and curr.data != target:
            curr = curr.next
        if curr:
            new_node = DNode(x)
            new_node.next = curr.next
            new_node.prev = curr
            if curr.next: 
                curr.next.prev = new_node
            curr.next = new_node

    def delete_at_position(self, pos):
        if not self.head: return
        curr = self.head
        if pos == 0:
            self.head = curr.next
            if self.head: self.head.prev = None
            return
        for _ in range(pos):
            if curr: curr = curr.next
        if curr:
            if curr.next: curr.next.prev = curr.prev
            if curr.prev: curr.prev.next = curr.next

class Stack:
    def __init__(self):
        self.storage = SinglyLinkedList()

    def push(self, x):
        self.storage.insert_at_beginning(x)

    def pop(self):
        if self.is_empty(): return None
        val = self.storage.head.data
        self.storage.head = self.storage.head.next
        return val

    def peek(self):
        return self.storage.head.data if not self.is_empty() else None

    def is_empty(self):
        return self.storage.head is None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new_node = SNode(x)
        if not self.tail:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.head: return None
        val = self.head.data
        self.head = self.head.next
        if not self.head: 
            self.tail = None
        return val

def is_balanced(expr):
    s = Stack()
    pairs = {')': '(', '}': '{', ']': '['} 
    for char in expr:
        if char in pairs.values():
            s.push(char)
        elif char in pairs:
            if s.is_empty() or s.pop() != pairs[char]:
                return False
    return s.is_empty()

if __name__ == "__main__":
    print("--- Task 1: Dynamic Array ---")
    da = DynamicArray(capacity=2)
    for i in range(1, 12): da.append(i) 
    print(f"Array: {da}")
    print(f"Popped: {da.pop()}, {da.pop()}, {da.pop()}") 
    print(f"Updated Array: {da}")

    print("\n--- Task 2: Linked Lists ---")
    sll = SinglyLinkedList()
    sll.insert_at_beginning(10)
    sll.insert_at_end(20)
    sll.traverse()
    sll.delete_by_value(10)
    sll.traverse()

    print("\n--- Task 4: Parentheses Checker ---")
    test_cases = ["([])", "([)]", "(((", ""] 
    for test in test_cases:
        print(f"'{test}' -> {'Balanced' if is_balanced(test) else 'Not balanced'}")