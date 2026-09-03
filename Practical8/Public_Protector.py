class Student:
    def __init__(self):
        self.name = "Snehal"    #public
        self._age = 20          #protected
        self.__marks = 100      #private
        
    def display(self):
        print("Name : ", self.name)
        print("Age : ", self._age)
        print("Marks : ", self.__marks)
            
s = Student()
print(s.name)
print(s._age)
s.display()