# Linked list

Связанный список (linked list) — это структура данных, в которой объекты расположены в линейном порядке. Однако, в отличие от массива, в котором этот порядок определяется индексами, порядок в связанном списке определяется указателями на каждый объект. Связанные списки обеспечивают простое и гибкое представление динамических множеств и поддерживают все операции. 

Связанные списки отличаются от списков способом хранения элементов в памяти. В то время как списки используют непрерывный блок памяти для хранения ссылок на свои данные, связанные списки хранят ссылки как часть своих собственных элементов.

Связынные списки имеют линейную структуру. 

`Реализация двухсвязного списка`

```python
# Adding a node at the front of the list
def push(self, new_data):

	# 1 & 2: Allocate the Node & Put in the data
	new_node = Node(data=new_data)

	# 3. Make next of new node as head and previous as NULL
	new_node.next = self.head
	new_node.prev = None

	# 4. change prev of head node to new node
	if self.head is not None:
		self.head.prev = new_node

	# 5. move the head to point to the new node
	self.head = new_node

# This code is contributed by jatinreaper
```

C использованием хвоста - позволяет вставлять в конец за O(1) и получить последний элемент за O(1)

```python
class LinkedList:
    def __init__(self):
        self.tail = None 
        self.head = None
        self.prev = None
    
    def insert (self,val):
        new_node = Node (val)
        if self.head is None:
            self.head = new_node
            return
        elif self.tail is None:
            self.head.next = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
```

- Двухсвязный список
    
    ```python
    class Node:
        def __init__(self,val = None):
            self.val = val
            self.next = None
            self.prev = None
    
    class LinkedList:
        def __init__(self):
            self.tail = None 
            self.head = None
        def insert (self,val):
            new_node = Node (val)
            if self.head is None: 
                self.head = new_node
                return
            elif self.tail is None: # добавляем хвост, прикрепляем головной узел к новому узлу, делаем новый узел хвостом, ставим предыдущий указатель на голову
                self.head.next = new_node
                self.tail = new_node
                self.tail.prev = self.head 
            else:
                self.tail.next = new_node    
                new_node.prev = self.tail
                self.tail = new_node
    ```
    

- Идеальная модель linked list
    
    ```python
    class Node:
        def __init__(self, data):
            self.data = data
            self.previous = None
            self.next = None
    
    class DoublyLinkedList:
        def __init__(self):
            self.head = None
            self.tail = None
    
        def is_empty(self):
            return self.head is None
    
        def insert_at_beginning(self, data):
            new_node = Node(data)
            if self.is_empty():
                self.head = self.tail = new_node
            else:
                new_node.next = self.head
                self.head.previous = new_node
                self.head = new_node
    
        def insert_at_end(self, data):
            new_node = Node(data)
            if self.is_empty():
                self.head = self.tail = new_node
            else:
                new_node.previous = self.tail
                self.tail.next = new_node
                self.tail = new_node
    
        def delete_from_beginning(self):
            if self.is_empty():
                return None
            data = self.head.data
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.previous = None
            return data
    
        def delete_from_end(self):
            if self.is_empty():
                return None
            data = self.tail.data
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.tail = self.tail.previous
                self.tail.next = None
            return data
    
        def display_forward(self):
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next
            print()
    
        def display_backward(self):
            current = self.tail
            while current:
                print(current.data, end=" ")
                current = current.previous
            print()
    
    # Example usage:
    dll = DoublyLinkedList()
    dll.insert_at_beginning(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    dll.insert_at_beginning(5)
    
    dll.display_forward()  # Output: 5 10 20 30
    dll.display_backward()  # Output: 30 20 10 5
    
    dll.delete_from_beginning()
    dll.delete_from_end()
    
    dll.display_forward()  # Output: 10 20
    dll.display_backward()  # Output: 20 10
    ```