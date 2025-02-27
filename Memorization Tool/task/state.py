from enum import Enum

class State(Enum):
    EXIT = 0
    MAIN_MENU = 1
    ADD_FLASHCARD_MENU = 2
    ADD_FLASHCARD = 3
    PRACTICE_FLASHCARD = 5
