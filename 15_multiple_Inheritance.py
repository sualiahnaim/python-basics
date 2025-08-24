# Multiple Inheritance : The Child inherits from more than one parent class

class Parent1:
    def assign_string_one(self,str1):
        self.str1=str1
    def show_string_one(self):
        return self.str1   
    
class Parent2:
    def assign_string_two(self,str2):
        self.str2=str2
    def show_string_two(self):
        return self.str2

class Child(Parent1,Parent2):
    def assign_string_three(self,str3):
        self.str3=str3
    def show_string_three(self):
        return self.str3

my_child=Child()
my_child.assign_string_one("Iam string of Parent one")
my_child.assign_string_two("Iam string of Parent two")
my_child.assign_string_three("Iam string of Child")

print(my_child.show_string_one())
print(my_child.show_string_two())
print(my_child.show_string_three())
print("Multiple Inheritance")



