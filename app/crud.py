from sqlalchemy.orm import Session
from app import models, schemas

# User CRUD operations
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password, role="user")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Test CRUD operations
def get_tests(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Test).offset(skip).limit(limit).all()

def get_test(db: Session, test_id: int):
    return db.query(models.Test).filter(models.Test.id == test_id).first()

def create_test(db: Session, test: schemas.TestCreate):
    db_test = models.Test(title=test.title, description=test.description)
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test

def update_test(db: Session, test_id: int, test: schemas.TestUpdate):
    db_test = get_test(db, test_id)
    if db_test:
        if test.title is not None:
            db_test.title = test.title
        if test.description is not None:
            db_test.description = test.description
        db.commit()
        db.refresh(db_test)
    return db_test

def delete_test(db: Session, test_id: int):
    db_test = get_test(db, test_id)
    if db_test:
        db.delete(db_test)
        db.commit()
    return db_test

# Question CRUD operations
def get_questions(db: Session, test_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Question).filter(models.Question.test_id == test_id).offset(skip).limit(limit).all()

def get_question(db: Session, question_id: int):
    return db.query(models.Question).filter(models.Question.id == question_id).first()

def create_question(db: Session, question: schemas.QuestionCreate):
    db_question = models.Question(test_id=question.test_id, question_text=question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

def update_question(db: Session, question_id: int, question: schemas.QuestionUpdate):
    db_question = get_question(db, question_id)
    if db_question:
        if question.question_text is not None:
            db_question.question_text = question.question_text
        db.commit()
        db.refresh(db_question)
    return db_question

def delete_question(db: Session, question_id: int):
    db_question = get_question(db, question_id)
    if db_question:
        db.delete(db_question)
        db.commit()
    return db_question

# Answer CRUD operations
def get_answers(db: Session, question_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Answer).filter(models.Answer.question_id == question_id).offset(skip).limit(limit).all()

def get_answer(db: Session, answer_id: int):
    return db.query(models.Answer).filter(models.Answer.id == answer_id).first()

def create_answer(db: Session, answer: schemas.AnswerCreate):
    db_answer = models.Answer(question_id=answer.question_id, answer_text=answer.answer_text, is_correct=answer.is_correct)
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer

def update_answer(db: Session, answer_id: int, answer: schemas.AnswerUpdate):
    db_answer = get_answer(db, answer_id)
    if db_answer:
        if answer.answer_text is not None:
            db_answer.answer_text = answer.answer_text
        if answer.is_correct is not None:
            db_answer.is_correct = answer.is_correct
        db.commit()
        db.refresh(db_answer)
    return db_answer

def delete_answer(db: Session, answer_id: int):
    db_answer = get_answer(db, answer_id)
    if db_answer:
        db.delete(db_answer)
        db.commit()
    return db_answer

# Result CRUD operations
def get_results(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Result).filter(models.Result.user_id == user_id).offset(skip).limit(limit).all()

def get_result(db: Session, result_id: int):
    return db.query(models.Result).filter(models.Result.id == result_id).first()

def create_result(db: Session, result: schemas.ResultCreate):
    db_result = models.Result(user_id=result.user_id, test_id=result.test_id, score=result.score)
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

def update_result(db: Session, result_id: int, result: schemas.ResultCreate):
    db_result = get_result(db, result_id)
    if db_result:
        db_result.score = result.score
        db.commit()
        db.refresh(db_result)
    return db_result

def delete_result(db: Session, result_id: int):
    db_result = get_result(db, result_id)
    if db_result:
        db.delete(db_result)
        db.commit()
    return db_result
