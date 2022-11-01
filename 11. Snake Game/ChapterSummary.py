# What's Inheritance?

# Inheritance models what is called an is-a relationship. This means that when you have a Derived class that inherits from a
# Base class, you created a relationship where Derived is-a specialized version of Base.


#          Base
#            ^
#            |
#            |
#            |
#       Derived(Base)


# Inheritance is basically gaining the attributes and methods of a parent class and ultimately expanding on that without having to rebuild
# methods and add attributes you've already created somewhere
# E.g

class Animal():
    def __init__ (self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class dog(Animal):
    # inherits all the methods
    def __init__ (self):
        pass
        super().__init__()  # inherits all the attributes and all else in the init method

    def breathe(self):
        super().breathe()   # inherits all in the breathe function in the parent 
        print("doing this underwater.")    # add to it


    def swin(self):
        print("moving in water.")


justin = dog()
print(justin.num_eyes)
justin.breathe()