from dataclasses import dataclass

__all__ = ['User']


class User(dataclass):
    name: str
    username: str
    email: str
    age: int
