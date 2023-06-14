from unittest import TestCase
from users.user import DBUsers
from os.path import exists
from os import remove
from pathlib import Path
import json


class DBUserTestCase(TestCase):

    def setUp(self) -> None:
        #remove(f'{Path.cwd()}/test_users.txt')
        self.db_users = DBUsers
        self.db_users.file_name = 'test_users.txt'

    @classmethod
    def tearDownClass(cls):
        import os
        if os.path.exists('test_users.txt'):
            os.remove('test_users.txt')



    def test_create(self):
        user_data = {
            'user_id': '1',
            "email": "algo@algo.com",
            "name": "rodrigo",
            "last_name": "urcino",
            "age": 25
        }
        self.db_users.create(user_data)
        file = open(self.db_users.file_name, 'r')
        user = json.loads(file.readlines()[0])
        file.close()
        open(self.db_users.file_name, 'w').close()

        self.assertDictEqual(user, user_data)
        self.assertTrue(exists(f'{Path.cwd()}/{DBUsers.file_name}'))

    def test_read(self):
        user_data = {
            'user_id': '1',
            "email": "algo@algo.com",
            "name": "rodrigo",
            "last_name": "urcino",
            "age": 25
        }

        self.db_users.create(user_data)
        all_users_from_file = self.db_users.read()
        open(self.db_users.file_name, 'w').close()

        self.assertIsInstance(all_users_from_file, list)

        self.assertIsNotNone(all_users_from_file)

    def test_search_user(self):
        user_data = {
            'user_id': '1',
            "email": "algo@algo.com",
            "name": "rodrigo",
            "last_name": "urcino",
            "age": 25
        }

        self.db_users.create(user_data)
        user_from_file = self.db_users.search_user(user_id=user_data['user_id'])
        open(self.db_users.file_name, 'w').close()

        self.assertIsNotNone(user_from_file)
        self.assertDictEqual(user_from_file, user_data)

    def test_delete(self):
        user_data = {
            'user_id': '1',
            "email": "algo@algo.com",
            "name": "rodrigo",
            "last_name": "urcino",
            "age": 25
        }

        self.db_users.create(user_data)
        self.db_users.delete(user_id=user_data['user_id'])
        user_from_file = self.db_users.search_user(user_id=user_data['user_id'])

        self.assertIsNone(user_from_file)

    def test_update(self):
        user_data = {
            'user_id': '1',
            "email": "algo@algo.com",
            "name": "rodrigo",
            "last_name": "urcino",
            "age": 25
        }
        new_data_user = user_data
        new_data_user["age"] = 27
        new_data_user["name"] = "Rodrigo"

        self.db_users.create(user_data)
        self.db_users.update(user_id=user_data['user_id'], new_data_user=new_data_user)
        user_from_file = self.db_users.search_user(user_id=user_data['user_id'])
        open(self.db_users.file_name, 'w').close()

        self.assertDictEqual(user_from_file, new_data_user)


