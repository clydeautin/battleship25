class Ship:
    def __init__(self, name: str, length: int):
        self.name = name
        self.length = length
        self.health = length

    def hit(self) -> None:
        self.health -= 1
    
    def sunk(self) -> bool:
        return self.health == 0