class MyQueue:

    def __init__(self):
        self.S_out=[]
        self.S_in=[]
        

    def push(self, x: int) -> None:
        self.S_in.append(x)
        

    def pop(self) -> int:
        self.move()
        if self.S_out:
            return self.S_out.pop()
        else:    
            return None
        
        

    def peek(self) -> int:
        self.move()
        if self.S_out:
            return self.S_out[-1]
        else:    
            return None       


        
    def empty(self) -> bool:
        return not self.S_out and not self.S_in
    def move(self):
        if not self.S_out:
            while self.S_in:
                self.S_out.append(self.S_in.pop())

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()