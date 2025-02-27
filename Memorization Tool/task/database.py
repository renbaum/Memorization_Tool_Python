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



class Database():
    def __init__(self):
        db_file = "flashcard.db"
        count = 0
        while not (statusnew := not os.path.exists(db_file)):
            db_file = f"flashcard{count}.db"
            count += 1
        engine = create_engine(f"sqlite:///{db_file}", echo=False)
        Base.metadata.create_all(bind=engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.session.query(Flashcard).delete()
        self.session.commit()

    def add_flashcard(self):
        flash = Flashcard()
        while flash.question == None or flash.question == "":
            flash.question = input("Question:\n").strip()
        while flash.answer == None or flash.answer == "":
            flash.answer = input("Answer:\n").strip()

        self.session.add(flash)
        return State.ADD_FLASHCARD_MENU

    def practice_flashcard(self):
        flashcards = self.session.query(Flashcard).all()
        for flash in flashcards:
            print(f"Question: {flash.question}")
            answer = input('Please press "y" to see the answer or press "n" to skip:\n')
            if answer == 'y':
                print(f"Answer: {flash.answer}")
        return State.MAIN_MENU









