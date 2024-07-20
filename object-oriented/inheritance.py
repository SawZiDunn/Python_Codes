class Employee:
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last
        
class Supervisor(Employee):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password
        
class Chef(Employee):
        
    def leave_request(self, days):
        return "May I take a leave for " + str(days) + " days?"
    
adrian = Supervisor("Adrian", "A", "apple")
emily = Chef("Emily", "E")
Juno = Chef("Juno", "J")

print(emily.leave_request(5))
print(adrian.password)
print(emily.name)