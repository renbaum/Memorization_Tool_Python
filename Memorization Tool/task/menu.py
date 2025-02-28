from state import State

class Menu:
    def __init__(self):
        pass

    def main_menu(self):
        print()
        print("1. Add flashcards")
        print("2. Practice flashcards")
        print("3. Exit")
        return self.choice_main_menu()

    def choice_main_menu(self):
        answer = self.get_user_choice()
        match answer:
            case "3": return State.EXIT
            case "1": return State.ADD_FLASHCARD_MENU
            case "2": return State.PRACTICE_FLASHCARD
            case _:
                print(f"{answer} is not an option")
                print()
                return State.MAIN_MENU

    def flashcard_menu(self):
        print()
        print("1. Add a new flashcard")
        print("2. Exit")
        return self.choice_flashcard_menu()

    def choice_flashcard_menu(self):
        answer = self.get_user_choice()
        match answer:
            case "2": return State.MAIN_MENU
            case "1": return State.ADD_FLASHCARD
            case _:
                print(f"{answer} is not an option")
                print()
                return State.ADD_FLASHCARD_MENU

    def get_user_choice(self) -> str:
        answer = input()
        return answer