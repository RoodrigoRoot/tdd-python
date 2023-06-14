from unittest import TestCase
from notes.notes import DBNotes, Note
from users.user import User


class ManageNotesTestCase(TestCase):

    def setUp(self) -> None:
        DBNotes.file_name = 'test_notes.txt'
        self.user = User(
            name='rod',
            last_name='alvarez',
            age=27,
            email='rod@azulschool.net'
        )
        self.user.create()

    @classmethod
    def tearDownClass(cls):
        import os
        if os.path.exists('test_notes.txt'):
            os.remove('test_notes.txt')

    def test_create_note(self):
        note = Note(
            user_id=self.user.user_id,
            content='Hagamos esto una vez más'
        )
        result_note = note.create()

        self.assertEqual(
            result_note, {'success': True, 'message': 'Note Created!'})
