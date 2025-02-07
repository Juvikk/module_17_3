from pydantic import BaseModel


class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int


class UpdateUser(CreateUser):
    firstname: str
    lastname:str
    age: int


class CreateTask(BaseModel):
    title: str
    content: str
    priority: int


class UpdateTask(CreateTask):
    title: str
    content: str
    priority:\
        int