from models.note import NoteList, Note
from utils.json_control import load_json, save_json
from view import ConsoleView


class MenuPresenter:
    def __init__(self, view: ConsoleView, model: NoteList):
        self.view = view
        self.model = model

    def run(self):
        self.menu_control()

    def print_menu(self):
        self.view.print_message(f'{"=" * 10} Меню {"=" * 10}')
        self.view.print_message('1. Все заметки')
        self.view.print_message('2. Определенная заметка')
        self.view.print_message('3. Добавить заметку')
        self.view.print_message('4. Изменить заметку')
        self.view.print_message('5. Удалить заметку')
        self.view.print_message('6. Сохранить заметки')
        self.view.print_message('7. Загрузить заметки')
        self.view.print_message('0. Выход')
        self.view.print_message('>> ')

    def get_id(self):
        self.view.print_message('Введите id\n>> ')
        return int(self.view.get_input())

    def build_note(self) -> Note:
        self.view.print_message('Введите название')
        title = self.view.get_input()
        self.view.print_message('Введите описание')
        description = self.view.get_input()
        return Note(title=title, description=description)

    def menu_control(self):
        command_code = -1
        while command_code != 0:
            self.print_menu()
            command_code = int(self.view.get_input())

            match command_code:
                case 1:
                    result = self.model.get(None)
                    if result:
                        self.view.print_message(*result)
                    else:
                        self.view.print_message('Заметки не найдены')

                case 2:
                    id_note = self.get_id()
                    result = self.model.get(id_note)
                    if result:
                        self.view.print_message(result)
                    else:
                        self.view.print_message(f'Заметка №{id_note} не найдена')

                case 3:
                    note = self.build_note()
                    self.model.add(note)

                case 4:
                    id_note = self.get_id()
                    note = self.build_note()
                    if self.model.update(id_note, note):
                        self.view.print_message(f'Заметка успешно изменена')
                    else:
                        self.view.print_message(f'Заметка №{id_note} не найдена')

                case 5:
                    id_note = self.get_id()
                    if self.model.delete(id_note):
                        self.view.print_message('Заметка успешно удалена')
                    else:
                        self.view.print_message(f'Заметка №{id_note} не найдена')

                case 6:
                    self.view.print_message('Введите имя файла')
                    filename = self.view.get_input()
                    save_json(self.model.model_dump(), filename)

                case 7:
                    self.view.print_message('Введите имя файла')
                    filename = self.view.get_input()
                    self.model = NoteList(**load_json(filename))
