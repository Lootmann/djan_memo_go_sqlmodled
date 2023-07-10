from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class Word(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    spell: str
    meaning: str

    examples: List["Example"] = Relationship(back_populates="word")
