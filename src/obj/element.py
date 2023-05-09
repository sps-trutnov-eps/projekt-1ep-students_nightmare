class Element:

    def __init__(self, position: tuple[int], dimensions: tuple[int]) -> None:


        self.x: int = position[0]
        self.y: int = position[1]
        self.width: int = dimensions[0]
        self.height: int = dimensions[1]


    def clicked(self) -> bool:
        pass

