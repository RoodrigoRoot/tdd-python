from dataclasses import dataclass, field
from uuid import uuid4
import json
from utils import send_mail


def generate_id():
    return str(uuid4())[:3]


@dataclass
class User:

    user_id: str = field(init=False)
    name: str
    last_name: str
    age: int
    email: str

    def __post_init__(self):
        self.user_id = generate_id()

    def create(self) -> dict:
        try:
            self.validate_age()
            DBUsers.create(
                    {
                        'user_id': self.user_id,
                        'name': self.name,
                        'last_name': self.last_name,
                        'age': self.age,
                        'email': self.email
                    }
                )
        except Exception:
            {'succes': False, 'message': "Can't create user!'",
             'id': self.user_id}

        send_mail()
        return {'succes': True, 'message': 'User created!'}

    @classmethod
    def get_user_by_id(cls, user_id) -> dict:
        return DBUsers.search_user(user_id)

    @classmethod
    def delete_user(cls, user_id: str) -> dict:
        try:
            DBUsers.delete(user_id=user_id)
        except Exception:
            return {'succes': False, 'message': "Can't delete user!'"}
        return {'succes': True, 'message': 'User deleted!'}

    @classmethod
    def update_user(cls, user_id: str, data: dict):
        try:
            data['user_id'] = user_id
            DBUsers.update(user_id=user_id, new_data_user=data)
        except Exception:
            return {'succes': False, 'message': "Can't update user!'"}
        return {'succes': True, 'message': 'Updated user!'}

    def validate_age(self):
        if self.age < 18:
            raise Exception

@dataclass
class DBUsers:
    file_name: str = 'users.txt'

    @classmethod
    def create(cls, data: dict):
        file = open(cls.file_name, 'a+')
        file.write(json.dumps(data))
        file.write('\n')
        file.close()

    @classmethod
    def read(cls) -> list:
        file = open(cls.file_name, 'r')
        all_users = file.readlines()
        file.close()
        return all_users

    @classmethod
    def search_user(cls, user_id):
        all_users = cls.read()
        for user in all_users:
            find_user = json.loads(user)
            if find_user['user_id'] == user_id:
                return json.loads(user)

    @classmethod
    def delete(cls, user_id: str):
        all_users = cls.read()
        file = open(cls.file_name, 'w')
        for user in all_users:
            find_user = json.loads(user)
            if find_user['user_id'] == user_id:
                continue
            file.write(user)
        file.close()

    @classmethod
    def update(cls, user_id: str, new_data_user: dict):
        all_users = cls.read()
        file = open(cls.file_name, 'w')
        for user in all_users:
            find_user = json.loads(user)
            if find_user['user_id'] == user_id:
                file.write(json.dumps(new_data_user))
                file.write('\n')
            else:
                file.write(user)
        file.close()
