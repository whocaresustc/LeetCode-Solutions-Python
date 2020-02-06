class Vector2D(object):

    def __init__(self, v):
        """
        :type v: List[List[int]]
        """
        self.row = 0
        self.col = 0
        self.v = v
        

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            val = self.v[self.row][self.col]
            self.col += 1   # don't forget
            return val
        return None

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.row < len(self.v):
            if self.col < len(self.v[self.row]):
                return True
            self.row += 1
            self.col = 0
        return False
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()



"""
Design and implement an iterator to flatten a 2d vector. It should support the following operations: next and hasNext.

 

Example:

Vector2D iterator = new Vector2D([[1,2],[3],[4]]);

iterator.next(); // return 1
iterator.next(); // return 2
iterator.next(); // return 3
iterator.hasNext(); // return true
iterator.hasNext(); // return true
iterator.next(); // return 4
iterator.hasNext(); // return false
 

Notes:

Please remember to RESET your class variables declared in Vector2D, as static/class variables are persisted across multiple test cases. Please see here for more details.
You may assume that next() call will always be valid, that is, there will be at least a next element in the 2d vector when next() is called.
 

Follow up:

As an added challenge, try to code it using only iterators in C++ or iterators in Java.
"""
