# Multi Level Inheritance : We have Parent, Child, Grandchild relationship

class Parent:
    def get_name(self,name):
        self.name=name
    def show_name(self):
        return self.name

class Child(Parent):
    def get_age(self,age):
        self.age=age
    def show_age(self):
        return self.age

class Grandchild(Child):
    def get_gender(self,gender):
        self.get_gender=gender
    def show_gender(self):
        return self.get_gender

gc=Grandchild()
gc.get_name("Ram Singh")
gc.get_age(35)
gc.get_gender("Male")

print(gc.show_name())
print(gc.show_age())
print(gc.show_gender())
