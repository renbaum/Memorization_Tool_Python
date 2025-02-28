import os

from sqlalchemy import Column, String, Integer, create_engine, func
from sqlalchemy.orm import declarative_base, sessionmaker
from state import State

Base = declarative_base()

class Flashcard(Base):
    __tablename__ = 'flashcard'

    id = Column(Integer(), primary_key=True)
    question = Column(String(100))
    answer = Column(String(100))
    box = Column(Integer(), default=1)




class Database():
    def __init__(self):
        db_file = "flashcard.db"
        engine = create_engine(f"sqlite:///{db_file}", echo=False)
        Base.metadata.create_all(bind=engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()
    def add_flashcard(self):
        flash = Flashcard()
        while flash.question == None or flash.question == "":
            flash.question = input("Question:\n").strip()
        while flash.answer == None or flash.answer == "":
            flash.answer = input("Answer:\n").strip()

        self.session.add(flash)
        self.session.commit()
        return State.ADD_FLASHCARD_MENU

    def practice_flashcard(self):
        flashcards = self.session.query(Flashcard).all()
        if len(flashcards) == 0:
            print()
            print("There is no flashcard to practice!")
            return State.MAIN_MENU
        for flash in flashcards:
            print(f"Question: {flash.question}")
            self.work_with_flashcard(flash)
        return State.MAIN_MENU

    def work_with_flashcard(self, flashcard: Flashcard):
        while True:
            print('press "y" to see the answer:')
            print('press "n" to skip:')
            print('press "u" to update:')

            answer = input()
            match answer.lower():
                case "y":
                    print(f"Answer: {flashcard.answer}")
                    self.update_box(flashcard)
                    break
                case "n":
                    break
                case "u":
                    self.update_flashcard(flashcard)
                    break
                case _:
                    print(f"{answer} is not an option")
                    print()

    def update_flashcard(self, flashcard: Flashcard):
        while True:
            print('press "d" to delete the flashcard:')
            print('press "e" to edit the flashcard:')

            answer = input()
            match answer.lower():
                case "d":
                    self.session.delete(flashcard)
                    self.session.commit()
                    break
                case "e":
                    print(f"\ncurrent question: {flashcard.question}")
                    q = input("please write a new question:\n")
                    print(f"\ncurrent answer: {flashcard.answer}")
                    a = input("please write a new answer:\n")
                    if len(a) > 0: flashcard.answer = a
                    if len(q) > 0: flashcard.question = q
                    self.session.commit()
                    break
                case _:
                    print(f"{answer} is not an option")
                    print()

    def update_box(self, flashcard: Flashcard):
        while True:
            print('press "y" if your answer is correct:')
            print('press "n" if your answer is wrong:')

            answer = input()
            match answer.lower():
                case "y":
                    if flashcard.box == 3:
                        self.session.delete(flashcard)
                    else:
                        flashcard.box = flashcard.box + 1
                    self.session.commit()
                    break
                case "n":
                    flashcard.box = 1
                    self.session.commit()
                    break
                case _:
                    print(f"{answer} is not an option")
                    print()









