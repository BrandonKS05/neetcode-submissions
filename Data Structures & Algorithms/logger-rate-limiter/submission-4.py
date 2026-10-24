class Logger:

    def __init__(self):
        self.stack = {}
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.stack:
            self.stack[message] = timestamp + 10
            return True
        elif message in self.stack and timestamp >= self.stack[message]:
            self.stack[message] = timestamp + 10
            return True
        elif message in self.stack and timestamp < self.stack[message]:
            return False
        

      
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
