from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class Example(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sentence: str
    translation: str

    word_id: Optional[int] = Field(default=None, foreign_key="word.id")
    word: Optional["Word"] = Relationship(back_populates="examples")
