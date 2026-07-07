import ctypes

class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = self._make_array(self.capacity) 



    def get(self, i: int) -> int:
        if i < 0 or i >= self.size:
            raise IndexError("Out of bounds")
        return self.array[i]



    def set(self, i: int, n: int) -> None:
        if i < 0 or i >= self.size:
            raise IndexError("Out of bounds")

        self.array[i] = n 


    def pushback(self, n: int) -> None:
        if self.size == self.capacity: 
            self._resize()
        self.array[self.size] = n
        self.size += 1 



    def popback(self) -> int:
        val = self.array[self.size - 1 ]
        self.size -= 1 
        return val 

    def _resize(self) -> None:
        new_capacity = self.capacity*2
        new_array = self._make_array(new_capacity)

        #copy elements from old to new 

        for i in range(self.size):
            new_array[i] = self.array[i]
        
        self.array = new_array
        self.capacity = new_capacity 


    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity

    def _make_array(self,capacity: int):
        #Return a new array with double capacity 
        return (capacity * ctypes.py_object)()

