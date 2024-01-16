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
        return f""


basic_chars = BasicAttributes(
    color="red",
    year=1998,
    cc = 1200,
    hp = 68,
    total_km=365000
)

basic_chars.__str__()