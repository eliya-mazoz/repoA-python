import asyncio
from user_dataclasses import User


class Users:

    def __init__(self):
        pass

    async def get_user(self, user_id: int) -> User:
        """
        Create user
        Args:
            user_id (int): user id
        """
        print("get user id ", user_id)
        return User(name='John Doe', username='johndoe', email="test@test.com", age=25)

    async def create_user(self, user_data: User) -> None:
        """
        Create user
        """
        print("successfully created user")

    async def update_user(self, user_id: int, user_data: User) -> None:
        """
        Update user
        """

        print("successfully updated user", user_id)

    async def delete_user(self, user_id: int) -> None:
        """
        Delete user
        """
        print("successfully deleted user", user_id)
