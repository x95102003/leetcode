class MyCircularDeque(object):

    def __init__(self, k):
        self.max_size = k
        self.cur_size = 0
        self.myqueue = list()
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.myqueue.insert(0, value) 
        self.cur_size +=1 
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.myqueue.append(value) 
        self.cur_size +=1
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        del self.myqueue[0]
        self.cur_size -=1 
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        del self.myqueue[-1]
        self.cur_size -=1 
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.myqueue[0]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.myqueue[-1]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.cur_size == 0

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.cur_size == self.max_size

if __name__ == '__main__':
# Your MyCircularDeque object will be instantiated and called as such:
    obj = MyCircularDeque(10)
    param_1 = obj.insertFront(5)
    param_2 = obj.insertLast(3)
    param_3 = obj.deleteFront()
    param_4 = obj.deleteLast()
    param_5 = obj.getFront()
    param_6 = obj.getRear()
    param_7 = obj.isEmpty()
    param_8 = obj.isFull()
