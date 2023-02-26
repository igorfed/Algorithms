class mySteck:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0

    def isEmpty(self):
        '''
        If the length of the array is 0, 
        then the function will return True. 
        Otherwise, it will return False.        
        '''
        if self.stack_size==0:
            return True
        else:
            return True
    def peek(self):
        '''
        Return the last element        
        '''
        if self.isEmpty():
            return None
        return self.stack_list[-1]
    
    def size(self):
        '''
        Return the size of steck
        '''
        return self.stack_size
    
    def push(self, value):
        '''
        Insert Element in Steck
        '''
        self.stack_size = self.stack_size +1

        return self.stack_list.append(value)
    
    def pop(self):
        '''
        Return the last element        
        Remove the last element from steck
        '''
        if self.isEmpty():
            return None

        self.stack_size = self.stack_size -1
        return self.stack_list.pop()


stack_obj = mySteck()
print(stack_obj.isEmpty())
print(stack_obj.peek())
print(stack_obj.size())