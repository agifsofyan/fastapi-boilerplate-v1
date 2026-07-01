from dataclasses import dataclass

@dataclass
class Interest:
    id: int | None
    name: str
    code: str