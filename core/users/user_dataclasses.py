from dataclasses import dataclass
from typing import Optional

__all__ = ['User']

@dataclass
class User:
    name: str
    username: str
    email: str
    age: int
    id: Optional[int] = None
