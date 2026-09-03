# Hybrid Inheritance
# Combination of Single and Multiple Inheritance
class A:
    def show_a(self):
        print("This is A class")

class B(A):                 # Single Inheritance
    def show_b(self):
        print("This is B class")

class C:
    def show_c(self):
        print("This is C class")

class D(B, C):              # Multiple Inheritance
    def show_d(self):
        print("This is D class")

obj = D()

obj.show_a()
obj.show_b()
obj.show_c()
obj.show_d()