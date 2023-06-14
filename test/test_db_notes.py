import json
from unittest import TestCase
from notes.notes import DBNotes


class DBNotesTestCase(TestCase):

    def setUp(self) -> None:
        self.file_name = 'test_notes.txt'
        DBNotes.file_name = self.file_name
        self.user_id = 'd5d4e636'
        self.content = 'Una vez'

    @classmethod
    def tearDownClass(cls):
        import os
        if os.path.exists('test_notes.txt'):
            os.remove('test_notes.txt')

    def test_create_note(self):
        DBNotes.create_note(user_id=self.user_id, content=self.content)
        file = open(self.file_name, 'r')
        content_file = json.loads(file.read())

        self.assertIsNotNone(content_file)
        self.assertEqual(content_file[self.user_id][0]['content'], self.content)
        self.assertEqual(content_file[self.user_id][0]['id'], '1')
        file.close()

    def test_get_all_notes(self):
        DBNotes.create_note(user_id=self.user_id, content=self.content)
        DBNotes.create_note(user_id='23', content=self.content)

        all_notes = DBNotes.get_all_notes()

        self.assertIsNotNone(all_notes[self.user_id])
        self.assertIsNotNone(all_notes['23'])
