from presenter import MenuPresenter
from view import ConsoleView
from models.note import NoteList

view = ConsoleView()
notes_list = NoteList(data=[])
menu_presenter = MenuPresenter(view, notes_list)
menu_presenter.run()