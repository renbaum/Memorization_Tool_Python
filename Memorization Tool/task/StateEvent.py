from database import Database
from state import State
from menu import Menu


class StateEvent:
    def __init__(self, state):
        self.state = state
        self.menu = Menu()
        self.database = Database()

    def handle_state(self) -> bool:
        state_actions = {
            State.MAIN_MENU: (self.menu.main_menu, None),  # Maps states to respective functions and their required params.
            State.ADD_FLASHCARD_MENU: (self.menu.flashcard_menu, None),
            State.ADD_FLASHCARD: (self.database.add_flashcard, None),
            State.PRACTICE_FLASHCARD: (self.database.practice_flashcard, None),
        }
        if self.state == State.EXIT:
            return False  # Exit the loop.

        action = state_actions.get(self.state)
        if action:
            func, param = action
            self.state = func(param) if param else func()  # Call the mapped function with or without parameters.
        else:
            print("Not implemented!")  # Handle unspecified state.
            print()
            self.state = State.MAIN_MENU

        return True

    def get_state(self) -> State:
        return self.state

    def set_state(self, state: State):
        self.state = state

    def main_loop(self):
        while True:
            if not self.handle_state():
                break
        print("Bye!")

