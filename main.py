from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine


class Word(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    spell: str
    meaning: str


def main():
    engine = create_engine("sqlite:///test.db")
    SQLModel.metadata.create_all(engine)

    word = Word(spell="hello", meaning="こんにちは")

    with Session(engine) as session:
        session.add(word)
        session.commit()


if __name__ == "__main__":
    main()
