from unittest import TestCase
from users.user import User
from unittest.mock import patch
from utils import send_mail


class ManageUserTestCase(TestCase):

    def setUp(self) -> None:
        self.email = 'azul@azulschool.com'
        self.name = 'Azul'
        self.last_name = 'School'
        self.age = 4

    @classmethod
    def tearDownClass(cls):
        import os
        if os.path.exists('test_users.txt'):
            os.remove('test_users.txt')


    def test_create_user(self):
        with patch('users.user.generate_id') as generate_id_mock:
            with patch('users.user.send_mail') as send_email_mock:
                generate_id_mock.return_value = '123qweaqsdzxc'
                send_email_mock = {'success': True, 'message': 'Email sent!'}

                user = User(
                    email="algo@algo.com",
                    name="rodrigo",
                    last_name="urcino",
                    age=24
                )

                user_create_response = user.create()

                self.assertDictEqual({'succes':True, 'message': 'User created!'}, user_create_response)
                self.assertEqual(user.user_id, "123qweaqsdzxc")
                self.assertEqual(send_email_mock, {'success': True, 'message': 'Email sent!'})

    def test_delete_user(self):
        with patch('users.user.generate_id') as generate_id_mock:
            generate_id_mock.return_value = '123qweaqsdzxc'

            user = User(
                email="algo@algo.com",
                name="rodrigo",
                last_name="urcino",
                age=24
            )

            user_delete_response = User.delete_user(user.user_id)
            get_user_response = User.get_user_by_id(user.user_id)

            self.assertDictEqual({'succes': True, 'message': 'User deleted!'}, user_delete_response)
            self.assertIsNone(get_user_response)


    def test_get_user(self):
        with patch('users.user.generate_id') as generate_id_mock:
            generate_id_mock.return_value = '123qweaqsdzxc'

            data_user = {
                "email":"algo@algo.com",
                "name":"rodrigo",
                "last_name":"urcino",
                "age":24
            }

            user = User(
                **data_user
            )
            data_user['user_id'] = "123qweaqsdzxc"

            user.create()
            get_user_response = User.get_user_by_id(user_id=user.user_id)

            self.assertIsNotNone(get_user_response)
            self.assertDictEqual(get_user_response, data_user)


    def test_update_user(self):
        with patch('users.user.generate_id') as generate_id_mock:
            generate_id_mock.return_value = '123qweaqsdzxc'
            user = User(
                email="algo@algo.com",
                name="rodrigo",
                last_name="urcino",
                age=24
            )
            new_data_user = {
                "email":"rod@azulschool.com",
                "name": "Francisco",
                "last_name": "alvarez",
                "age":27
            }

            user_delete_response = User.update_user(user.user_id, data=new_data_user)
            get_user_response = User.get_user_by_id(user.user_id)

            self.assertDictEqual({'succes': True, 'message': 'Updated user!'}, user_delete_response)
            self.assertIsNotNone(get_user_response)
