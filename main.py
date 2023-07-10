from pprint import pprint as p

from sqlmodel import Session, SQLModel, create_engine, select

from models.examples import Example
from models.words import Word


def enclose(msg: str):
    def outer(func):
        def inner():
            print("***" * 3 + f"{msg}" + "***" * 3)
            func()
            print()

        return inner

    return outer


engine = create_engine("sqlite:///test.db")
SQLModel.metadata.create_all(engine)


@enclose("insert_db")
def insert_db():
    with Session(engine) as session:
        word = Word(spell="hello", meaning="こんにちは")
        session.add(word)
        session.commit()

        example1 = Example(sentence="hello world", translation="こんにちは、せかい", word_id=word.id)

        example2 = Example(sentence="hello, goodbye", translation="こんにちは、さようなら", word_id=word.id)

        session.add(example1)
        session.add(example2)
        session.commit()


@enclose("select_db")
def select_db():
    with Session(engine) as session:
        statement = select(Word)
        words = session.exec(statement)

        for word in words:
            p(word)
            p(word.examples)


@enclose("filter_db")
def filter_db():
    with Session(engine) as session:
        statement = select(Example).where(Example.sentence.contains(","))
        examples = session.exec(statement)

        for ex in examples:
            p(ex)


def main():
    insert_db()
    select_db()
    filter_db()


if __name__ == "__main__":
    main()
