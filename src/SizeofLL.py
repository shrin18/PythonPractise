import sys
import os

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class singly_linked_list:
    def __init__(self):
        #create an empty list
        self.tail = None
        self.head = None
        self.count = 0

    def append_item(self, data):
        #Append items on the list
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.count += 1

    def iterate_item(self):
        #iterate the list
        current_item = self.tail
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val

    def __getitem__(self, index):
        if index > (self.count-1):
            return "Index out of range"
        current_val = self.tail
        for n in range(index):
            current_val = current_val.next
        return current_val.data

items = singly_linked_list()

items.append_item('PHP')
items.append_item('C++')
items.append_item('C#')
items.append_item('Java\n')
items.append_item('Shrinish')
items.append_item('Heramb')
items.append_item('Donde')

print("Search using index: \n")
print(items[0])
print(items[1])
print(items[2])
print(items[3])
print(items[10])

print("Printing original list: \n")
for val in items.iterate_item():
    print(val)

print("\nSize of list is:", items.count)