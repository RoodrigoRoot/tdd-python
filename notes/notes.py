import json
from dataclasses import dataclass


@dataclass
class Note:
    user_id: str
    content: str


    def create(self) -> dict:
        DBNotes.create_note(
            user_id=self.user_id,
            content=self.content
        )
        return {'success': True, 'message': 'Note Created!'}


@dataclass
class DBNotes:
    file_name = 'notes.txt'


    @classmethod
    def create_note(cls, user_id, content):
        all_notes = cls.get_all_notes()
        try:
            if all_notes and all_notes.get(user_id):
                note_id = len(all_notes[user_id]) + 1
                all_notes[user_id].append({note_id: content})
                cls.write_note(content=all_notes)
            elif not all_notes:
                cls.write_note({user_id:[{'id':'1', 'content': content}]})
            else:
                note_to_write = all_notes | {user_id:[{'id':'1', 'content': content}]}
                cls.write_note(note_to_write)
        except Exception:
            return {'success': False, 'mesage': "Can't create note!"}

        return {'success': True, 'mesage': "Note Created!"}

    @classmethod
    def write_note(cls, content):
        file = open(cls.file_name, 'w')
        file.write(json.dumps(content))
        file.write('\n')
        file.close()

    @classmethod
    def read(cls) -> list:
        file = open(cls.file_name, 'a+')
        file.seek(0)
        all_notes = file.read()
        file.close()
        return all_notes

    @classmethod
    def get_all_notes(cls):
        all_notes = cls.read()
        if all_notes.split():
            return json.loads(all_notes)
