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

basic_chars.company
basic_chars.model
basic_chars.year
basic_chars.cc