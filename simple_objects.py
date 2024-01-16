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

        self.company = company
        self.model = model
        self.color = color
        self.year = year
        self.cc = cc
        self.hp = hp
        self.total_km = total_km

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