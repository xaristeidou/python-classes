'''
Parent / Base class which will be inherited from other objects. 
'''
class Fruit:
    def __init__(
            self,
            fruit_name: str,
            color: str,
            weight: float
    ) -> None:
        self.fruit_name = fruit_name
        self.color = color
        self.weight = weight

    def fruit_print_details(self) -> None:
        return f"This is a {self.fruit_name}, is {self.color}, and weights {self.weight}"
    
'''
This is a Child class. It inherites that attributes and methods from the 'Fruit' class
We can access all the attributes and methods that are assigned to the Parent class
'''
class Watermellon(Fruit):
    pass

watermellon = Watermellon(
    fruit_name="watermellon",
    color="red_green",
    weight=10.5
)

watermellon.fruit_name
watermellon.color
watermellon.weight

watermellon.fruit_print_details()