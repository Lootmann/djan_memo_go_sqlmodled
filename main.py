from sqlmodel import Session, SQLModel, create_engine, select

from models.examples import Example
from models.words import Word

engine = create_engine("sqlite:///test.db")
SQLModel.metadata.create_all(engine)


def insert_db():
    with Session(engine) as session:
        word = Word(spell="hello", meaning="こんにちは")
        session.add(word)
        session.commit()

        example1 = Example(
            sentence="hello world", translation="こんにちは、せかい", word_id=word.id
        )

        example2 = Example(
            sentence="hello, goodbye", translation="こんにちは、さようなら", word_id=word.id
        )

        session.add(example1)
        session.add(example2)
        session.commit()


def select_db():
    with Session(engine) as session:
        statement = select(Word)
        words = session.exec(statement)

        for word in words:
            print(word)
            print(word.examples)


def main():
    insert_db()
    select_db()


if __name__ == "__main__":
    main()
