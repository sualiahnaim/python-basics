# Object : objects are specific instances of class \ real world enties
# Class : class is a bluprint for real world entities

class phone:
    def set_color(self,color):
        self.color = color
    def set_cost(self,cost):
        self.cost = cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
    def make_call(self):
        print("Iam making a call")
    def play_game(self):
        print("Iam playing a game")    
    
p1 = phone() # Create a object
p1.set_color("Blue")
p1.set_cost(50000)
print(p1.show_color())   # call
print(p1.show_cost())    # call
p1.make_call()    # call
p1.play_game()    # call

