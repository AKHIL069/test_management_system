from sqlalchemy.orm import Session
from app import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password, role="user")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_tests(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Test).offset(skip).limit(limit).all()

def create_test(db: Session, test: schemas.TestCreate):
    db_test = models.Test(title=test.title, description=test.description)
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test

def update_test(db: Session, test_id: int, test: schemas.TestUpdate):
    db_test = db.query(models.Test).filter(models.Test.id == test_id).first()
    if db_test is None:
        return None
    db_test.title = test.title
    db_test.description = test.description
    db.commit()
    db.refresh(db_test)
    return db_test

def delete_test(db: Session, test_id: int):
    db_test = db.query(models.Test).filter(models.Test.id == test_id).first()
    if db_test is None:
        return None
    db.delete(db_test)
    db.commit()
    return db_test

def get_questions(db: Session, test_id: int):
    return db.query(models.Question).filter(models.Question.test_id == test_id).all()

def create_question(db: Session, question: schemas.QuestionCreate):
    db_question = models.Question(test_id=question.test_id, question_text=question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

def update_question(db: Session, question_id: int, question: schemas.QuestionUpdate):
    db_question = db.query(models.Question).filter(models.Question.id == question_id).first()
    if db_question is None:
        return None
    db_question.question_text = question.question_text
    db.commit()
    db.refresh(db_question)
    return db_question

def delete_question(db: Session, question_id: int):
    db_question = db.query(models.Question).filter(models.Question.id == question_id).first()
    if db_question is None:
        return None
    db.delete(db_question)
    db.commit()
    return db_question

def get_answers(db: Session, question_id: int):
    return db.query(models.Answer).filter(models.Answer.question_id == question_id).all()

def create_answer(db: Session, answer: schemas.AnswerCreate):
    db_answer = models.Answer(question_id=answer.question_id, answer_text=answer.answer_text, is_correct=answer.is_correct)
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer

def update_answer(db: Session, answer_id: int, answer: schemas.AnswerUpdate):
    db_answer = db.query(models.Answer).filter(models.Answer.id == answer_id).first()
    if db_answer is None:
        return None
    db_answer.answer_text = answer.answer_text
    db_answer.is_correct = answer.is_correct
    db.commit()
    db.refresh(db_answer)
    return db_answer

def delete_answer(db: Session, answer_id: int):
    db_answer = db.query(models.Answer).filter(models.Answer.id == answer_id).first()
    if db_answer is None:
        return None
    db.delete(db_answer)
    db.commit()
    return db_answer

def get_results(db: Session, user_id: int):
    return db.query(models.Result).filter(models.Result.user_id == user_id).all()

def create_result(db: Session, result: schemas.ResultCreate):
    db_result = models.Result(user_id=result.user_id, test_id=result.test_id, score=result.score)
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result
