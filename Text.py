from sqlalchemy import Column, String, Integer
import models.Text
from repository.base import Base


class Text(Base.Base):
    __tablename__ = 'texts'

    id = Column(Integer, primary_key=True)
    language = Column(String(20))
    tag = Column(String(2000))
    value = Column(String(100000))
    description = Column(String(2000))

    def __init__(self,
                 id=0,
                 language="",
                 tag="",
                 value="",
                 description="",
                 text=models.Text.Text()):
        if (text.id or text.value):
            self.id = text.id
            self.language = text.language
            self.tag = text.tag
            self.value = text.value
            self.description = text.description
        else:
            self.id = id
            self.language = language
            self.tag = tag
            self.value = value
            self.description = description
