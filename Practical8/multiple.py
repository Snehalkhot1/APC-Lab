# Multiple Inheritance --> Two or more parent classes → One child class
# The Child class inherits from both parent1 and parent2.

class parent1:
    def show_parent1(self):
        print("This is Parent_1 class")
class parent2:
    def show_parent2(self):
        print("This is Parent_2 class")
class Child(parent1, parent2):
    def show_child(self):
        print("This is Child class")
obj = Child()
obj.show_parent1()
obj.show_parent2()
obj.show_child()