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
    
