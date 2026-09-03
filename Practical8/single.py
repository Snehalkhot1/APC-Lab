#Single Inheritance --> One parent class → One child class
#The Child class inherits the properties and methods of the Parent class.

class Parent:
    def show_parent(self):
        print("This is Parent class")
class Child(Parent):
    def show_child(self):
        print("This is Child class")
obj = Child()
obj.show_parent()
obj.show_child()