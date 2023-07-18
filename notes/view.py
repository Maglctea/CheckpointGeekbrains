class ConsoleView:
    def get_input(self):
        return input()

    def print_message(self, message, *args):
        print(message, *args)
