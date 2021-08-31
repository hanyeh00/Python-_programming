class Parent:
    
    def print_last_name(self):
        print('Roberts')
    

class Child(Parent):
    
    def print_first_name(self):
        print('Bucky')
    
    def print_last_name(self):
      super (Child,self).print_last_name() #call parent
      print('Snitzleberg')

bucky = Child()
bucky.print_last_name()
