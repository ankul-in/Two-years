#kata
#https://www.codewars.com/kata/570e6e32de4dc8a8340016dd/train/python


class Lamp(object):
    def __init__(self,colour):
        self.color=colour
        self.on=False
    def toggle_switch(self):
        print("changing state of lamp-->")
        if self.on==True:
            self.on=False
        else:
            self.on=True
        
    def state(self):
        if self.on==True:
            return "The lamp is on."
        else:
            return "The lamp is off."
        

my_lamp = Lamp("Blue")
print(my_lamp.state())
my_lamp.toggle_switch()
print(my_lamp.state())