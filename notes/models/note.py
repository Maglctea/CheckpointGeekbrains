from datetime import datetime
from turtle import title
from typing import Optional

from pydantic import BaseModel


class Note(BaseModel):
    id_task: Optional[int] = None
    title: str
    description: str
    created_at: datetime = datetime.now()
    update_at: datetime = datetime.now()

    def __str__(self):
        return f'''ID: {self.id_task}
Наименование: {self.title}
Описание: {self.description}
Создано: {self.created_at}
Изменено: {self.update_at}
{"-" * 10}\n'''


class NoteList(BaseModel):
    counter_id: int = 0
    data: list[Note]

    def add(self, note: Note) -> None:
        self.data.append(note)
        self.counter_id += 1
        note.id_task = self.counter_id
        note.created_at = datetime.now()
        note.update_at = datetime.now()

    def get(self, id_note: Optional[int]) -> Optional[Note | list[Note]]:
        if id_note is None:
            return self.data
        else:
            result = list(filter(lambda task: task.id_task == id_note, self.data))
            return result[0] if result else None

    def delete(self, id_note: int) -> Optional[Note]:
        note = self.get(id_note)
        if note:
            self.data.remove(note)
            return note
        else:
            return None

    def update(self, id_note: int, new_note: Note) -> Optional[Note]:
        note = self.get(id_note)

        if note:
            for arg in vars(new_note).keys():
                value = getattr(new_note, arg)
                setattr(note, arg, value)
            note.update_at = datetime.now()

            return note
        else:
            return None
