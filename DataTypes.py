class Player:
    def __init__(self, name: str, points: int) -> None:
        self.name = name
        self.points = points
    
    def __str__(self) -> str:
        return self.name + ' has ' + str(self.points) + ' points'
    
    def __repr__(self) -> str:
        return self.name + ' has ' + str(self.points) + ' points'