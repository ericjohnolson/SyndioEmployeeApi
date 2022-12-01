from pydantic import BaseModel


class Employee(BaseModel):
    id: int
    gender: str

    class Config:
        orm_mode = True