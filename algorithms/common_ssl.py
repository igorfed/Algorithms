
class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None

class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        '''
        time complexity for get_head() is O(1) as we simply return the head.
        '''
        return self.head_node

    def is_empty(self):
        '''
        Check if list is empty
        '''
        if self.head_node is None:  # Check whether the head is None
            return True
        else:
            return False

    # Insertion at Head / Вставить новый элемент в начало списка 
    def insert_at_head(self, data):
        # Create a new node containing your specified value
        temp_node = Node(data)
        # The new node points to the same node as the head
        temp_node.next_element = self.head_node
        self.head_node = temp_node  # Make the head point to the new node
        return self.head_node  # return the new list

    # Supplementary print function
    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True

    def insert_at_tail(self, value):
        # Creating a new node
        new_node = Node(value)

        # Check if the list is empty, if it is simply point head to new node
        if self.get_head() is None:
            self.head_node = new_node
            return

        # if list not empty, traverse the list to the last node
        temp = self.get_head()

        while temp.next_element is not None:
            temp = temp.next_element

        # Set the nextElement of the previous node to new node
        temp.next_element = new_node
        return

    def delete_at_head(self):
        # Get Head and firstElement of List
        first_element = self.get_head()
        # If List is not empty then link head to the
        # nextElement of firstElement.
        if (first_element is not None):
            self.head_node = first_element.next_element
            first_element.next_element = None
        return
    
    def search(self, dt):
        if self.is_empty():
            print("List is Empty")
            return None
        temp = self.head_node
        while(temp is not None):
            if(temp.data is dt):
                return temp
            temp = temp.next_element

        print(dt, " is not in List!")
        return None
        

lst = LinkedList()  # Linked List created
print(f"1. Get Head {lst.get_head()}")  # Returns None since headNode does not contain any data
print(f"2. Check if list is empty {lst.is_empty()}")  # Returns true

print(f"3. Inserting values in list head")
for i in range(1, 10):
    lst.insert_at_head(i)
lst.print_list()

lst0 = LinkedList()  # Linked List created
lst0.print_list()
insert_at_tail(lst0, value=3)
lst0.print_list()
print(len(lst0))