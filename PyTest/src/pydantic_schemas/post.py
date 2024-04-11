from pydantic import BaseModel, validator, Field


class Post(BaseModel):
    id: int = Field(ls=2)
    title: str


