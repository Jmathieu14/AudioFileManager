class Aka:
    def __init__(self, name: str) -> None:
        self.name = name

    def to_dict(self) -> dict[str]:
        return {
            "name": self.name
        }
    
    def __eq__(self, __value: object) -> bool:
        return type(__value) == type(self) and self.name == __value.name