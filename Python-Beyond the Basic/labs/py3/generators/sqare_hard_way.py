'''
This is the hard way to create an efficient of iterator
'''
class Squares:
    def __init__(self, max_root):
        self.max_root = max_root
        self.root = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.root == self.max_root:
            raise StopIteration
        value = self.root ** 2
        self.root += 1
        return value
        
for sq in Squares(5):
    print (sq)