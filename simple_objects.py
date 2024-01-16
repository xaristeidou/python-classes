class BasicAttributes:
    def __init__(
            self,
            color: str,
            year: int,
            cc: int,
            hp: int,
            total_km: float
    ) -> None:
        
        self.color = color
        self.year = year
        self.cc = cc
        self.hp = hp
        self.total_km = total_km


basic_chars = BasicAttributes(
    color="red",
    year=1998,
    cc = 1200,
    hp = 68,
    total_km=365000
)
