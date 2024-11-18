import asyncio
import random

from core.users.user_dataclasses import User

class Users:

    def __init__(self):
        self.current_id = 0
        self.users = {}

    async def create_user(self, user_data: User) -> None:
        """
        Create user
        """
        if user_data.id is None:
            self.current_id = random.randint(1, 1000)
            user_data.id = self.current_id
        if user_data.id in self.users:
            raise Exception("User already exists")
        self.users[user_data.id] = user_data
        print(f"User {user_data.name} with ID {user_data.id} was successfully created ")

    async def get_user(self, user_id: int) -> User:
        """
        Create user
        Args:
            user_id (int): user id
        """
        print("get user id ", user_id)
        user = self.users.get(user_id)
        if user is None:
            raise Exception("User not found")
        return user


    async def delete_user(self, user_id: int) -> None:
        """
        Delete user
        """
        user = self.users.pop(user_id, None)
        if user is None:
            raise Exception("User not found")
        print("successfully deleted user", user_id)
