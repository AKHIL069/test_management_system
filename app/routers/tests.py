from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, models, dependencies
from typing import List

router = APIRouter()

# Test endpoints
@router.get("/tests", response_model=List[schemas.Test])
def read_tests(skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    tests = crud.get_tests(db, skip=skip, limit=limit)
    return tests

@router.post("/tests", response_model=schemas.Test)
def create_test(test: schemas.TestCreate, db: Session = Depends(dependencies.get_db)):
    return crud.create_test(db=db, test=test)

@router.put("/tests/{test_id}", response_model=schemas.Test)
def update_test(test_id: int, test: schemas.TestCreate, db: Session = Depends(dependencies.get_db)):
    return crud.update_test(db=db, test_id=test_id, test=test)

@router.delete("/tests/{test_id}", response_model=schemas.Test)
def delete_test(test_id: int, db: Session = Depends(dependencies.get_db)):
    return crud.delete_test(db=db, test_id=test_id)

# Question endpoints
@router.get("/tests/{test_id}/questions", response_model=List[schemas.Question])
def read_questions(test_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    questions = crud.get_questions(db, test_id=test_id, skip=skip, limit=limit)
    return questions

@router.post("/tests/{test_id}/questions", response_model=schemas.Question)
def create_question(test_id: int, question: schemas.QuestionCreate, db: Session = Depends(dependencies.get_db)):
    return crud.create_question(db=db, question=question)

@router.put("/questions/{question_id}", response_model=schemas.Question)
def update_question(question_id: int, question: schemas.QuestionCreate, db: Session = Depends(dependencies.get_db)):
    return crud.update_question(db=db, question_id=question_id, question=question)

@router.delete("/questions/{question_id}", response_model=schemas.Question)
def delete_question(question_id: int, db: Session = Depends(dependencies.get_db)):
    return crud.delete_question(db=db, question_id=question_id)

# Answer endpoints
@router.get("/questions/{question_id}/answers", response_model=List[schemas.Answer])
def read_answers(question_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    answers = crud.get_answers(db, question_id=question_id, skip=skip, limit=limit)
    return answers

@router.post("/questions/{question_id}/answers", response_model=schemas.Answer)
def create_answer(question_id: int, answer: schemas.AnswerCreate, db: Session = Depends(dependencies.get_db)):
    return crud.create_answer(db=db, answer=answer)

@router.put("/answers/{answer_id}", response_model=schemas.Answer)
def update_answer(answer_id: int, answer: schemas.AnswerCreate, db: Session = Depends(dependencies.get_db)):
    return crud.update_answer(db=db, answer_id=answer_id, answer=answer)

@router.delete("/answers/{answer_id}", response_model=schemas.Answer)
def delete_answer(answer_id: int, db: Session = Depends(dependencies.get_db)):
    return crud.delete_answer(db=db, answer_id=answer_id)
