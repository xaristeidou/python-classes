from typing import Union

class BasicAttributes:
    def __init__(
            self,
            company: str,
            model: str,
            color: str,
            year: int,
            cc: int,
            hp: int,
            total_km: float
    ) -> None:

        self.company: str = company
        self.model: str = model
        self.color: str = color
        self.year: int = year
        self.cc: int = cc
        self.hp: int = hp
        self.total_km: float = total_km

    def __str__(self) -> str:
        '''
        __str__() method provides a string output with details of object's attributes
        '''
        return (
        f"This is a {self.company} {self.model} of {self.year}."
        f"It is {self.color} and has {self.cc} cc engine and {self.hp} horse power."
        f"In total has done {self.total_km} km."
        )
    
    def __repr__(self) -> str:
        '''
        __repr__() method provides an example of how to instanciate the object
        '''
        return (f"BasicAttributes({self.company}, {self.model}, {self.color}, "
        f"{self.year}, {self.cc}, {self.hp}, {self.total_km})")
    
    def __len__(self) -> int:
        '''
        __len__() method returns the length of a specific attribute or whatever
        we choose to return. We can use >>> return len(vars(self)), to get the
        number of attributes of the class
        '''
        return len(vars(self))

    def _vars(self) -> dict:
        '''
        _vars() method returns all attributes with corresponding values.
        This method is not using a built-in function.
        '''
        return vars(self)
    
    def __getitem__(self, key) -> Union[str, int, float]:
        '''
        __getitem__() method returns the value of an attribute passed as key.
        '''
        return vars(self)[f"{key}"]
    

basic_chars = BasicAttributes(
    company = "Toyota",
    model = "Starlet",
    color = "red",
    year = 1998,
    cc = 1200,
    hp = 68,
    total_km = 365000
)

# prints the information about this specific car object
basic_chars.__str__()

basic_chars.__repr__()

basic_chars.__len__()

basic_chars._vars()

basic_chars.__getitem__("company")

'''
isinstance is a built-in function that is responsible to check if an object
is an instance of a specific class. Can be used also a tuple of classes to check.
The example bellow will return True because it check if  basic_chars
is instance of either BasicAttributes or float.
'''
isinstance(basic_chars, (BasicAttributes, float))

'''
hasattr is a built-in function that is responsible to check if an object
has an attribute that is passed as second argument. Returns True if it does
otherwise False.
'''
hasattr(basic_chars, "company")