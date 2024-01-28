'''
Parent / Base class which will be inherited from other objects. 
'''
class Fruit:
    def __init__(
            self,
            fruit_name: str = "name",
            color: str = "color",
            weight: float = 0
    ) -> None:
        self.fruit_name = fruit_name
        self.color = color
        self.weight = weight

    def fruit_print_details(self) -> None:
        return f"This is a {self.fruit_name}, is {self.color}, and weighs {self.weight}"
    
'''
This is a Child class. It inherites that attributes and methods from the 'Fruit' class
We can access all the attributes and methods that are assigned to the Parent class
'''
class Watermellon(Fruit):
    pass

# simple inheritancde
watermellon = Watermellon()
watermellon.fruit_name
watermellon.color
watermellon.weight
watermellon.fruit_print_details()


# inheritance with selecting attributes
watermellon = Watermellon(
    fruit_name="watermellon",
    color="red_green",
    weight=10.5
)

watermellon.fruit_name
watermellon.color
watermellon.weight
watermellon.fruit_print_details()



'''
We pass 'Fruit' class in the 'Apple' class, but this time we define the
__init__() method. This will override the __init__() of the Parent class.
Now if we try to access any attribute from 'Fruit' class we won't be able to.
Nevertheless, all methods from Parent class are inhereted. If methods use
attributes they won't be usable, but they are defined.
'''
class Apple(Fruit):
    def __init__(self) -> None:
        pass

apple = Apple()
apple.fruit_name
apple.color
apple.weight
apple.fruit_print_details


'''
To define any new attributes and at the same time keep the Parent class attributes
we have to apply __init__() to the name of the parent class in __init__() of the child
class. Then we can define any new attribute to the child class. 
'''
class Apple(Fruit):
    def __init__(self, quantity) -> None:
        Fruit.__init__(self)
        self.quantity = quantity
    
apple = Apple(quantity=10)
apple.fruit_name
apple.color
apple.weight
apple.quantity
apple.fruit_print_details()



apple.color # will raise an error
apple.fruit_print_details # will show the method is constructed

