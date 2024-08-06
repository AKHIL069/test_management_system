from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    role: str

    class Config:
        orm_mode = True

class TestBase(BaseModel):
    title: str
    description: str

class TestCreate(TestBase):
    pass

class Test(TestBase):
    id: int

    class Config:
        orm_mode = True

class QuestionBase(BaseModel):
    question_text: str

class QuestionCreate(QuestionBase):
    pass

class Question(QuestionBase):
    id: int
    test_id: int

    class Config:
        orm_mode = True

class AnswerBase(BaseModel):
    answer_text: str
    is_correct: bool

class AnswerCreate(AnswerBase):
    pass

class Answer(AnswerBase):
    id: int
    question_id: int

    class Config:
        orm_mode = True

class ResultBase(BaseModel):
    score: int

class ResultCreate(ResultBase):
    pass

class Result(ResultBase):
    id: int
    user_id: int
    test_id: int

    class Config:
        orm_mode = True
