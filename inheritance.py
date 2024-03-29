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
        self.fruit_name: str = fruit_name
        self.color: str = color
        self.weight: float = weight

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
    fruit_name = "watermellon",
    color = "red_green",
    weight = 10.5
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
    def __init__(self, quantity:float) -> None:
        Fruit.__init__(self)
        self.quantity = quantity
    
apple = Apple(quantity = 10)
apple.fruit_name
apple.color
apple.weight
apple.quantity
apple.fruit_print_details()



'''
We can inherite all attributes from Parent class and then override the value of any
attribute we can by passing the value of our new attribute to a selected one in the
__init__() of the Parent class.
'''
class Apple(Fruit):
    def __init__(self, name: str) -> None:
        Fruit.__init__(
            self,
            fruit_name = name
        )

apple = Apple(name = "apple")
apple.fruit_name # the default name of the Parent class have been overridden
apple.color
apple.weight
apple.fruit_print_details()


'''
Instead of the name of the Parent class we can also use the super() function.
It is used instead so the Child class will inherit all methods and attributes from
the Parent class.
'''
class Apple(Fruit):
    def __init__(self) -> None:
        super().__init__()

apple = Apple()
apple.fruit_name
apple.color
apple.weight
apple.fruit_print_details()


'''
We can change any default value of the Parent class by passing the value we want
to any specific attribute to override.
'''
class Apple(Fruit):
    def __init__(self, name: str) -> None:
        super().__init__(fruit_name=name)

apple = Apple(name="apple")
apple.fruit_name
apple.color
apple.weight
apple.fruit_print_details()


'''
Defining a method with the same name of the Parent class method name will override it.
So the method when called will use the new defines method in Child class.
'''
class Apple(Fruit):
    def __init__(self):
        super().__init__()

    def fruit_print_details(self) -> None:
        return "Override of the Parent method"
    
    
apple = Apple()
apple.fruit_name
apple.color
apple.weight
apple.fruit_print_details()


'''
If we don't want to override we can re-define the method in Child class,
and use the super().<method_name>() to denote that this is the same exact method
with the Parent class.
'''
class Apple(Fruit):
    def __init__(self):
        super().__init__()

    def fruit_print_details(self) -> None:
        return super().fruit_print_details()
    

apple = Apple()
apple.fruit_name
apple.color
apple.weight
apple.fruit_print_details()


'''
We can use also the name of the Parent class in __init__ of the Child and then
use the super() function to denote a method from the Parent class.
'''
class Apple(Fruit):
    def __init__(self):
        Fruit.__init__(self)

    def fruit_print_details(self) -> None:
        return super().fruit_print_details()


apple = Apple()
apple.fruit_print_details()
